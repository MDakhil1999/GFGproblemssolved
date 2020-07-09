#Preorder Traversal of Binary Tree

#https://practice.geeksforgeeks.org/problems/preorder-traversal/1

def preorder(root):
    l1 = []
    
    if root == None:
        return l1
    else:
        l1.append(root.data)
        if root.left:
            l1 += preorder(root.left)
        if root.right:
            l1 += preorder(root.right)
    return l1
