n = int(input())
score_map = {}

for _ in range(n):
    name, score = input().split()
    score = int(score)

    if score not in score_map:
        score_map[score] = name
    else:
        score_map[score] = min(score_map[score], name)

# sort scores from low to high
sorted_scores = sorted(score_map.keys())

# collect names
result = [score_map[score] for score in sorted_scores]

print(",".join(result))
