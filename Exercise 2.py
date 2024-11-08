#Question 1: Arithmetic and Assignment Operators

# TODO: Add 3 to x using the += operator
x1 = 17
x1 += 3

# TODO: Multiply y by 2 using the *= operator
y1 = 5
y1 *= 2

# TODO: Divide x by y and store the result in a variable called 'result'
result = x1/y1
# TODO: Print the value of 'result'
print(f"The result of dividing x and y would be: {result} ")
#----------------------------------------------------------------------------------------------
# # # Question 2: Comparison and Logical Operators

# # # TODO: Create a condition that checks if a is greater than b
a = 10
b = 5
c = 12
if a > b:
    print("true")
else: 
    print("false")
# TODO: Create a condition that checks if b is even (hint: use the modulus operator)
if b % 2:
    print("true")
else:
    print("false")
# TODO: Create a condition that checks if c is less than or equal to a
if c <= a:
    print("true")
else:
    print("false")
# TODO: Combine the above conditions using logical operators to create a 'final_condition'
#       The 'final_condition' should be True if either:
#    -  a is greater than b, or
#    - b is even and c is less than or equal to a
if a >= b and c <= a:
   
# # TODO: Print the value of 'final_condition'
    print("The final condition is true")
else:
    print("The final condition is not true")
# # #------------------------------------------------------------------------------------
# # # Question 3: Conditional Statements

# # # TODO: Ask the user to input a test score (0-100) and store it in a variable called 'score'
score = int(input("Kindly input your test score: "))

# TODO: Implement a grading system using if-elif-else statements:
#       90-100: A
#       80-89: B
#      70-79: C
#      60-69: D
#       Below 60: F
if score >= 90 or  score <=100:
    print("You got an A for your test score")
elif score >= 80:
   print("You got B for your test score")
elif score >= 70:
    print("You got C for your test score")
elif score >= 60:
    print("You a D for your test score")
else:
    print("You got an F for your test score")
# # # TODO: Print the grade for the given score

# #------------------------------------------------------------------------------------
# # Question 4: Combining Operators and Conditionals

# TODO: Ask the user to input two numbers and store them in variables 'num1' and 'num2'
num1 = int(input("Please input any number: "))
num2 = int(input("Please input another number: "))

# TODO: Ask the user to input an operation (+, -, *, /) and store it in a variable called 'operation'

# TODO: Use conditional statements to perform the chosen operation on num1 and num2
operation = input("Please input any of the following operation + , - , * , / : ")
output = 0
if operation == "+":
    output = num1 + num2
    print(output)
elif operation == "-":
    output = num1 - num2
    print(output)
elif operation == "*":
    output = num1 * num2
    print(output)
elif operation == "/":
    output = num1 / num2
    print(output)
    
# TODO: Handle the case of division by zero


# TODO: Print the result of the operation
