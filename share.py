'''
Sharing Economy
@author xingjian
@since 2019/06/03
'''
# cost function
def cost(n):
    if n == 1:
        return 160
    else:
        return 0.75 * cost(n-1)

# test
for i in range(1,21):
    c = cost(i)
    print("{} {:.2f} {:.2f}".format(i,c,c * i))
