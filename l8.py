# wap to find a given number is armstrong or not   

num = int(input("enter a numbner : "))
m = len(str(num))
temp = num
sum = 0
while(temp > 0):
    last_digit = temp % 10
    sum = last_digit**m + sum
    temp = temp//10
if num == sum:
    print("armstrong")
else:
    print("not armstrong")