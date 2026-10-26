"""Four fixed examples used to inspect the two signals before tuning.

The human passages use the course instructions and the starter's criteria text.
The AI passages were drafted by an AI assistant for this calibration.
These examples are diagnostics, not a claim of detector accuracy.
"""

SAMPLES = {
    "clear_ai": (
        "Artificial intelligence offers many benefits to modern society. "
        "It can improve efficiency, support decision making, and create new "
        "opportunities across a wide range of industries. However, it is "
        "important to consider the ethical implications of these systems. "
        "Organizations should adopt responsible practices, promote transparency, "
        "and work together to ensure that AI benefits everyone."
    ),
    "clear_human": (
        "This is the number people set carelessly. Saying it to someone who'd "
        "be on the receiving end is when that becomes obvious. Working on your "
        "own? Paste the criterion into Claude and ask: My system allows this "
        "rate of wrongly flagging human writing as AI-generated. Write the "
        "message a real writer would send me if they were one of the people "
        "that rate allows. Don't tell me whether my number is right. Read it, "
        "then decide whether your number still stands. It might. That's your "
        "call to make, not the model's."
    ),
    "formal_human": (
        "An acceptance criterion names a number or something plainly "
        "observable. The detector is accurate is an opinion — and perfect AI "
        "detection isn't possible anyway, so it's an opinion about something "
        "nobody can deliver. Of 10 pieces I wrote myself, at most 1 is labelled "
        "high-confidence AI is a criterion. Under each, write a sentence or "
        "two on why that target."
    ),
    "edited_ai": (
        "Artificial intelligence offers many benefits to modern society. "
        "It can improve efficiency; sometimes, anyway. It supports decisions "
        "and creates new opportunities across industries, though the results "
        "aren't always tidy. Organizations should consider ethical implications, "
        "promote transparency, and work together to make these systems useful. "
        "Still, who gets to decide what 'useful' means?"
    ),
}


if __name__ == "__main__":
    import detector
    import scoring
    import stylometry

    for name, passage in SAMPLES.items():
        model_score = detector.model_signal(passage)
        style_score = stylometry.style_signal(passage)
        combined = scoring.combine_signals(model_score, style_score)
        print(f"{name:14} model={model_score:.4f} style={style_score:.4f} combined={combined:.4f}")
