"""Tiny classifier used as a documentation fixture."""

THRESHOLD = 0.6


def predict(features, weights=None):
    weights = weights or [1.0] * len(features)
    score = sum(f * w for f, w in zip(features, weights)) / max(len(features), 1)
    return 1 if score > THRESHOLD else 0
