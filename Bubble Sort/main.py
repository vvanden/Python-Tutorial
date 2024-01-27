ls=[33,88,1,22,99,44,11,66,55,77]
ls_sort=ls.copy()

ls_len=len(ls_sort)

for idx1 in range(ls_len - 1):
    for idx2 in range(ls_len - 1):
        if idx2 < ls_len:
            if ls_sort[idx2] > ls_sort[idx2 + 1]:
                ls_hold = ls_sort[idx2 + 1]
                ls_sort[idx2 + 1] = ls_sort[idx2]
                ls_sort[idx2] = ls_hold
        
print("orig list:", ls)
print("sort list:", ls_sort)