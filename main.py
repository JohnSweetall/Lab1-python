# Author: John Sweetall jts6052@psu.edu
# Collaborator: Yash Patni yjp5077@psu.edu
# Collaborator: Angus Hendrick ajh97@psu.edu
# Collaborator: Angela Bao ymb5072@psu.edu


temp = float(input("Enter temperature: "))
units = input("Enter units in F° or C°: ")

CelsiusConversion = (1.8 * temp) + 32
FahrenheitConversion = (temp - 32) / 1.8

if units == "F" or units == "f" :
  print (f"{temp}° in Fahrenheit is equivalent to {FahrenheitConversion}° Celsius.")
elif units == "C" or units == "c" :
  print (f"{temp}° in Celsius is equivalent to {CelsiusConversion}° Fahreheit.")
else:
  print (f"That is an invalid unit ( {units} ).")

