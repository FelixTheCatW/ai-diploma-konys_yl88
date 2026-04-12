from functools import reduce
def sum_by_key(rows: list[dict], key: str) -> float:    
    as_number = lambda val: val if (isinstance(val, float) or isinstance(val, int)) and not isinstance(val, bool) else .0
    
    def to_number(v):
        return v if v and (isinstance(v, float) or isinstance(v, int)) and not isinstance(v, bool) else .0

    a = reduce(lambda total, row: total + to_number(row.get(key)), rows, .0)
    print(a)
    return sum(as_number(row.get(key)) for row in rows)


rows = [{"a": 1}, {"a": 2.5}, {"b": 10}, {"a": "x"}]
assert sum_by_key(rows, "a") == 3.5
assert sum_by_key([], "a") == 0.0