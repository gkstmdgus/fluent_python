ranks = list('AKQ')
patterns = ["Spade", "Heart", "Diamond", "Clover"]

result = [(rank, pattern) for rank in ranks for pattern in patterns]

print(result)

for rank in ranks:
    for pattern in patterns:
        print((rank, pattern))