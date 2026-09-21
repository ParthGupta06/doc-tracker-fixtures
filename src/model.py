"""Tiny classifier used as a documentation fixture."""

THRESHOLD = 0.6


def predict(features):
    score = sum(features) / max(len(features), 1)
    return 1 if score > THRESHOLD else 0
