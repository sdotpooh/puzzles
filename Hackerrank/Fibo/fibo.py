'''
Sean Vinas
31 Oct 2014
f(0) = 0
f(1) = 1
Use a dictionary to store fibo numbers.
First check if value is in the dict, if not add fib numbers till the value
exceeds the test value. Then check if in the dict to print the required output.
'''
fib = {'0': 0, '1': 1}
highest_value = 1
highest_key = '1'
size = int(input())
for i in range(size):
    f = int(input())
    while f > highest_value:
        #start adding to fib to build dict
        highest_value = fib[str(int(highest_key) - 1)] + fib[highest_key]
        highest_key = str(int(highest_key) + 1)
        fib[highest_key] = highest_value
    if f not in fib.values():
        print('IsNotFibo')
    else:
        print('IsFibo')
