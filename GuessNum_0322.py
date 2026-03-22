import random
i = random.randint(1,10)
count = 0
while True:
    count += 1
    num = int(input("請輸入數字:"))
    if num == i:
        print("猜對了")
        print(f"這是你猜的第{count}次")
        break
    elif num < i:
        print("你猜得比答案小")
    else :
        print("你猜得比答案大")
    print(f"這是你猜的第{count}次")


