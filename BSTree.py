class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BSTree:
    def __init__(self):
        self.root = None
    def __contains__(self,data):
        iterNode = self.root
        while iterNode:
            if iterNode.data == data:
                return True
            elif iterNode.data > data:
                iterNode = iterNode.left
            else:
                iterNode = iterNode.right
        return False
    
    def inorder(self):
        def _inorder(node):
            if node is not None:
                _inorder(node.left)
                res.append(node.data)
                _inorder(node.right)
        res = []
        _inorder(self.root)
        return res

    def insert(self,data):
        self.root = self._insert(self.root,data)
    def _insert(self,node,data):
        if node is None:
            return Node(data)
        if node.data < data:
            node.right = self._insert(node.right,data)
        else:
            node.left = self._insert(node.left,data)
        return node
    def find_most_left(self,node):
        while node.right:
            node = node.right
        return node
    def delete(self,data):
        self._delete(self.root,data)
    def _delete(self,node,data):
        if not node:
            return None
        if node.data < data:
            node.right = self._delete(node.right,data)
        elif node.data > data:
            node.left = self._delete(node.left,data)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                most_left = self.find_most_left(node.right)
                node.data = most_left.data
                node.right = self._delete(node.right, most_left.data)
        return node
        
    def search(self,data):
        def _search(node,data):
            if node is None:
                return None
            elif node.data == data:
                return data
            elif node.data > data:
                return _search(node.left,data)
            else:
                return _search(node.right,data)
        return _search(self.root,data)
