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