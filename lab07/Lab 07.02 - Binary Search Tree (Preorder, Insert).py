"""preorder, insert"""
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
        def pre(node: BSTNode):
            """___"""
            if node:
                print("-> " + str(node.get_data()) + " ", end='')
                pre(node.get_left())
                pre(node.get_right())
        pre(current)
        print()

def main():
    """Data Structures and Algorithms Lab  Binary Search Tree"""
    my_bst = BST()
    for _ in range(int(input())):
        my_bst.insert(int(input()))
    print("Preorder: ", end="")
    my_bst.preorder()

main()
