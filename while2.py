x=3
password ='a123456'
while True:
	key = input('請輸入密碼')
	if key != password:
		x=x-1;
		print('密碼錯誤! 還有' , x ,'次機會');
		if x==0:
			print('end 最多輸入三次');
			break;
	elif key == 'a123456':
		print('登入成功')
		break;



