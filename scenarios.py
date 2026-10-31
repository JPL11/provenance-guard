"""Three-trial scenarios mapped to the five targets in criteria.md."""

import csv
from pathlib import Path

from calibration_samples import SAMPLES

def attack_texts(wanted_ids):
    """Reuse the supplied, labelled challenge texts for comparison scenarios."""
    path = Path(__file__).parent / "attack_set" / "attacks.csv"
    if not path.exists():
        return {}
    with path.open(encoding="utf-8", newline="") as stream:
        return {row["id"]: row["text"] for row in csv.DictReader(stream)
                if row["id"] in wanted_ids}


_comparison = attack_texts({"EV01", "EV02", "EV03", "EV04", "EV05",
                            "EV10", "FP01", "FP02", "FP03", "FP04",
                            "FP05", "FP06", "FP07", "FP08"})
AI_TEXTS = [
    "Artificial intelligence is changing how organizations manage routine work. Automated systems can sort information, draft summaries, and identify patterns across large collections of records. These tools may help employees spend less time on repetitive tasks and more time reviewing important decisions. Their benefits depend on careful implementation. Teams should explain when automated tools are used, protect sensitive information, and check results for errors. A thoughtful process combines machine speed with human judgment, making the technology useful while keeping responsibility with the people who rely on it.",
    "Remote work has become a lasting part of many workplaces. Employees can avoid long commutes and arrange focused time around their responsibilities. Organizations can also recruit people who live outside a central office location. However, distance creates new communication challenges. Managers need clear expectations, regular conversations, and shared records of decisions. Workers benefit when they know where to ask questions and how quickly to expect a response. A successful remote policy balances flexibility with dependable collaboration, so people can work independently without losing a sense of connection to their team.",
    "Public transportation can improve daily life in growing cities. Reliable buses and trains give residents another way to reach work, school, and essential services. When more people use transit, streets may have less congestion and neighborhoods can reduce some forms of pollution. These outcomes require thoughtful planning. Routes should connect the places people need to visit, and schedules should remain dependable throughout the day. Cities must also maintain stations and vehicles so that the system feels safe and accessible. Investment in transit works best when local communities help shape its priorities.",
    "Good communication is an important part of effective education. Students learn more confidently when instructions are clear and feedback arrives in time to be useful. Teachers can support this process by explaining goals, checking for understanding, and offering several ways to ask for help. Families also benefit from regular updates about progress and upcoming work. Technology can make messages easier to share, but it cannot replace a respectful conversation. A learning environment improves when students know what is expected and believe that questions will be taken seriously.",
    "Many communities are looking for practical ways to reduce household waste. Residents can start by repairing useful items, choosing products with less packaging, and sorting materials according to local recycling rules. These individual habits matter more when public services make them convenient. Clear collection schedules and accessible drop-off locations help people participate consistently. Businesses can contribute by designing durable goods and explaining how customers should dispose of them. Waste reduction is a shared responsibility, and steady improvements across households, companies, and local government can conserve resources over time.",
]
KNOWN_HUMAN_PROXY = [
    *[_comparison[key] for key in ("FP01", "FP02", "FP03", "FP04",
                                   "FP05", "FP06", "FP07", "FP08")
      if key in _comparison],
    SAMPLES["clear_human"], SAMPLES["formal_human"],
]
_running = (Path(__file__).parent / "RUNNING.md").read_text(encoding="utf-8")
RUNNING_HUMAN = " ".join(_running.split("**Signal one** measures", 1)[1]
                          .split("**Signal two** cannot read.", 1)[0].split())
_design = (Path(__file__).parent / "design.md").read_text(encoding="utf-8")
DESIGN_HUMAN = " ".join(_design.split("A person writes a plain paragraph.", 1)[1]
                         .split("\n\n", 1)[0].split())
HUMAN_TEXTS = [
    _comparison["FP01"], _comparison["FP03"], SAMPLES["clear_human"],
    DESIGN_HUMAN, RUNNING_HUMAN,
]
BORDERLINE_TEXTS = [_comparison[key] for key in ("EV02", "EV03", "EV04", "FP01")
                    if key in _comparison]

SCENARIOS = [
    {"name": "known human proxy (not owner-authored)", "criterion": 1,
     "texts": KNOWN_HUMAN_PROXY},
    {"name": "score separation", "criterion": 2,
     "groups": {"AI": AI_TEXTS, "human": HUMAN_TEXTS}},
    {"name": "label coverage", "criterion": 3,
     "texts": [SAMPLES["clear_human"], SAMPLES["formal_human"]] * 2 + BORDERLINE_TEXTS +
              ([_comparison["EV10"]] * 4 if "EV10" in _comparison else [])},
    {"name": "appeal record", "criterion": 4,
     "appeal_texts": [SAMPLES["clear_human"]] * 5},
    {"name": "bad input", "criterion": 5,
     "bodies": [
         {"creator_id": "eval_bad_missing"},
         {"text": "", "creator_id": "eval_bad_empty"},
         {"text": 12, "creator_id": "eval_bad_type"},
         {"text": "x" * 10001, "creator_id": "eval_bad_huge"},
     ]},
]


def validate() -> list[str]:
    problems = []
    if len(KNOWN_HUMAN_PROXY) != 10:
        problems.append("criterion 1 proxy needs ten known-human passages")
    if len(AI_TEXTS) != 5 or len(HUMAN_TEXTS) != 5:
        problems.append("criterion 2 needs five AI and five human comparison passages")
    if len(BORDERLINE_TEXTS) != 4 or len(SCENARIOS[2]["texts"]) != 12:
        problems.append("criterion 3 needs four human, four borderline, and four AI submissions")
    for scenario in SCENARIOS:
        if scenario.get("groups"):
            for name, texts in scenario["groups"].items():
                if not texts:
                    problems.append(f"{scenario['name']}: group {name} is empty")
        elif not scenario.get("texts") and not scenario.get("bodies") and not scenario.get("appeal_texts"):
            problems.append(f"{scenario['name']}: no inputs configured")
    return problems
