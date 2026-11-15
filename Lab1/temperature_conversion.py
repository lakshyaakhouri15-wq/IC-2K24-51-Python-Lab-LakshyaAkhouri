"""Convert a temperature from Celsius to Fahrenheit."""

temperature_c = float(input("Enter the temperature in Celsius: "))

temperature_f = (temperature_c * 1.8) + 32

print(f"Celsius: {temperature_c:.2f} °C")
print(f"Fahrenheit: {temperature_f:.2f} °F")
