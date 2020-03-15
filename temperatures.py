"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print("Result: {:.2f} F".format(fahrenheit))
    elif choice == "F":
        get_fahrenheit = float(input("Enter Fahrenheit: "))
        convert_fahrenheit = 5 / 9 * (get_fahrenheit - 32)
        print("Result: {:.2f} C".format(convert_fahrenheit))
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")