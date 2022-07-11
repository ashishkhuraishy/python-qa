import random
import time

length = int(input("enter the length of your random number : "))

# setting up a seed value for increasing
# the randomness and using current time in
# seconds as the seed value beacuse that 
# value will be unique every time 
random.seed(time.time())

res = ""
for i in range(length):
    # generating a random digit from 0 - 9
    dig = random.randint(0, 9)
    # appending taht value to result
    res += str(dig)

print("your random number is : ", res)




