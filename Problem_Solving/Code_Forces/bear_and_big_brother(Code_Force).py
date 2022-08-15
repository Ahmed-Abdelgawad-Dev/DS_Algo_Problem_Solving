def bear_and_big_brother(a: int = 4, b: int = 9) -> int:
    a, b = map(int, input().split(" "))
    years = 0
    while 1 <= a <= b <= 10:
        for i in range(10):
            a *= 3
            b *= 2
            years += 1
            if a > b:
                break
        return(years)


x = bear_and_big_brother()
print(x)
