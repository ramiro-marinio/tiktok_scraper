"""This module contains a function that converts tiktok number strings to numbers."""
def convert_number(s:str) -> float:
    """Converts a string to a number. 
    The string can be in the format of a number, a number followed by a K, M, or B"""
    s = s.strip().upper()
    if s.endswith('K'):
        return float(s[:-1]) * 1_000
    elif s.endswith('M'):
        return float(s[:-1]) * 1_000_000
    elif s.endswith('B'):
        return float(s[:-1]) * 1_000_000_000
    elif s.isdigit() or (s.replace('.', '', 1).isdigit() and s.count('.') < 2):
        return float(s)
    else:
        raise ValueError("Invalid input string")
