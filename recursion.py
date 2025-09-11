def rec(i):
    if i == 0:
        return
    print(i)
    rec(i-1)

rec(10)