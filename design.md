# Submission trace and endpoint contract

This is the design recorded before implementing the routes.

## Text to reader label

1. `POST /submit` receives JSON with `text` and `creator_id` and rejects malformed or oversized input.
2. The service creates a `content_id` so the decision can be found and appealed later.
3. `detector.py::model_signal` measures how predictable the words are to the local GPT-2 model and returns a 0–1 AI-likeness score. Plain human writing can be predictable; unusual AI writing can be surprising. It cannot establish who wrote the text.
4. `stylometry.py::style_signal` measures sentence length variation, word variety, and punctuation patterns and returns a second 0–1 score. It cannot understand meaning or authorship; edits that change the text's shape can move it.
5. `scoring.py::combine_signals` combines those scores, treating a strong disagreement as uncertainty. A higher combined score means more AI-like, not proof of AI authorship.
6. `scoring.py::score_to_label` chooses `human`, `unsure`, or `ai` and its full reader-facing sentence.
7. `audit.py::log_decision` records the timestamp, ID, creator, scores, guess, label, and status in `logs/audit.jsonl`; `/submit` returns the decision to the caller for display.

## The false-positive path

A person writes a plain paragraph. The model may find it predictable and assign a high AI-like score, while the style signal may also find regular sentences. If the combined score crosses the AI band, the writer sees an automated label saying the text may be AI-generated, even though it is theirs. The response gives them the `content_id`; they can send it and their explanation to `POST /appeal`. The service then appends an `under_review` event without changing the original decision. A human review is still needed; an appeal does not automatically reverse the label.

## Endpoint contract

| Route | Request JSON | Success response | Errors |
|---|---|---|---|
| `POST /submit` | `text`: nonempty string up to 10,000 characters; `creator_id`: nonempty string | HTTP 200 with `content_id` (string), `creator_id` (string), `guess` (`human`, `unsure`, `ai`), `confidence` (0–1 combined AI-like score), `label` (full sentence), `model_score` (0–1), `style_score` (0–1), `status` (`decided`) | 400 for malformed/missing fields; 413 for oversized text; 503 if the model cannot run |
| `POST /appeal` | `content_id`: existing ID; `reasoning`: nonempty string up to 2,000 characters | HTTP 200 with `content_id`, `status` (`under_review`), and `message` (confirmation) | 400 for malformed/missing fields; 404 for unknown ID; 409 for an already appealed ID |

`GET /log` returns the append-only decision and appeal entries. An appeal entry shares the original `content_id` and records the writer's reasoning and new status. The latest event determines current status; the original decision remains available.
