from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    _cache = {}

    @wraps(func)
    def wrapper(*args: Any) -> Any:

        if args in _cache:
            print("Getting from cache")
            return _cache[args]

        print("Calculating new result")
        result = func(*args)
        _cache[args] = result
        return result

    return wrapper
