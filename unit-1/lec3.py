'''
text type -> str
numeric -> int, float, complex
sequence -> list, tuple, range
mapping -> dict
set type -> set, frozenset
boolean type -> bool
binary type -> bytes, bytearray, memoryview
None type : None
'''

x = "amiya" 
x = 20.5
x = 20e5
x = 20E5
x = 2 + 4j

l = ["cat", "dog", "horse"] # list
t = ("cat", "dog", "horse") # tuple
x = range(6)
#print(range(0,6))

'''
random
randrange(l, r) returns number from l to r - 1
'''

# import random
# print(random.randrange(1,10))
# y = int(3.9)
# print(y)

# t = float("3")
# print(t)

# strings are simply array of characters
a = "hello world"
# print(a[1])
#for x in "banana": # for loop
#    print(x)

#print(len(a))

# text = "the best things in life are free"
# if "free" in text:
#     print(True) # does in use binary search?
# else:
#     print(False)
# if "expensive" not in text:
#     print("expensive not in text")
# else:
#     print(False)
# string slicing

# print(a[0:7])
# print(a[:9])
# print(a[0:])
# print(a[-1 : -12 : -1])
# print(a.upper(), a.lower())
# b = " hello world "
# print(b.strip())
# print(b.replace('h', 'j'))
# a = b.replace('h', 'j') # strings are immutable
# print(a)
# a = "Hello, world!"
# print(a.split(","))
# z = a + " " + b
# print(z)

# age = 36
# txt = "My name is John and I am {}"
# print(txt.format(age))
# print(txt[:len(txt)])
# p = "My name is Khan"
# print(p[11:len(p)])

# str = "morning"
# print(str.endswith("ing"))
# print(str.capitalize())
# print(str.find('n'))
# print(str.count("n"))
