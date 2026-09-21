from src.model import predict


def accuracy(rows, labels):
    hits = sum(1 for r, y in zip(rows, labels) if predict(r) == y)
    return hits / max(len(labels), 1)
