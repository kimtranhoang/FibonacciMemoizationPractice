import time
start_time = time.time()

fibonacci_cache = {}


def fibonacci(i): 
    # if have cache value reuturn it
    if i in fibonacci_cache:
        return fibonacci_cache[i]
    # compute ith term
    if i == 1:
            value = 1
    elif i == 2:
        value = 1
    elif i > 2:
        value = fibonacci(i-1) + fibonacci(i-2)

    # store cache in dictionary
    fibonacci_cache[i] = value
    return value

i = int(input('Enter a number:'))
for i in range(1,i+1):
    print(i, ":", fibonacci(i)) 

print("Process finished in --- %s seconds ---" % (time.time()- start_time))