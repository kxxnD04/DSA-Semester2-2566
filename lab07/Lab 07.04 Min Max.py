"""Min Max"""
class BSTNode:
    """node for binary tree"""
    def __init__(self, data=None):
        """init"""
        self.data = data
        self.left = None
        self.right = None
    def get_data(self):
        """get data node"""
        return self.data
    def set_data(self, data):
        """to set data"""
        self.data = data
    def get_left(self):
        """return left node"""
        return self.left
    def set_left(self, left):
        """to set left node"""
        self.left = left
    def get_right(self):
        """to get right node"""
        return self.right
    def set_right(self, right):
        """to set right"""
        self.right = right

class BST:
    """BST"""
    def __init__(self):
        """init"""
        self.root = BSTNode()
    def get_root(self):
        """to get root node"""
        return self.root
    def set_root(self, root):
        """to set root"""
        self.root = root
    def insert(self, data):
        """to insert data"""
        current = self.root
        if current.get_data() is None:
            self.set_root(BSTNode(data))
            return
        while True:
            if data < current.get_data():
                if current.get_left() is None:
                    current.set_left(BSTNode(data))
                    break
                current = current.left
            else:
                if current.get_right() is None:
                    current.set_right(BSTNode(data))
                    break
                current = current.right
    def preorder(self):
        """traverse by preorder"""
        current = self.root
        def pre(node):
            """DRY"""
            if node:
                print("-> " + str(node.get_data()) + " ", end='')
                pre(node.get_left())
                pre(node.get_right())
        pre(current)
        print()
    def inorder(self):
        """Inorder"""
        current = self.root
        def inor(node):
            """SO DRY"""
            if node:
                inor(node.get_left())
                print("-> " + str(node.get_data()) + " ", end='')
                inor(node.get_right())
        inor(current)
        print()
    def postorder(self):
        """post"""
        current = self.root
        def post(node):
            """FKING DRY"""
            if node:
                post(node.get_left())
                post(node.get_right())
                print("-> " + str(node.get_data()) + " ", end='')
        post(current)
        print()
    def is_empty(self):
        """check the BST"""
        return self.root.get_data() == None
    def traverse(self):
        """traverse into tree"""
        if self.is_empty():
            return print("This is an empty binary search tree.")
        print('Preorder: ', end='')
        self.preorder()
        print('Inorder: ', end='')
        self.inorder()
        print('Postorder: ', end='')
        self.postorder()
    def find_min(self):
        """find min"""
        current = self.root
        if self.is_empty():
            return None
        else:
            while current.left:
                current = current.left
            return current.get_data()
    def find_max(self):
        """find max"""
        current = self.root
        if self.is_empty():
            return None
        else:
            while current.right:
                current = current.right
            return current.get_data()

def main():
    """Data Structures and Algorithms Lab  Binary Search Tree"""
    my_bst = BST()
    for _ in range(int(input())):
        my_bst.insert(int(input()))
    my_bst.traverse()
    print("Max:", my_bst.find_max())
    print("Min:", my_bst.find_min())

main()
