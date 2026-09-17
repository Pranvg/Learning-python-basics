def calculator(a, b, operation):
    if operation == '+':
        return a + b 
    
    elif operation == '-':
        return a - b
    

    elif operaion == '*':
        return a * b
    
    elif operation == '/':

        if b == 0:
            return "error: you cannot divide by zero!"
        
        return a / b
    
    else:
        return "invalid statement"
    

print("Welcome to the simple calculator!")


num1 = float(input("Enter a number: "))

operator = input("Enter a operator(+, -, /, *): ")

num2 = float(input("Enter the second number: "))

result = calculator(num1, num2, operator)
print("The answer is:", result)











class OnlineStore:

    total_products = 0


    def __init__(self, name, price):
        self.name = name 
        self.price = price

        OnlineStore.total_products += 1 
    def get_info(self):
        print(f"the product {self.name} has a price is {self.price} ")

    @staticmethod
    def calc_discount(price, discount):
        final_price = price- price * discount / 100

        print(f"the final price after discount = {final_price}")


p1 = OnlineStore("Laptop", 67_000)
p2 = OnlineStore("Iphone", 50_000)

p1.get_info()

p2.calc_discount(50_000, 5)

print(f"total products that created or added in our online store is: {OnlineStore.total_products}")



