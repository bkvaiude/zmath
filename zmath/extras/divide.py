def divide(x: int, y: int) -> int:
    if y > 0:
        return x / y
    else:
        raise ValueError("y must be positive")
