'''
    This solution taking function in the tree itslef instead in the node
'''
class Node :
    def __init__(self,data) :
        self.data = data
        self.left = None
        self.right = None

class Tree :
    def __init__(self) :
        self.root = None

    def insert(self,data) :
        if self.root is None :
            self.root = Node(data)
            return
        self._insert(data,self.root)

    def _insert(self,data,cur) :
        if cur.data > data :
            if cur.left is None :
                cur.left = Node(data)
            else :
                self._insert(data,cur.left)
        else :
            if cur.right is None :
                cur.right = Node(data)
            else :
                self._insert(data,cur.right)

    def preorder(self) :
        self._preorder(self.root)

    def _preorder(self,cur) :
        print(cur.data)
        if cur.left :
            self._preorder(cur.left)
        if cur.right :
            self._preorder(cur.right)

    def postorder(self) :
        self._postorder(self.root)

    def _postorder(self,cur) :
        if cur.left :
            self._postorder(cur.left)
        if cur.right :
            self._postorder(cur.right)
        print(cur.data)

    def inorder(self) :
        self._inorder(self.root)

    def _inorder(self,cur) :
        if cur.left :
            self._inorder(cur.left)
        print(cur.data)
        if cur.right :
            self._inorder(cur.right)
        
bst = Tree()    
bst.insert(1)
bst.insert(2)
bst.insert(3)
bst.insert(2)
bst.insert(-1)
#bst.preorder()
#bst.postorder()
bst.inorder()
