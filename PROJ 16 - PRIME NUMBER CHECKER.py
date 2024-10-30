def is_prime(num):
    flag = True
    if num <=1:
        flag = False
    for loop in range(2,num):
        if num % loop == 0:
            flag = False
    print(flag)

is_prime(int(input("Input a number to check if it is a prime number of not: ")))