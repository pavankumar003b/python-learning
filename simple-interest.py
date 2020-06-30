# program to find simple interest:

def simple_interest(p,t,r):
  print('the principle is',p)
  print('the time is',t)
  print('the rate is',r)
  
  si=(p * t * r)/100
  
  print('the simple interest is',si)
  return si
  
simple_interest(9, 3, 9)
