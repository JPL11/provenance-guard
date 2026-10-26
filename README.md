# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does
1. `POST /submit` accepts JSON with `text` and `creator_id`, and rejects malformed or oversized text.
2. The service assigns a `content_id` that can later identify the decision in an appeal.
3. `detector.py::model_signal` scores how predictable the text is to a local GPT-2 model.
4. `stylometry.py::style_signal` scores sentence length, vocabulary, and punctuation patterns.
5. `scoring.py::combine_signals` makes a combined 0–1 AI-like score and treats strong disagreement as uncertainty.
6. `scoring.py::score_to_label` chooses a machine-readable guess and a sentence for the reader.
7. `audit.py::log_decision` appends the decision and both signal scores to `logs/audit.jsonl`; `/submit` returns the ID, scores, guess, and label.

`confidence` in the API is the combined AI-like score, not a verified probability of authorship. A real writer can be wrongly labeled. They can submit the `content_id` and an explanation to `POST /appeal`; a new `under_review` event is appended while the original decision stays intact for human review. The input and output fields and error responses are specified in [design.md](design.md).
<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->



---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:**
`detector.py::model_signal` converts GPT-2 perplexity into an AI-like score. Low perplexity means the local model found the text predictable.

**Why that might differ between human and AI writing:**
Generated text often favors likely next words, so ordinary model output can be easier for another model to predict.

**What it can't see:**
Predictability is not authorship. Plain human writing can score AI-like; unusual or edited AI text can score human-like. It cannot see a writer's process or evidence of authorship.

### Signal two — the style signal

**What it measures:**
`stylometry.py::style_signal` uses sentence length variation, unique words divided by words, and marks such as commas, semicolons, questions, and dashes per word. Low variation and low punctuation density raise its AI-like score.

**Why that might differ between human and AI writing:**
Generic generated prose often has more even sentence lengths and repeated forms. The style score weights sentence spread 0.60, vocabulary ratio 0.15, and punctuation density 0.25 after scaling them to 0–1.

**What it can't see:**
It has no idea what the sentences mean or who wrote them. A person can write evenly, and a few edits to punctuation or sentence breaks can shift the score without changing authorship. Vocabulary ratio also varies with text length.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:** Use a weighted average of the model and style scores. If their scores differ by at least 0.45, keep the combined result in the unsure band so a strong disagreement cannot create a high-confidence claim.

**The numbers:** `0.75 × model_score + 0.25 × style_score`; disagreement at `|model_score - style_score| >= 0.45`; human scores below `0.32`, AI scores at or above `0.70`, and scores between those bounds are unsure. The disagreement cap is `0.69` for an AI-leaning average and the floor is `0.32` for a human-leaning average.

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**
For the AI-drafted calibration paragraph, the model score was `0.8070` while style was `0.3847`. The gap was `0.4223`, just below the `0.45` disagreement guard; the weighted result was `0.7014`, barely in the AI band. This is a fragile high-confidence result, so the label must still say the assessment can be wrong. A gap of `0.45` or more would force `unsure`.

| Calibration passage | Model | Style | Combined |
|---|---:|---:|---:|
| clear AI draft | 0.8070 | 0.3847 | 0.7014 |
| course prose | 0.2282 | 0.2281 | 0.2282 |
| formal course prose | 0.0745 | 0.3377 | 0.1403 |
| lightly edited AI draft | 0.4840 | 0.2143 | 0.4166 |

The fixed passages are in `calibration_samples.py`. This small set demonstrates a score spread, not accuracy on a population.



---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | `0.00 ≤ score < 0.32` | This text shows more signs of human writing, but an automated check cannot verify who wrote it. |
| unsure | `0.32 ≤ score < 0.70` | We cannot tell who wrote this text from these checks. No AI claim is being made; the writer can share context or request a review. |
| high-confidence AI | `0.70 ≤ score ≤ 1.00` | This text shows strong signs of AI generation, but this automated assessment can be wrong. If you wrote it, you can request a review using your content ID. |

**Why I worded the "unsure" one this way:**
It describes a limit of the checks rather than an accusation about the writer, and it tells the reader a review is available. All three labels were reached through real `/submit` requests: the course-prose sample scored `0.2282`, the lightly edited AI draft `0.4166`, and the clear AI draft `0.7014`.
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->



---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text":"At noon the rain stopped. I waited, then walked home through the garden. Nothing else happened that afternoon.","creator_id":"ta-sample"}'
```
{"confidence":0.5401,"content_id":"21b02b0f-70d0-4b62-b9ec-41c0f1d49231","creator_id":"ta-sample","guess":"unsure","label":"We cannot tell who wrote this text from these checks. No AI claim is being made; the writer can share context or request a review.","model_score":0.5584,"status":"decided","style_score":0.4851}
```json

```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id":"21b02b0f-70d0-4b62-b9ec-41c0f1d49231","reasoning":"Please review this demonstration entry and its recorded scores."}'
```
{"content_id":"21b02b0f-70d0-4b62-b9ec-41c0f1d49231","message":"Your appeal was recorded for human review.","status":"under_review"}
```json

```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=2"
```
{"count":2,"entries":[{"combined_score":0.5401,"content_id":"21b02b0f-70d0-4b62-b9ec-41c0f1d49231","creator_id":"ta-sample","guess":"unsure","label":"We cannot tell who wrote this text from these checks. No AI claim is being made; the writer can share context or request a review.","model_score":0.5584,"status":"decided","style_score":0.4851,"timestamp":"2026-10-26T15:28:37+00:00"},{"content_id":"21b02b0f-70d0-4b62-b9ec-41c0f1d49231","creator_id":"ta-sample","event":"appeal","reasoning":"Please review this demonstration entry and its recorded scores.","status":"under_review","timestamp":"2026-10-26T15:28:41+00:00"}]}
```json

```

---

## How I Used AI

**Moment 1**

- *What I asked for:* Help choosing testable acceptance targets before implementation.
- *What came back:* The assistant offered false-positive limits of 0, 1, or 2 in 10 and score gaps of 0.30, 0.20, or 0.10, then suggested three other areas.
- *What I changed:* I selected 0 in 10 and 0.30. The starter's blank `criteria.md` now records those choices and three clearly marked TA-example proposals before any results were collected.

**Moment 2**

- *What I asked for:* Help implementing the route, signals, labels, and appeal path in milestone order, with actual curl checks and no Codex coauthor credit.
- *What came back:* The assistant wrote the service code and showed four fixed calibration scores, three label responses, and an append-only appeal log.
- *What I changed:* The starter stubs were replaced with a real two-signal route and appeal handler; the README was updated to match measured scores and an honestly worded demonstration appeal. Git commits use my configured identity without a Codex coauthor trailer.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
