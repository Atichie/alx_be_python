# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    convert Fahrenheit to Celsius using the global conversion factor.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    convert Celsius to Fahrenheit using the global conversion factor.
    """
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR +32

def main():
    try:
        temp = float(input("Enter the temperature to convert: "))
        unit = input("Is the temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'C':
            convert_temp = convert_to_fahrenheit(temp)
            print(f"{temp}c is equal to {converted_temp:2f}F")
        elif unit == 'F':
            converted_temp = convert_to_celsius(temp)
            print(f"{temp}F is equal to {converted_temp:sf}C")
        else:
            print("Invalid input. Please specify 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

name = 'main'
if name == '_main_':
    main()
