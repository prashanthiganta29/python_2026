
#task 4-->practice variables,comments,datatypes and type function, type conversion
# VARIABLES
name = "PRASHANTHI"
age = 20
height = 5.8
print("name =", name, "age =", age, "height =", height)
#DATATYPES or type function = used to find the datatype of a variable
print(type(name))
print(type(age))
print(type(float)) 
#this is a single line comments used explain code in single line without printing
'''
#this is multi line comment used to explain code in multiple line without printing
'''
#type conversion = changing one data type into another data type 
#manual type coversion by int(),str(),float()(EXPLICIT CONVERSION)
number ="432"
print(type(number))
number=int(number)
print(type(number))
weight=67.17
print(type(weight))
weight=int(weight)
print(type(weight))
#Automatic type conversion by python(IMPLICIT CONVERSION)
num1=10
num2=5.5
result=num1+num2
print(result)
print(type(result))
#QUESTION Create a Python script with both single-line and multi-line comments explaining the purpose of the script.
# THIS IS SINGLE LINE COMMENT.
#The purpose of this script is to demonstrates the use of comments in python
#comments are used to explain the code
'''
this is a multi line comment
1.the purpose of this script is show how the single line and multiline comments are used
2.print a simple to the screen
'''
print("welcome to the pythonlife!!!!!!!")
#QUESTION Declare two variables, one storing an integer and the other a string. Print their values.
rollno = 124
stream = 'AI'
print('rollno =',rollno,'stream =',stream)
#QUESTION Write a program that prints a pattern using multiple print statements.
print("*")
print("***")
print("******")
print("*********")
print("**********")
#QUESTION Create a Python script for a simple task and add comments to explain each step.
#assigning value to a variable
english_marks=90
#assigning value to a variable
telugu_marks=100
#adding marks using arithmetic operator
total_marks=english_marks + telugu_marks
#printing total marks
print(total_marks)
#QUESTION Create variables of different data types(int,float,str) and print their values
int_num=10
float_num=10.99999
str_num="10"
print(int_num,float_num,str_num)
#QUESTION Determine the data type of a variable
print(type(int_num))
print(type(float_num))
print(type(str_num))
#QUESTION Display the memory addresses
print("memory address of int_num=",id(int_num))
print("memory address of float_num=",id(float_num))
print("memory address of str_num=",id(str_num))
#QUESTION Create a program that takes user age = “35”, converts it to an integer, and then prints the result type.
age=45
age=int(age)
print('age=',age)
print("type of age =",type(age))
#QUESTION Concatenate two strings and print the result.
first_name="PRASHANTHI"
last_name="GANTA"
full_name= first_name+' '+last_name
print("MY NAME IS", full_name)



