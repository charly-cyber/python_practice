print("Enter 'A' if you want to convert Celsius to Fahrenheit")
print("Enter 'B' if you want to convert Fahrenheit to Celsius")

choice = input("Your choice: ")

if choice == 'A':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenhei = (celsius * 9/5) + 32
    fahrenheit = round(fahrenhei, 2)
    print(f"{celsius}°C is equal to {fahrenheit}°F")
elif choice == 'B':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsiu = (fahrenheit - 32) * 5/9
    celsius = round(celsiu, 2)
    print(f"{fahrenheit}°F is equal to {celsius}°C")
else:
    print("Invalid choice. Please enter 'A' or 'B'.")