# Switch temperature between F to C
tempStr = input('please input temperature(F/C):\n')
if tempStr[0:1] in ['F','f']:
    C = (eval(tempStr[1:]) - 32)/1.8
    print("C{:.2f}".format(C))
elif tempStr[0:1] in ['C','c']:
    F = (eval(tempStr[1:]) * 1.8) + 32
    print("F{:.2f}".format(F))
else:
	print('input error!')
