#compound interest

def compound_interest(p,r,t):
    print('the principle is',p)
    print('the rate is',r)
    print('the time is',t)
    ci=p*(pow((1+r/100),t))
    print('compound interest is',ci)
    return ci
compound_interest(1200, 13.5, 24)
