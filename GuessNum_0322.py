import random
i = random.randint(1,10)
while True:
    num = int(input("請輸入數字:"))
    if num == i:
        print("猜對了")
        break
    elif num < i:
        print("你猜得比答案小")
    else :
        print("你猜得比答案大")


