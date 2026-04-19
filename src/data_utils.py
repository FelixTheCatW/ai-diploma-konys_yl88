def find_by_name(data, name):
    for item in data:
        if item["name"] == name:
            return item
    return None

def filter_by_value(data, key, value):
    return [d for d in data if d[key]==value]

def count_items(data):
    return len(data)