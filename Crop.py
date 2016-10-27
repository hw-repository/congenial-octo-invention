def crop(lo,x,hi):
    return max(lo,min(x,hi))

while True:
    lo = float(input('lo = '))
    x = float(input('x = '))
    hi = float(input('hi = '))
    if (lo<hi):
        print crop(lo,x,hi)
        break
    print 'Incorrect input: lo must be less then hi!'
    
