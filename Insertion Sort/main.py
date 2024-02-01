def insertionsort(arr):

    if len(arr) == 1:
        return

    i = 1

    while i < len(arr):
        if arr[i] < arr[i-1]:
            hold = arr.pop(i)
            j = i-1
            if j == 0:
                arr.insert(j, hold)
            elif arr[j] > hold:
                arr.insert(j, hold)
                i -= 1
        else:
            i+=1

ls=[3,8,1,2,9,4,10,6,5,7]

ls_sort=ls.copy()
insertionsort(ls_sort)

print("orig list:", ls)
print("sort list:", ls_sort)