# SYNTAX OF ITERATOR
list = [4,7,2,8,5]
iterator = iter(list)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

# USE FOR LOOP WITH ITERATOR
list = [4, 7, 6, 2]
iterator = iter(list)
for element in iterator:
    print(element)
    
# BUILDING CUSTOME ITERATOR 
   # Give next power of two, start from Zero to User define number

class PowTwo:
    def __init__(self, max):
        self.max = max
    def __iter__(self):
        self.n = 0
        return self
    def __next__(self):
        if self.n < self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration
no = PowTwo(5)
iterator = iter(no)
for i in iterator:
    print(i)
# we can also use the given below instead of above 4 lines

# for elemt in PowTwo(5):
#     print(elemt)

# INFINITE ITERATOR