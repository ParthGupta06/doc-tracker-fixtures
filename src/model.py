"""Tiny classifier used as a documentation fixture."""


def predict(features):
    score = sum(features) / max(len(features), 1)
    return 1 if score > 0.5 else 0
