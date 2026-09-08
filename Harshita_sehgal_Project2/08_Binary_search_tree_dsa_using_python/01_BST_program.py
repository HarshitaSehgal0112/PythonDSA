# BST part-1
"""
1 define a class node with instance variables left,right and item. The variables left
  and right are used to refer left and right child node. The item variable is used to
  hold data item.
2 define a class BST to implement binary search tree data structure. make __init__()
  method to create root instance variable to hold the reference of root node.
3 In class BST, define insert method to store new data item in the binary search tree.
4 In class BST, define a search method to find a given item in the binary search tree
  and return the node reference. It returns node if search failed.
5 In class BST, define a method to implement inorder traversal.
6 In class BST, define a method to implement preorder traversal.
7 In class BST, define a method to implement postorder traversal.
"""
class Node:
    def __init__(self,item):
        self.left=None
        self.item=item
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def insert(self,data):
        self.root=self.rinsert(self.root,data)
    def rinsert(self,root,data):
        if root is None:
            return Node(data)
        elif root.item>data:
            root.left=self.rinsert(root.left,data)
        elif root.item<data:
            root.right=self.rinsert(root.right,data)
        return root
    def search(self,data):
        return self.rsearch(self.root,data)
    def rsearch(self,root,data):
        if root is None:
            return None
        if root.item==data:
            return root
        elif root.item<data:
            return self.rsearch(root.right,data)
        elif root.item>data:
            return self.rsearch(root.left,data)
        else:
            return root
    def inorder(self):
        result=[]
        self.rinorder(self.root,result)
        return result
    def rinorder(self,root,result):
        if root:
            self.rinorder(root.left,result)
            result.append(root.item)
            self.rinorder(root.right,result)
    def preorder(self):
        result=[]
        self.rpreorder(self.root,result)
        return result
    def rpreorder(self,root,result):
        if root:
            result.append(root.item)
            self.rpreorder(root.left,result)
            self.rpreorder(root.right,result)
    def postorder(self):
        result=[]
        self.rpostorder(self.root,result)
        return result
    def rpostorder(self,root,result):
        if root:
            self.rpostorder(root.left,result)
            self.rpostorder(root.right,result)
            result.append(root.item)
b1=BST()
print(b1.insert(50))
print(b1.insert(30))
print(b1.insert(70))
print(b1.insert(20))
print(b1.insert(40))
print(b1.insert(60))
print(b1.insert(80))
print("Inorder traversal:",b1.inorder())
print("preorder traversal:",b1.preorder())
print("postorder traversal:",b1.postorder())
x=b1.search(40)
if x:
    print("40 found")
else:
    print("40 not found")













