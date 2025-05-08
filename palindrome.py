l1 = [1, 2, 3]
l2 = [1, 3, 1]

copy_l2 = l2.copy()
copy_l2.reverse()

copy_l1 = l1.copy()
copy_l1.reverse()

if(l2 == copy_l2):
    print("list 2 This is palindrome")
else:
    print(" list 2  This is palindrome")



if(l1 == copy_l1):
    print("list 1 This is palindrome")
else:
    print(" list 1  This is not palindrome")