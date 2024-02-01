def mergesort(msls):

    if len(msls) > 1:  

        ls_left = msls[:len(msls)//2]
        ls_right = msls[len(msls)//2:]

        #recursion
        mergesort(ls_left)
        mergesort(ls_right)

        L_idx = 0 #leftmost element of LEFT arrary index
        R_idx = 0 #leftmost element of RIGHT arrary index
        M_idx = 0 #merged array index

        #merge, compare left to right array and push lowest values into merged array
        while L_idx < len(ls_left) and R_idx < len(ls_right):
            #left array is lower, push in merged array
            if ls_left[L_idx] < ls_right[R_idx]:
                msls[M_idx] = ls_left[L_idx]
                L_idx += 1
                M_idx += 1

            else:
            #right array is lower, push in merged array
                msls[M_idx] = ls_right[R_idx]
                R_idx += 1
                M_idx += 1

        #nothing left to compare, place remaining left array items into the merged array
        while L_idx < len(ls_left):
            msls[M_idx] = ls_left[L_idx]
            L_idx += 1
            M_idx += 1
        
        #nothing left to compare, place remaining right array items into the merged array
        while R_idx < len(ls_right):
            msls[M_idx] = ls_right[R_idx]
            R_idx += 1
            M_idx += 1

ls=[33,88,1,22,99,44,11,66,55,77]

ls_sort=ls.copy()
mergesort(ls_sort)

print("orig list:", ls)
print("sort list:", ls_sort)