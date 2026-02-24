#8a
limit = 100
squares = {i*i: i for i in range(1, limit)}

results = []
for a in range(1, limit):
    for b in range(a, limit):
        s = a*a + b*b
        if s in squares:
            c = squares[s]
            results.append((a, b, c))

print(results)

#8b
limit = 100
sum_map = {}

for c in range(1, limit):
    for d in range(c, limit):
        s = c*c + d*d
        if s not in sum_map:
            sum_map[s] = []
        sum_map[s].append((c, d))

results = []
for a in range(1, limit):
    for b in range(a, limit):
        s = a*a + b*b
        if s in sum_map:
            for c, d in sum_map[s]:
                results.append((a, b, c, d))

print(results)
