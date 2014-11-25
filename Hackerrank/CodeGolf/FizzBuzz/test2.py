#print(*[(not x%3)*'Fizz'+(not x%5)*'Buzz' or x for x in range(1,101)])
#i=0;exec"i+=1;print(i%3<1)*'Fizz'+(i%5<1)*'Buzz'or i;"*100


print(*[(x%3<1)*'Fizz'+(x%5<1)*'Buzz' or x for x in range(1,101)])
