# selection sort program
def selection_sort(data_list):
    for i in range(len(data_list)):
        min_index=i
        for j in range(i+1,len(data_list)):
            if data_list[j] < data_list[min_index]:
                min_index=j
        data_list[i],data_list[min_index]=data_list[min_index],data_list[i]
l1=[64,35,89,21,72,13]
selection_sort(l1)
print(l1)



