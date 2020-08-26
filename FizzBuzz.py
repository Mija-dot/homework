print("Welcome to the FizzBuzz game!")

number = input("Please enter a number between 1 and 100: ")
number = int(number)
for num in range(1, number+1):

    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")

    elif num % 3 == 0:
        print("fizz")

    elif num % 5 == 0:
        print("buzz")

    else:
        print(num)