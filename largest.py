def largest(a):
    length=len(a)
    if length==1:
        return a[0]
    return max(a[0],largest(a[1:]))
a=[1087,456789,123456789]
print(" The largest element is ", largest(a))