data = []

with open("reviews.txt", "r") as r:
	for line in r:
		data.append(line)
print(len(data)) 