# Merge sort program
def merge_sort(listl1):
    if len(listl1)>1:
        mid=len(listl1)//2
        leftlist=listl1[:mid]
        rightlist=listl1[mid:]

        merge_sort(leftlist)
        merge_sort(rightlist)

        i=j=k=0
        while i<len(leftlist) and j<len(rightlist):
            if leftlist[i]<rightlist[j]:
                listl1[k]=leftlist[i]
                i+=1
            else:
                listl1[k]=rightlist[j]
                j+=1
            k+=1
        while i<len(leftlist):
            listl1[k]=leftlist[i]
            i+=1
            k+=1
        while j<len(rightlist):
            listl1[k]=rightlist[j]
            j+=1
            k+=1
l1=[78,23,48,12,8,27,18,28]
merge_sort(l1)
print(l1)
