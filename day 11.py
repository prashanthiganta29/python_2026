#Add function
# def sum(a,b):
#     return a*b
# result = sum(7,5)
# print(result)

#Square Function
#def square(x):
 #   return x*x
#result = square(4)
#print(result)

#Factorial Function
# def factorial(n):
#     if n<0:
#         return "factorial is not define"
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# print (factorial(6))   



# #Maximam Function
# def maximum(numbers):
#     if not numbers:
#         return None
#     max_value = numbers[1]
#     for num in numbers:
#         if num > max_value:
#             max_value = num
#     return max_value
# print (maximum([3,4,5,6,7,8]))    


#Reverse Function
def reverse(s):









































#Atm program using functions


as
        else:
            self.balance += amount
            print(f"${amount} credited successfully")

    def debit(self):

        amount = float(input("Enter amount to debit: "))

        if amount <= 0:
            print("Please enter positive amount")

        elif amount > self.balance:
            print("Insufficient balance")

        else:
            self.balance -= amount
            print(f"${amount} debited successfully")
s ATM:
    def __init__(self,balance):
        self.balance = balance


    def display_menu(self):
        print("\nATM Menu:")
        print("1. Credit")
        print("2. Debit")
        print("3. Balance")
        print("4. Exit")

    def show_balance(self):
        print(f"Your current balance is: ${self.balance}")


class Transaction(ATM):

    def credit(self):

        amount = float(input("Enter amount to credit: "))

        if amount <= 0:
            print("Please enter positive amount")


class User(Transaction):

    def run(self):

        while True:

            self.display_menu()

            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                self.credit()

            elif choice == '2':
                self.debit()

            elif choice == '3':
                self.show_balance()

            elif choice == '4':
                print("Thank you for using ATM")
                break

            else:
                print("Invalid choice")


obj = User(50000)
obj.run()





