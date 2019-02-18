weight = input('请输入体重(公斤)')
weight = float(weight)
height = input('请输入身高(厘米)')
height = float(height)
height1 = height / 100
bmi = weight / (height1**2)
print('bmi=', bmi)
if bmi < 18.5:
	print('体重过轻')
elif bmi >= 18.5 and bmi < 24:
	print('正常范围')
elif 24 <= bmi < 27:
	print('过重')
elif 27 <= bmi < 30:
	print('轻度肥胖')
elif 30 <= bmi < 35:
	print('中度肥胖')
else:
	print('重度肥胖')
