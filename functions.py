def circle_area(radius):
    pi = 3.14159
    area = pi * radius ** 2
    return area



def calculate_tax(money, tax):
    total_due = money + (money * tax)
    return total_due



def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5 / 9)
    return celsius



radius = float(input("Enter radius: "))
area = circle_area(radius)
print(f"{area:.2f}")


money = float(input("Enter money: "))
tax = float(input("Enter tax rate: "))
total = calculate_tax(money, tax)
print(f"{total:.2f}")


fahrenheit = float(input("Enter Fahrenheit temperature: "))
celsius = fahrenheit_to_celsius(fahrenheit)
print(celsius)