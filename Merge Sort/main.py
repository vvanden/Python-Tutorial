def mergesort(msls):

    ls_len=len(msls)

    if ls_len > 1:

        ls_half = int(ls_len / 2)

        ls_s = msls[0:ls_half]
        ls_e = msls[ls_half:ls_len]

        mergesort(ls_s)
        mergesort(ls_e)

        msls_len=len(msls)

        print(msls)

        for idx2 in range(msls_len - 1):
            if idx2 < msls_len:
                if msls[idx2] > msls[idx2 + 1]:
                    ls_hold = msls[idx2 + 1]
                    msls[idx2 + 1] = msls[idx2]
                    msls[idx2] = ls_hold


ls=[33,88,1,22,99,44,11,66,55,77]
#ls=[33,88,1,22,99,44,11,66,55]

ls_sort=ls.copy()

mergesort(ls_sort)

print(ls)
print(ls_sort)