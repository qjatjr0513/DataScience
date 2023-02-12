import fah_converter

print("Enter a celcius value: ")
celcius = float(input())
fahrenheit = fah_converter.cover_c_to_f(celcius)
print("That's", fahrenheit, "degrees Fahrenheit")