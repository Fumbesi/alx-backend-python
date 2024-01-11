#!/usr/bin/env python3

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely gets a value from a dictionary, returning the value associated with the given key
    if the key is present, otherwise returning the specified default value.

    Args:
        dct (Mapping): The input dictionary.
        key (Any): The key to lookup in the dictionary.
        default (Union[T, None], optional): The default value to return if the key is not present. Defaults to None.

    Returns:
        Union[Any, T]: The value associated with the key if present, otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
