'''
   0
 1   0
   1   0
 1   1

should return 5
'''

class Node :
    def __init__(self,data) :
        self.data = data
        self.left = None
        self.right = None

def unival(root,ctr = 0 ):
    if root :
        if root.left is None and root.right is None :
            ctr += 1
        elif root.data == root.left.data and root.data == root.right.data:
            ctr +=1
        else :
            ctr += 0
        left = unival(root.left)
        right = unival(root.right)
        return ctr + left + right
    return ctr 
    
node1 = Node(0)
node2 = Node(1)
node3 = Node(0)
node4 = Node(1)
node5 = Node(0)
node6,node7 = Node(1),Node(1)

node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5
node4.left = node6
node4.right = node7

print(unival(node1))

