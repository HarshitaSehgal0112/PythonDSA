# Quick sort program
def Quick_sort(listl1):
    if len(listl1)==0:
        return listl1
    else:
        pivot=listl1[0]
        lesser=[x for x in listl1[1:] if x<=pivot]
        greater=[x for x in listl1[1:] if x>pivot]
        return Quick_sort(lesser)+[pivot]+Quick_sort(greater)
l1=[53,11,72,68,41,25,18,37,44,80]
l1=Quick_sort(l1)
print(l1)