data = []
conut = 0

with open("reviews.txt", "r") as r:
	for line in r:
		data.append(line)
		conut += 1
		if conut % 1000 == 0:
			print(len(data))
print("總共", len(data), "萬筆資料") 

total_sum = 0
tosum = 0
for d in data:
	total_sum = total_sum + len(d)
	tosum = total_sum / len(data)
print("平均", tosum, "總文字長度") 
# print(total_sum / len(data))

new = []

for c in data:
	if len(c) < 100:
		new.append(c)
print("一共有", len(new), "筆留言長度小於100")
print(new[0])