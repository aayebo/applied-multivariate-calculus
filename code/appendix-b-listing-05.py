def unit_vector(v):
    """Return v/||v|| for a nonzero numerical vector."""
    v = np.asarray(v, dtype=float)
    magnitude = np.linalg.norm(v)
    if magnitude == 0:
        raise ValueError("The zero vector has no unit direction")
    return v / magnitude

print(unit_vector([3, 4, 0]))
