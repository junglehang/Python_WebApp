flist = []
for i in range(3):
    def foo(x):
        print(x + i)
    flist.append(foo)

for f in flist:
    f(2)