#!/usr/bin/env python3

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with the string k and the square of the int/float v.

    Args:
        k (str): The string key.
        v (Union[int, float]): The value, which can be either an int or a float.

    Returns:
        Tuple[str, float]: A tuple containing the string key and the square of v as a float.
    """
    return k, float(v) ** 2

if __name__ == "__main__":
    print(to_kv.__annotations__)
    print(to_kv("eggs", 3))
    print(to_kv("school", 0.02))
