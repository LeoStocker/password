i=3
while i >= 1:
	password = input('請輸入密碼: ')
	if password != 'a123456':
		i = i-1
		print('密碼錯誤!','還有',i,'次機會')
	else:
		i = -1
if i == -1:
    print('登入成功')
elif i == 0:
	print('已無登入機會')