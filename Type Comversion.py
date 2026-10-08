int("10")       # string → integer
float("10.5")   # string → float
str(25)         # integer → string
str(3.14)       # float → string

print(int("24")) #print only 24
value = "10"
print(type(value))


##
a = "10"
b = 5
print(int(a) + b)   # 15

##
a = "24"
b = int(a)

print(a) #24
print(type(a)) #<class 'str'>

print(b) #24
print(type(b)) #<class 'int'>


##
x = "10.5"      # x is a string
y = float(x)    # convert to float

print(x) #10.5
print(type(x)) #String
print(y) #10.5
print(type(y)) #float


##
pi = 3.14           # pi is a float
pi_text = str(pi)   # convert to string

print(pi) #3.14
print(type(pi)) #float
print(pi_text) #3.14
print(type(pi_text)) #String