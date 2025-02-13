def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_a_kelvin(celsius):
    return celsius + 273.15

def kelvin_a_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_a_kelvin(fahrenheit):
    celsius = fahrenheit_a_celsius(fahrenheit)
    return celsius_a_kelvin(celsius)

def kelvin_a_fahrenheit(kelvin):
    celsius = kelvin_a_celsius(kelvin)
    return celsius_a_fahrenheit(celsius)

# Ejemplo de uso
temp_celsius = 25
temp_fahrenheit = 77
temp_kelvin = 298.15

print(f"{temp_celsius}°C en Fahrenheit es: {celsius_a_fahrenheit(temp_celsius)}°F")
print(f"{temp_fahrenheit}°F en Celsius es: {fahrenheit_a_celsius(temp_fahrenheit)}°C")
print(f"{temp_celsius}°C en Kelvin es: {celsius_a_kelvin(temp_celsius)} K")
print(f"{temp_kelvin} K en Celsius es: {kelvin_a_celsius(temp_kelvin)}°C")
print(f"{temp_fahrenheit}°F en Kelvin es: {fahrenheit_a_kelvin(temp_fahrenheit)} K")
print(f"{temp_kelvin} K en Fahrenheit es: {kelvin_a_fahrenheit(temp_kelvin)}°F")
