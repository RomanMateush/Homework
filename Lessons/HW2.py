alist=[10, 0,3,10,90,5,-2,4,18,45,707, 100,1,-266,706, 1]
largest = alist[0]
second_largest = alist[0]
for i in range(len(alist)):
    if alist[i] > second_largest:
        second_largest = alist[i]
    if alist[i] > largest:
        tmp = second_largest
        second_largest = largest
        largest = tmp      

print(largest, second_largest)