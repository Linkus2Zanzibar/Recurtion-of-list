def checksort(a):
    length=len(a)
    if length==1 or length==0:
        return True
    return a[0]<=a[1] and checksort(a[1:])
a=[10,20,30,40,50,60,70,80,90,100]
if checksort(a):
    print(" The given array IS sorted ")
else:
    print(" The array is NOT sorted ")