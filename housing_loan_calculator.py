'''
A simple housing loan calculator
'''
def average_capital(amount,rate,term):
    '''
    Average Capital
    amount: loan amount
    rate: interest rate(per year)
    term: loan term(years)
    '''
    print('===Average Capital===')
    mon_principal = amount / (12 * term)
    mon_rate = rate / 12
    sum_i = 0;
    for i in range(12 * term):
        interest = (amount - i * mon_principal) * mon_rate
        sum_i += interest
        print("#{} monthly payment:{:.2f}".format(i + 1,mon_principal + interest))
    return sum_i

def average_capital_plus_interest(amount,rate,term):
    '''
    Average Capital Plus Interest
    amount: loan amount
    rate: interest rate(per year)
    term: loan term(years)
    '''
    print('===Average Capital Plus Interest===')
    mon_rate = rate / 12
    mon_pay = amount * (mon_rate / (1 - (1 + mon_rate) ** (-12 * term)))
    print("monthly payment:{:.2f}".format(mon_pay))
    sum_principal = 0
    sum_i = 0
    for i in range(12 * term):
        interest = (amount - sum_principal) * mon_rate
        print("#{} month interest:{:.2f}".format(i + 1,interest))
        sum_i += interest
        sum_principal += mon_pay - interest
    return sum_i

if __name__ == "__main__":
    amount,rate,term = eval(input("Please input loan amount,interest rate and years:"))
    sum_i = average_capital(amount,rate,term)
    print("Total Interest:{:.2f}".format(sum_i))
    sum_j = average_capital_plus_interest(amount,rate,term)
    print("Total Interest:{:.2f}".format(sum_j))
    print("Average Capital Saving Interest:{:.2f}".format(sum_j - sum_i))
    print("===Real Interest per year:{:.4f}===".format((1 + rate / 12) ** 12 - 1))
