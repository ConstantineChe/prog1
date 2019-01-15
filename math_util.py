import math

def is_positive_real(x):
    try: return math.inf > x > 0
    except Exception: return False

def is_natural_number(x):
    try: return int(x) == x and x > 0
    except Exception: return False

def is_finite(x):
    try:
        x = float(x)
        return not math.isinf(x)
    except Exception: return False
