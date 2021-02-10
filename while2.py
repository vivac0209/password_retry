x=3
password ='a123456'
while x >0:
	x=x-1
	key = input('請輸入密碼')
	if key == 'a123456':
		print('登入成功')
		break
	else:
		print('密碼錯誤!')
		if x > 0:
			print('還有', x ,'次機會')
		else:
			print('end')



