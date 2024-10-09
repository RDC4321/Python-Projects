#fizzbuzz game using loops & if/elif.
#prints numbers 1-100
#if number is divisible by 3 it prints "Fizz"
#if number is divisible by 5 it prints "Buzz"
#if number is divisible by both 3 & 5 it prints "FizzBuzz"
for numbers in range (1,101):
    if numbers%3==0 and numbers%5==0:
        numbers="FizzBuzz"
    elif numbers%5==0:
        numbers="Buzz"
    elif numbers%3==0:
        numbers="Fizz"
    print(numbers)