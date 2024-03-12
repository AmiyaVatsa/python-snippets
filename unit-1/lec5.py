list1 = ["flower", "animal", "ocean"]
print(list1[0:3])

thislist = ["lucknow", "delhi", "kolkata"]
if "lucknow" in thislist:
    print(True)
else:
    print(False)
thislist[1] = "raipur"
print(thislist)
fruits = "guava", "apple", "banana" # tuple declaration
#immutable

thislist[1:2] = ["mumbai", "pune"]
print(thislist)

thislist.insert(1, "Kozhikode")
print(thislist)

thislist.append("jalandhar")
print(thislist)

thislist.extend("jammu")
print(thislist)


tuple1 = ("Orange", "Grapes")
list1 = ["apple", "banana"]
list1.extend(tuple1)
print(list1)

list2 = ["apple", "banana", "cherry", "banana"]
list2.remove("banana")
print(list2)

list2.pop()
print(list2)
list2.pop(1)
print(list2)
del list2

for z in thislist:
    print(z)

newlist = []
for z in thislist:
    if "a" in z:
        newlist.append(z)
print(newlist)


newlist = [x for x in thislist if "a" in x]
print(newlist)


