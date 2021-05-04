# Shalommita
# 71200640
# LAB-11-TUPLE

def tuplee(bil):
    lst=list(bil)
    cnt=1
    for i in lst:
        cnt*=i
    return cnt

def tuplee2(bil):
    lst=list(bil)
    count=0
    for x in lst:
        count+=x
    return count

bil=(2,9,3,2)
print(type(bil))
print(tuplee(bil))
print(tuplee2(bil))