"""Delete"""
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
        self.root = None
    def get_root(self):
        """to get root node"""
        return self.root
    def set_root(self, root):
        """to set root"""
        self.root = root
    def insert(self, data):
        """to insert data"""
        def insert_node(root: BSTNode, data):
            """to insert but recursive"""
            if root is None:
                return BSTNode(data)
            elif root.get_data() < data:
                root.set_right(insert_node(root.get_right(), data))
            else:
                root.set_left(insert_node(root.get_left(), data))
            return root
        self.set_root(insert_node(self.root, data))
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
        return self.root == None
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
    def delete(self, data):
        """delete node from bst"""
        if self.is_empty():
            print("Delete Error, {} is not found in Binary Search Tree.".format(data))
            return None
        def del_(root, data):
            """for delete"""
            if root is None:
                print("Delete Error, {} is not found in Binary Search Tree.".format(data))
                return None
            if data < root.get_data():
                root.left = del_(root.left, data)
            elif data > root.get_data():
                root.right = del_(root.right, data)
            else:
                if root.left is None and root.right is None: #กรณีเป็น leaf node
                    root = None
                elif root.left is None: #มี right subtree
                    root = root.right
                elif root.right is None: #มี left subtree
                    root = root.left
            return root
        roots = self.root
        self.root = del_(roots, data)
def main():
    """Data Structures and Algorithms Lab  Binary Search Tree"""
    my_bst = BST()
    while 1:
        text = input()
        if text == "Done":
            break
        condition, data = text.split(": ")
        if condition == "I":
            my_bst.insert(int(data))
        elif condition == "D":
            my_bst.delete(int(data))
        else:
            print("Invalid Condition")
    my_bst.traverse()

main()
