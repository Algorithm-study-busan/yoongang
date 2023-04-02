def f():
    global a
    return a + 1

a = 1
f()
print(a)