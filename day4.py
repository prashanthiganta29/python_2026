'''Exercise:
Create a program that takes user input for their name and age. Use formatted strings (f-strings) to print a message
 welcoming the user andstating their age.'''
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Welcome {name}! You are {age} years old.")
'''Create a list called numbers that contains integers from 1 to 10.Check if the number 5 is in the list.
Check if the number 15 is not in the list.
'''
list=[1,2,3,4,5,6,7,8,9,10]
print(5 in list)
print(15 not in list)
'''Write a Python program to calculate the area of a rectangle using the given
formula: area = length * width . Take the values of length and width as inputs from
the user.'''
length=int(input('enter length:'))
width=int(input("enter width:"))
area=length*width
print("Area is ",area)
'''Write a Python program to demonstrate incrementing and decrementing a variable'''
number=10 
print("number before increment is",number)
number+=1
print("number after increment is",number)
number-=1
print("number after decrement is",number)
'''Write a Python program to convert temperature from Celsius to Fahrenheit. The
formula for conversion is: F = (C * 9/5) + 32 . Take the temperature in Celsius as input from the user'''
celsius=float(input("enter temperature in celsius:"))
fahrenheit=((celsius*9/5)+32)
print("temperature in farenheit",fahrenheit)
'''
Write a Python program to calculate the simple interest given the principal
amount, rate, and time (in years).'''
principal=100
rate=40
time=2
simple_interest=principal*rate*time
print(f" principal is {principal},rate is {rate} ,time is {time},simple interest is {simple_interest}")
'''
Write a Python program to concatenate two strings and display the result. The
strings should be taken as input from the user.'''
object=input("object is ")
colour=input("colour is ")
print("object is ",object,"and in colour of",colour)
'''
Write a Python program to convert a distance from kilometers to miles.'''
distance=float(input("enter distance in km:"))
distance=distance*0.621
print("distance is miles is ",distance)