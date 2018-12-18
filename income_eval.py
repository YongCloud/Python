'''
Income evaluator
2018/12/18
'''
# current income
income = 10
# income growth rate per year
r = 0.06
age = 26
retire_age = 60
gap = retire_age - age

sum = 0
for i in range(gap):
    income += income * r
    sum += income
    print("age:{}, income:{:.2f}".format((age+i+1),income))

print("Total income:{:.2f}".format(sum))
