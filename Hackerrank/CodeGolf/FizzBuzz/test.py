print(*[(not x%3)*'Fizz'+(not x%5)*'Buzz' or x for x in range(1,101)],sep='\n')
'''
(lambda x: print(x) if x%3==0 else (x-1))(100)

for i in range(1,101):
 l = ''
 if i%3==0:l='Fizz'
 if i%5==0:l+='Buzz'
 print(l if l else i)



for i in range(1,101)
 l = ''
 if i%3==0:l='Fizz'
 if i%5==0:l+='Buzz'
 print(l if l else i)
'''
