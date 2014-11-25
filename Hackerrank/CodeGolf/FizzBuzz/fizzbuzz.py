for i in range(1,101):
    l = ''
    if i%3 > 0 and i%5 > 0:
        l = str(i)
    if i%3==0:
        l = 'Fizz'
    if i%5==0:
        l += "Buzz"
    print(l)

