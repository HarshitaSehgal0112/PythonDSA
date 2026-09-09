# modified bubble sort program
def modified_bubble_sort(data_list):
    flag=False
    for r in range(1,len(data_list)):
        flag=False
        for i in range(len(data_list)-1):
            if data_list[i]>data_list[i+1]:
                data_list[i],data_list[i+1]=data_list[i+1],data_list[i]
                flag=True
        if not flag:
            break
list=[38,56,23,50,67,12]
modified_bubble_sort(list)
print(list)

