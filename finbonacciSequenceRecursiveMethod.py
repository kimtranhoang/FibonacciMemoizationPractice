# recursive method
# too slow if have a range of 100

def fibonacci(i):

    if i == 1:
        return 1
    elif i == 2:
        return 1
    elif i >2:
        return fibonacci(i-1) + fibonacci(i-2)

i = int(input('Enter a number:'))
# print(list(range(1,i+1)))

for i in range(1,i+1):
    print(i, ":", fibonacci(i))