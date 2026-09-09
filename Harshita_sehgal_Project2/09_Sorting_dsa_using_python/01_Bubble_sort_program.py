# Bubble sort program
def bubble_sort(data_list):
    for r in range(1,len(data_list)):
        for i in range(len(data_list)-1):
            if data_list[i]>data_list[i+1]:
                data_list[i],data_list[i+1]=data_list[i+1],data_list[i]
list=[24,58,11,67,92,43]
bubble_sort(list)
print(list)

