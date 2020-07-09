Inorder Traversal of Binary Tree

https://practice.geeksforgeeks.org/problems/inorder-traversal/1

def InOrder(root):                    #we are getting input as in the form of root
    l1 = []                          #we initialize an array which we need to return
    if root == None:                  #if the root is none then the tree is empty
        return l1                     #then we have to return None
    else:                             #otherwise
        l1 += InOrder(root.left)      #these 3 steps are much important
        l1.append(root.data)          
        l1 += InOrder(root.right)
    return l1                        #return the list
