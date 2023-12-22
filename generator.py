# Generator function that produce a sequence of number

def generator(n):
    count = 0
    while count < n:
        yield count
        count += 1
for count in generator(5):
    print(count)
    
# USE PYTHON GENERATOR EXPRESSION

number = (i for i in range(1, 10))
for i in number:
    print(i)
    
# Square of a no. using range function & generator expression

square_no = (i*i for i in range(1, 10))
for i in square_no:
    print(i)

# calculate power of two

pow_two = (2**n for n in range(0, 10))
for n in pow_two:
    print(n)
    
# OR
def pow_two_gen(max = 0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1
sq = pow_two_gen(5)
for i in sq:
    print(i)