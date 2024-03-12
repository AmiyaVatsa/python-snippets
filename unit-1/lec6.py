def f(n):
    return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = f) #conditional sort
print(thislist)