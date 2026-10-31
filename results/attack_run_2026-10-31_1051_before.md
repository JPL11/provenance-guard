# Attack run — before

> Superseded first pass; the final baseline with exact inputs and human verdicts is results/attack_run_2026-10-31_1102_before.md.


- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-10-31 10:51
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `185b2ffa-450f-4173-80ac-88cfbdb4c39e` | unsure | 0.320 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `80bdf3f3-1e9c-4425-b35e-07cf4ddb3428` | unsure | 0.499 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `2c88c917-cf24-47d6-a6cf-c04b6e2b39f8` | unsure | 0.577 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `d19a67b9-1bc7-40a3-9958-35228941aa9a` | unsure | 0.606 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `2e0bfe23-5230-4369-a0bc-7cf8dbea528b` | human | 0.285 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `fcf681f3-1f1c-4f20-b802-19bbfd95f558` | unsure | 0.493 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `d60accca-8472-4e10-bf05-6bd458876125` | unsure | 0.525 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `261c6452-d1c4-4783-accc-911a6b3a48e5` | human | 0.307 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `3fa0eced-2280-490a-809e-3d9e5f61b698` | unsure | 0.599 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `ac4c6323-9a35-465d-a43d-23b7b5352edc` | ai | 0.877 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `4d161e4f-9708-413a-8e4d-c3e19560c55b` | unsure | 0.560 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `0dc305f4-2f26-48b4-a238-4e6d619c3e9e` | ai | 0.712 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `ebfd167e-de92-4cb0-9fcb-a39122ed88f6` | ai | 0.742 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `b8539c8b-5df2-4c4d-b3b8-aa63d1285c6a` | ai | 0.740 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `d3771f98-1b5e-4c94-837e-537708c51f2b` | ai | 0.754 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `06e79a20-8d2d-4303-a3f3-d4665dbec543` | unsure | 0.690 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `1fea9767-7cf1-44c5-94c1-7604b39c9f18` | unsure | 0.690 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `c2a5258e-f6d9-4a31-a4d6-6abdc7256898` | unsure | 0.324 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `f8ba3f81-a6e4-488c-87d1-8490e60de193` | unsure | 0.409 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `dc1e651d-e89d-4646-a195-fb1f39403a54` | human | 0.200 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `4d5d21c8-bc39-48ae-9efc-14771df57496` | unsure | 0.558 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `6ecc2753-ae45-4b2d-adf7-d799ebc04651` | unsure | 0.469 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `bdd8cd48-124f-41e6-bacb-c6ec231ad558` | unsure | 0.501 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `5389980f-2f2c-4e5c-a240-6de6cc118ce5` | unsure | 0.520 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `05817c90-0afe-4335-9766-8c3ae6e3ddd9` | unsure | 0.320 |  |
| MF04 | malformed | text is only punctuation | 200 | `85de5d4f-0ead-4a7a-90dd-5d3e486b9a65` | unsure | 0.320 |  |
| MF05 | malformed | text is a very long single word | 200 | `f25cd9f3-4828-40e9-a09b-aa284614698b` | unsure | 0.690 |  |
| MF06 | malformed | text is emoji only | 200 | `c68a67ad-06ff-4eee-a6c3-879bbd25c3e1` | unsure | 0.690 |  |
| MF07 | malformed | text is right-to-left script | 200 | `e094ae0a-35b2-4545-8e6e-461d06f1daa5` | ai | 0.805 |  |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1f805ae9-9aac-4ccb-a5c3-2673b3b8fbeb` | unsure | 0.320 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `490a33cf-8430-4372-9a67-0cca52af3cc2` | unsure | 0.320 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5dab8c14-7f9e-4d19-8441-04234f9b04eb` | unsure | 0.320 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5a96c961-c009-42fc-8441-b5670d5068b5` | unsure | 0.320 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b9c1ae29-8c26-4f6c-ac91-dc7639ba0f85` | unsure | 0.320 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a27b4550-339c-4877-a64f-59f3c216e75f` | unsure | 0.320 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1abaeb97-ae6d-445a-a090-82b59b9486f6` | unsure | 0.320 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `243b6ad1-53e6-49cc-8ccc-6e8f910cb05e` | unsure | 0.320 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e5ae54ac-a804-48a2-ab5c-c79e292372ef` | unsure | 0.320 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1f3f83aa-9e7a-4694-818f-b2f05b369811` | unsure | 0.320 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "185b2ffa-450f-4173-80ac-88cfbdb4c39e",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.32,
  "model_score": 0.1635,
  "style_score": 0.6191,
  "label": "We cannot tell who wrote this text from these checks. No AI claim is being made; the writer can share context or request a review.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "80bdf3f3-1e9c-4425-b35e-07cf4ddb3428",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.4993,
  "model_score": 0.5943,
  "style_score": 0.2142,
  "label": "We cannot tell who wrote this text from these checks. No AI claim is being made; the writer can share context or request a review.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "2c88c917-cf24-47d6-a6cf-c04b6e2b39f8",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5766,
  "model_score": 0.6662,
  "style_score": 0.3078,
  "label": "We cannot tell who wrote this text from these checks. No AI claim is being made; the writer can share context or request a review.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "d19a67b9-1bc7-40a3-9958-35228941aa9a",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.6057,
  "model_score": 0.6114,
  "style_score": 0.5887,
  "label": "We cannot tell who wrote this text from these checks. No AI claim is being made; the writer can share context or request a review.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "2e0bfe23-5230-4369-a0bc-7cf8dbea528b",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.2847,
  "model_score": 0.3212,
  "style_score": 0.1753,
  "label": "This text shows more signs of human writing, but an automated check cannot verify who wrote it.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "fcf681f3-1f1c-4f20-b802-19bbfd95f558",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.4932,
  "model_score": 0.5727,
  "style_score": 0.2547,
  "label": "We cannot tell who wrote this text from these checks. No AI claim is being made; the writer can share context or request a review.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "d60accca-8472-4e10-bf05-6bd458876125",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.5252,
  "model_score": 0.5862,
  "style_score": 0.3423,
  "label": "We cannot tell who wrote this text from these checks. No AI claim is being made; the writer can share context or request a review.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "261c6452-d1c4-4783-accc-911a6b3a48e5",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.3068,
  "model_score": 0.2452,
  "style_score": 0.4914,
  "label": "This text shows more signs of human writing, but an automated check cannot verify who wrote it.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "3fa0eced-2280-490a-809e-3d9e5f61b698",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.5988,
  "model_score": 0.7042,
  "style_score": 0.2826,
  "label": "We cannot tell who wrote this text from these checks. No AI claim is being made; the writer can share context or request a review.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "ac4c6323-9a35-465d-a43d-23b7b5352edc",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.877,
  "model_score": 0.9792,
  "style_score": 0.5703,
  "label": "This text shows strong signs of AI generation, but this automated assessment can be wrong. If you wrote it, you can request a review using your content ID.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "4d161e4f-9708-413a-8e4d-c3e19560c55b",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5601,
  "model_score": 0.6175,
  "style_score": 0.3877,
  "label": "We cannot tell who wrote this text from these checks. No AI claim is being made; the writer can share context or request a review.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "0dc305f4-2f26-48b4-a238-4e6d619c3e9e",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.7122,
  "model_score": 0.7387,
  "style_score": 0.6327,
  "label": "This text shows strong signs of AI generation, but this automated assessment can be wrong. If you wrote it, you can request a review using your content ID.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "ebfd167e-de92-4cb0-9fcb-a39122ed88f6",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.7416,
  "model_score": 0.8051,
  "style_score": 0.551,
  "label": "This text shows strong signs of AI generation, but this automated assessment can be wrong. If you wrote it, you can request a review using your content ID.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "b8539c8b-5df2-4c4d-b3b8-aa63d1285c6a",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.7397,
  "model_score": 0.8329,
  "style_score": 0.46,
  "label": "This text shows strong signs of AI generation, but this automated assessment can be wrong. If you wrote it, you can request a review using your content ID.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "d3771f98-1b5e-4c94-837e-537708c51f2b",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.7536,
  "model_score": 0.8005,
  "style_score": 0.613,
  "label": "This text shows strong signs of AI generation, but this automated assessment can be wrong. If you wrote it, you can request a review using your content ID.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "06e79a20-8d2d-4303-a3f3-d4665dbec543",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.69,
  "model_score": 0.8814,
  "style_score": 0.3171,
  "label": "We cannot tell who wrote this text from these checks. No AI claim is being made; the writer can share context or request a review.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "1fea9767-7cf1-44c5-94c1-7604b39c9f18",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.69,
  "model_score": 0.8816,
  "style_score": 0.3504,
  "label": "We cannot tell who wrote this text from these checks. No AI claim is being made; the writer can share context or request a review.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "c2a5258e-f6d9-4a31-a4d6-6abdc7256898",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.3236,
  "model_score": 0.3223,
  "style_score": 0.3276,
  "label": "We cannot tell who wrote this text from these checks. No AI claim is being made; the writer can share context or request a review.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "f8ba3f81-a6e4-488c-87d1-8490e60de193",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.4094,
  "model_score": 0.4625,
  "style_score": 0.25,
  "label": "We cannot tell who wrote this text from these checks. No AI claim is being made; the writer can share context or request a review.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "dc1e651d-e89d-4646-a195-fb1f39403a54",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.2004,
  "model_score": 0.2044,
  "style_score": 0.1883,
  "label": "This text shows more signs of human writing, but an automated check cannot verify who wrote it.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "4d5d21c8-bc39-48ae-9efc-14771df57496",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5584,
  "model_score": 0.5943,
  "style_score": 0.4505,
  "label": "We cannot tell who wrote this text from these checks. No AI claim is being made; the writer can share context or request a review.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "6ecc2753-ae45-4b2d-adf7-d799ebc04651",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.4687,
  "model_score": 0.4998,
  "style_score": 0.3752,
  "label": "We cannot tell who wrote this text from these checks. No AI claim is being made; the writer can share context or request a review.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "bdd8cd48-124f-41e6-bacb-c6ec231ad558",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.5015,
  "model_score": 0.6401,
  "style_score": 0.0857,
  "label": "We cannot tell who wrote this text from these checks. No AI claim is being made; the writer can share context or request a review.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "5389980f-2f2c-4e5c-a240-6de6cc118ce5",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5196,
  "model_score": 0.5583,
  "style_score": 0.4035,
  "label": "We cannot tell who wrote this text from these checks. No AI claim is being made; the writer can share context or request a review.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "05817c90-0afe-4335-9766-8c3ae6e3ddd9",
  "creator_id": "attacker_MF03",
  "guess": "unsure",
  "confidence": 0.32,
  "model_score": 0.0,
  "style_score": 0.5,
  "label": "We cannot tell who wrote this text from these checks. No AI claim is being made; the writer can share context or request a review.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "85de5d4f-0ead-4a7a-90dd-5d3e486b9a65",
  "creator_id": "attacker_MF04",
  "guess": "unsure",
  "confidence": 0.32,
  "model_score": 0.0112,
  "style_score": 0.5,
  "label": "We cannot tell who wrote this text from these checks. No AI claim is being made; the writer can share context or request a review.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "f25cd9f3-4828-40e9-a09b-aa284614698b",
  "creator_id": "attacker_MF05",
  "guess": "unsure",
  "confidence": 0.69,
  "model_score": 0.9976,
  "style_score": 0.5,
  "label": "We cannot tell who wrote this text from these checks. No AI claim is being made; the writer can share context or request a review.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "c68a67ad-06ff-4eee-a6c3-879bbd25c3e1",
  "creator_id": "attacker_MF06",
  "guess": "unsure",
  "confidence": 0.69,
  "model_score": 0.9969,
  "style_score": 0.5,
  "label": "We cannot tell who wrote this text from these checks. No AI claim is being made; the writer can share context or request a review.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "e094ae0a-35b2-4545-8e6e-461d06f1daa5",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.8048,
  "model_score": 0.9064,
  "style_score": 0.5,
  "label": "This text shows strong signs of AI generation, but this automated assessment can be wrong. If you wrote it, you can request a review using your content ID.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 413,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "1f805ae9-9aac-4ccb-a5c3-2673b3b8fbeb",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.32,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We cannot tell who wrote this text from these checks. No AI claim is being made; the writer can share context or request a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "490a33cf-8430-4372-9a67-0cca52af3cc2",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.32,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We cannot tell who wrote this text from these checks. No AI claim is being made; the writer can share context or request a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "5dab8c14-7f9e-4d19-8441-04234f9b04eb",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.32,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We cannot tell who wrote this text from these checks. No AI claim is being made; the writer can share context or request a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "5a96c961-c009-42fc-8441-b5670d5068b5",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.32,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We cannot tell who wrote this text from these checks. No AI claim is being made; the writer can share context or request a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "b9c1ae29-8c26-4f6c-ac91-dc7639ba0f85",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.32,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We cannot tell who wrote this text from these checks. No AI claim is being made; the writer can share context or request a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "a27b4550-339c-4877-a64f-59f3c216e75f",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.32,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We cannot tell who wrote this text from these checks. No AI claim is being made; the writer can share context or request a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "1abaeb97-ae6d-445a-a090-82b59b9486f6",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.32,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We cannot tell who wrote this text from these checks. No AI claim is being made; the writer can share context or request a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "243b6ad1-53e6-49cc-8ccc-6e8f910cb05e",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.32,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We cannot tell who wrote this text from these checks. No AI claim is being made; the writer can share context or request a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "e5ae54ac-a804-48a2-ab5c-c79e292372ef",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.32,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We cannot tell who wrote this text from these checks. No AI claim is being made; the writer can share context or request a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "1f3f83aa-9e7a-4694-818f-b2f05b369811",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.32,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We cannot tell who wrote this text from these checks. No AI claim is being made; the writer can share context or request a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
