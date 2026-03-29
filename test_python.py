import sys

def flatten(chunks: list[list[Any]]) -> list[Any]:
    return [item for chunk in chunks for item in chunk]


chunks = [[1, 2], [3], []]
a = flatten(chunks)
print(a)
assert flatten(chunks) == [1, 2, 3]