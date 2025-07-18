number1 = int(input("Enter your first number: -> ")) # "int" points at intiger and "input" -> takes input
number2 = int(input ("Pleae enter your second number: -> "))
addition = int(number1 + number2)
multiply = int(number1 * number2)
devision = float(number1 / number2) # "float" point at floating point division.
subtruction =  int(number1 - number2) 

# Now lets print the result of this calculation using "print" statement.
print ("The result of addition is", addition) #to print the result.
print ("The result of multiplication is", multiply,"\n")

#lets look at more efficient way to print all the result together
print ("The result of addition, multiplication, devision and subtruction is as follows")
print (f"Addition {addition}, \nMultiplication {multiply}, \nDevision {devision}, \nSubtruction {subtruction}")