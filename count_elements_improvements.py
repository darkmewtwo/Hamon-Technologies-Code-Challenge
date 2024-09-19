from collections import Counter
from typing import Iterable, Dict, Any

#Using collections package
def count_elements(input: Iterable[Any]) -> Dict[Any, int]:
    return dict(Counter(input))

#Using get method in dict
def count_elements(input: Iterable[Any]) -> Dict[Any, int]:
    result = {}
    for key in input:
        result[key] = result.get(key, 0) + 1
    return result