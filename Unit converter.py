
print("Hello! Welcome to the unit converter that converts kilometers into miles.")

while True:
    print("Enter a number of kilometers to be converted convert into miles. Enter only a number!")

    km = input("Kilometers: ")

    km = float(km.replace(",", "."))

    miles = km * 0.6213

    print("{0} kilometers is {1} miles.".format(km, miles))

    question = input("Would you like to do another conversion (yes/no): ")

    if  question != "yes":
        break

