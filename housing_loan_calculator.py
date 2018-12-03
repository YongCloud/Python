# Average Capital
def average_capital(c,i,t):
    print('===Average Capital===')
    month_c = c / (12 * t)
    month_i = i / 12
    sum_i = 0;
    for i in range(12 * t):
        interest = (c - i * month_c) * month_i
        sum_i += interest
        print("month pay:{:.2f}".format(month_c + interest))
    return sum_i

# Average Capital Plus Interest
def average_capital_plus_interest(c,i,t):
    print('===Average Capital Plus Interest===')
    month_i = i / 12
    month_pay = c * (month_i / (1 - (1 + month_i)**(-12*t)))
    print("month pay:{:.2f}".format(month_pay))
    sum_c = 0
    sum_i = 0
    for i in range(12 * t):
        interest = (c - sum_c) * month_i
        print("month interest:{:.2f}".format(interest))
        sum_i += interest
        sum_c += month_pay - interest
    return sum_i

if __name__ == "__main__":
    c,i,t = eval(input("please input capital,interest and year:"))
    sum_i = average_capital(c,i,t)
    print("total interest:{:.2f}".format(sum_i))
    sum_j = average_capital_plus_interest(c,i,t)
    print("total interest:{:.2f}".format(sum_j))
    print("saving interest:{:.2f}".format(sum_j - sum_i))
    print("===real interest:{:.4f}===".format((1 + i/12)**12 - 1))
