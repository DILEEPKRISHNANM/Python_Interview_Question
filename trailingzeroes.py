def factorial(n):
    if n<1:
        print("Error ")
        return None
    elif n==0 or n==1:
        return 1

    else:
        return n*factorial(n-1)



n=18

result = factorial(n)
if result is not None:

    print(result)

count=0

for i in str(result)[::-1]:
    if i == '0':
        count+=1
  

print(count)
