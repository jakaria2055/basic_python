#BREAK
num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 64)
x = 64
i = 1

while i < len(num):
    if(num[i] == x):
        print("Value found in index", i)
        break
    i += 1





#CONTINUE
i = 0
while i <= 10:
    if(i%2==0):
        i += 1
        continue  #skip
    print(i)
    i += 1