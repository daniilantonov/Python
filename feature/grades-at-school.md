file = open('input.txt','r')
data = {}
for line in data :
    name, score = line.split(',')
    if name not in data:
        data[name] = []
        data[name].append(int(score))
for name, scores in data.items():
    data[name] = (min(scores), sum(scores) / len(scores), max(scores))
with open('output.txt', 'r') as f:
    for name, scores in data.items():
        f.write(f"{name},{scores[0]},{scores[1]},{scores[2]}\n")
