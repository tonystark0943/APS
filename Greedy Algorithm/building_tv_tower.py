sets = [
    ('S1', {'A', 'B', 'C'}, 10),
    ('S2', {'B', 'D'}, 15),
    ('S3', {'C', 'D', 'E'}, 12)
]

neighborhoods = {'A', 'B', 'C', 'D', 'E'}
selected = []
covered = set()
total_cost = 0

while covered != neighborhoods:
    best_set = None
    best_ratio = 0
    
    for name, neighborhoods_covered, cost in sets:
        if (name, neighborhoods_covered, cost) in selected:
            continue
        new_neighborhoods = len(neighborhoods_covered - covered)
        if new_neighborhoods > 0:
            ratio = new_neighborhoods / cost
            if ratio > best_ratio:
                best_ratio = ratio
                best_set = (name, neighborhoods_covered, cost)
    
    if best_set:
        selected.append(best_set)
        covered.update(best_set[1])
        total_cost += best_set[2]

print("Selected sets:", [s[0] for s in selected])
print("Total cost:", total_cost)
print("Neighborhoods covered:", sorted(covered))
