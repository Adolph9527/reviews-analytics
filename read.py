data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
#print(len(data)) #1,000,000

print('檔案讀取完畢, 總共有', len(data), '筆資料')


#print(data[0])
#print('==============')
#print(data[1])


#留言的平均長度
sum_len = 0
for d in data:
	#len(d)  每一筆留言的字(母)數
	sum_len = sum_len + len(d) #所有留言的字(母)數
print('每筆留言的平均字數是', sum_len/len(data))  #所有字(母)數/100萬筆留言 = 平均每筆留言的字(母)數

#篩選清單
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('共有', len(new), '筆資料長度小於100')

#print(new[0])
#print(new[1])

good = []
for d in data:     #d是單一筆留言
	if 'good' in d:    #if (True / False)
		good.append(d)
print('共有', len(good), '筆留言提到good')		


#list comprehension

good = [d for d in data if 'good' in d]
#第一個字為運算 在此處為good.append(d)的運算
#print(good)

bad = [d for d in data]
#print(bad)

bad = []
for d in data:
		bad.append('bad' in d) #Boolean
print(bad)