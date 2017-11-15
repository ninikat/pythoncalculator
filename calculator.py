import operands as op

input_one = int(raw_input("Enter your first number: "))
input_two = raw_input("Enter one of the following:  +, -, *, / ")
input_three = int(raw_input("Enter your second number: "))    
    
if input_two == "+":
    addition = op.add(input_one,input_three)
    print("Your result is: " + str(addition))
elif input_two == "-": 
    subtraction = op.subtract(input_one,input_three)
    print("Your result is: " + str(subtraction))
elif input_two == "*": 
    multiplication = op.multiply(input_one,input_three)
    print("Your result is: " + str(multiplication))
elif input_two == "/": 
    division = op.divide(input_one,input_three)
    print("Your result is: " + str(division))






