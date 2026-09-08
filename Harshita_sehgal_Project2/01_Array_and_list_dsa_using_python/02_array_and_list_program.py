# given a list of heterogenous elements. write a python script to remove all the non int values from the list

l1=[10,4.6,'abc',True,45,50,20+5j]
print("after removing all the non int values from the given list")
l1.remove(True)
l1.remove(4.6)
l1.remove('abc')
l1.remove(20+5j)
print(l1)