# wap to print 1 to 100 and then print odd even in the front of the numbers 
# 1- odd 
# 2- even
# 3- odd
# 4- even
# ...........
for i in range (1,101):
    if i % 2 == 0:
       print(f'{i} - even')
    else:
       print(f'{i} - odd')
     

