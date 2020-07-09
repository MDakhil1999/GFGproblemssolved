#Postorder Traversal of Binary Tree

#https://practice.geeksforgeeks.org/problems/postorder-traversal/1

def postOrder(root):
    l1 = []
    if root == None:
        return 
    else:
        if root.left:
            l1 += postOrder(root.left)
        if root.right:
            l1 += postOrder(root.right)
        l1.append(root.data)
    return l1
