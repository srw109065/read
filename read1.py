data = []
conut = 0
	
with open("reviews.txt", "r") as r:
	for line in r:
		data.append(line)
		conut += 1
		if conut % 1000 == 0:
			print(len(data))
print("總共", len(data), "萬筆資料") 

print(data[0])

total_sum = 0
tosum = 0
for d in data:
	total_sum = total_sum + len(d)
	tosum = total_sum / len(data)
print("平均", tosum, "總文字長度") 
#print(total_sum / len(data))

new = []

for c in data:
	if len(c) < 100:
		new.append(c)
print("一共有", len(new), "筆留言長度小於100")

good = []

for s in data:
	if 'good' in s:
		good.append(s)
print('一共有', len(good), '筆留言提到good')

#文字記數#使用者查詢
wc = {} # word_count 字典記數
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1 #新增重複出現的key+1
		else:
			wc[word] = 1 #新增新的key進WC字典

for word in wc:
	if wc[word] > 10000:
		print(word, wc[word])

print(len(wc))

while True:
	word = input("請問你想要查詢甚麼字: ")
	if word == "q":
		break
	if word in wc:
		print(word, "出現過的次數: ", wc[word])
	else:
		print("這個字沒有出現過喔")

print("感謝使用本查詢功能")