print("10", "05", "2025", sep="-")
print("2025", "05", "2025", sep="/")

print("Name\tAge\tCity")
print("Ali\t25\tDhaka")

#### Number Formatting (int and float)
#a) Integer Formatting**
num = 7
print(f"{num:03d}") #007

#b) Float Formatting**
pi = 3.1415926
print(f"{pi:.2f}") #3.14

#c) Both together**
price = 45.6789
quantity = 3
print(f"Quantity: {quantity:02d}, Price: {price:.2f}") #03,45.68


#### Printing same thing using multple ways
name = "Shehab"
age = 26

print("Name:", name, "Age:", age) #Name: Shehab Age: 26
print(f"Name: {name} Age: {age}") #Name: Shehab Age: 26

print("10", "07", "2025", sep="-") #10-07-2025
print("10-07-2025") #10-07-2025

a = 10
b = 20
c = 30
print(a, "|", b, "|", c)
print(a, b, c, sep=" | ")
print(f"{a} | {b} | {c}")


###Output:
#10 | 20 | 30
#10 | 20 | 30
#10 | 20 | 30
