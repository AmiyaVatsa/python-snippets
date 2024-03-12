# txt = "We are the so called \'vikings\' from the north"
# print(txt)
# print(txt.capitalize())
# print(txt.casefold())
# print(txt.center(100, '%')) # increases the total length of string to this length and adds padding around the string
# print(txt.index('the'))
# print(txt.isalnum())
# print(txt.isalpha())
# print(txt.isascii())

# s = "geeks for geeks"
# print(s.center(24))

# x = input()
# print(x.isnumeric())

# print(bool("Hello"))
# print(bool(15))
# print(bool("Abc"))

x = 200.567779
print(isinstance(x, float))


'''
List is a collection of elements which is ordered and changable. Allows duplicate members.
Tuple is a collection of elements which is ordered and not changable. Allows duplicate numbers
Set is unordered, unchangable, not indexed, not duplicate 
Dictionary is ordered, changable and allows no duplicate keys
'''

mylist = ["cherry", "orange", "mango"]
print(mylist)
print(len(mylist))
mylist = [34, "asgga"]
print(mylist)
list2 = [True, False]
print(type(list2))
a = list(('apple', 'orange'))
print(a, type(a))
print(mylist[0:2])
