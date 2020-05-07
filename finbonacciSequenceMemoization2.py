from functools import lru_cache
import time
start_time = time.time()

@lru_cache(maxsize = 1000)

def fibonacci(i):

    # check input integer
    if type(i) != int()
        raise TypeError("i must be an integer")
    if n < 1:
        raise ValueError("i must be a positive int")

    if i == 1:
        return 1
    elif i == 2:
        return 1
    elif i > 2:
        return fibonacci(i-1) + fibonacci(i-2)
for i in range(1,501):
    print(i, ":", fibonacci(i))


print("Process finished in --- %s seconds ---" % (time.time()- start_time))
