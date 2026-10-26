# Acceptance criteria — Provenance Guard

Recorded before implementation. The TA selected the targets in criteria 1 and 2; criteria 3–5 are illustrative proposals to review before using this as a student example.

## 1. False positives on known human writing

Of 10 passages that I know were written by people, **0 of 10** may receive the `ai` (high-confidence AI) label.

**Why this target:** A wrong public accusation is costly to a writer. The high-confidence label should require stronger evidence than these ordinary human samples provide.

## 2. Score separation

For five clearly AI-generated passages and five clearly human-written passages of roughly 80–180 words, the median combined AI score of the AI group must be at least **0.30 higher** than the median of the human group.

**Why this target:** A three-tenths gap is large enough to show that the two groups are meaningfully separated on a 0–1 scale, while the median keeps one unusual passage from deciding the result.

## 3. Label coverage

Across a planned set of 12 submissions (four clear human, four borderline, and four clear AI), **all three** guesses — `human`, `unsure`, and `ai` — must appear at least once.

**Why this target:** If a band cannot be reached by realistic text, readers cannot benefit from it and the thresholds or signal calibration need attention.

## 4. Appeal record

For **five** successful appeals of five different submitted `content_id` values, each response must say `under_review`, and `/log` must contain exactly one matching appeal event while retaining the original decision and its scores.

**Why this target:** A writer needs a reliable route to challenge a wrong label. Keeping the original decision makes the review auditable.

## 5. Bad input

For each of four inputs — missing `text`, empty `text`, non-string `text`, and text over **10,000 characters** — `/submit` must return a client error (**400** for the first three, **413** for the fourth), write no decision, and never return 500.

**Why this target:** Invalid input should not become a false classification or an unbounded model request, and the caller should get an actionable error.
