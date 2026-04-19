def analyze(data):
    result = []

    for item in data:
        if item["score"] >= 80:
            result.append(item["name"])

    return result


data = [
    {"name": "A", "score": 90},
    {"name": "B", "score": 70},
    {"name": "C", "score": 85}
]

print(analyze(data))