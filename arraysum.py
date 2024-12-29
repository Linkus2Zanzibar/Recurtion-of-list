def arraysum(a):
    length=len(a)
    if length==1:
        return a[0]
    return a[0] + arraysum(a[1:])
a=[27,132,5976,5437,53789]
print("THe sum of the array is ",arraysum(a))