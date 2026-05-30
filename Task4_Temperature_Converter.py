while True:
    print("\n=== Temperature Converter ===")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        celsius = float(input("Enter Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print("Temperature in Fahrenheit:", fahrenheit)

    elif choice == "2":
        fahrenheit = float(input("Enter Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print("Temperature in Celsius:", celsius)

    elif choice == "3":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")