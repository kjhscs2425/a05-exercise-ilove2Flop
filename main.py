
"""
`check_fever` should return `True` if the temperature is `100.4` or higher. For
any lower temperature, it should return `False`.
"""


# Get temperature from user and convert to float

temp = input("Would you like to enter your temperature in Celcius or Fahrenheit: ")
if temp.upper() == "C":
    result = input("Enter your body temprature in Celcuis: ")
    r = float(result)
    if r >= 37.8:
        print("You have a fever")
    else:
        print("You don't have a fever")
elif temp.upper() == "F":
    theanswer1 = input("Enter your body temprature in Fahrenheit:")
    ta1 = float(theanswer1)
    if ta1 >= 98.6:
        print("You have a fever")
    else:
        print("You don't have a fever")
else:
    print("Please try again")