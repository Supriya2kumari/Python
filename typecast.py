#implicit type conversion
a = 10
b = 20.5
print(a+b)

#explicit conversion (float to int)
b = int(b)
print(a+b)

# convert string to int using int() function
a = 20
b = "30"
b = int(b)
print(a+b)

# convert int to string using str() function
a = 20
b = "30"
a = str(a)
print(a+b)

#convert float to string
a = 10.3
b = "20"
a = str(a)
print(a+b)

# convert string to float
a = 10.3
b = "20"
b = float(b)
print(a+b)

#convert int to boolean using bool()
a = 10
b = True
print(a+b)  # 11
a = bool(a)
print(a+b)  # 2

#explicit convertion of bool to int (conversion of bool to int is implicit)
a = 10
b = True
b = int(b)
print(a+b)  

#convert bool to float (it is implicit converstion)
a = 10.5
b = False
print(a+b)

#convert float to bool
a = 10.5
b = False
a = bool(a)
print(a+b)

# int to list
a = 12
# a = str(a)
# a = list (a)
a = list(str(a))
print(a)

# float to list
a = 10.5
a = list(str(a))
print(a)

# string to list
a = "radhe"
a = list(a)
print(a)

# bool to list
a = True
a = list(str(int(a)))
print(a)

# int to tuple
a = 10
a = tuple(str(a))
print(a)

# float to tuple
a = 10.5
a = tuple(str(a))
print(a)

# string to tuple
a ="supriya"
a = tuple(a) 
print(a)

#bool to tuple
a = True
a = tuple(str(int(a)))
print(a)

#list to tuple
a = [1,2,3]
a = tuple(a)
print(a)

# int to set
a = 10
a = set(str(a))
print(a) 

# float to set
a = 10.5
a = set(str(a))
print(a)

# string to set
a ="supriya"
a = set(a) 
print(a)

#bool to set
a = True
a = set(str(int(a)))
print(a)

#list to set
a = [1,2,3]
a = set(a)
print(a) 

#tuple to set
a = (4,5,6)
a = set(a)
print(a)

