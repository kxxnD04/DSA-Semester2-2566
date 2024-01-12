"""Crate BTSNODE"""
class BSTNode:
    """node for binary tree"""
    def __init__(self, data=int):
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
_TREE = BSTNode(int(input()))
print(_TREE.get_data())
print(_TREE.get_left())
print(_TREE.get_right())
