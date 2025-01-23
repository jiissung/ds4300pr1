from typing import List, Optional, Any

from indexer.trees.bst_index import BinarySearchTreeIndex
from indexer.trees.avl_node import AVLNode

class AVLTreeIndex(BinarySearchTreeIndex):
    """
    An AVL Tree implementation of an index that maps a key to a list of values.
    AVLTreeIndex inherits from BinarySearchTreeIndex meaning it automatically
    contains all the data and functionality of BinarySearchTree.  Any
    functions below that have the same name and param list as one in 
    BinarySearchTreeIndex overrides (replaces) the BSTIndex functionality. 

    Methods:
        insert(key: Any, value: Any) -> None:
            Inserts a new node with key and value into the AVL Tree
    """
    
    def __init(self):
       super().__init__()
       self.root: Optional[AVLNode] = None 
    
    def _height(self, node: Optional[AVLNode]) -> int:
        """
        Calculate the height of the given AVLNode.

        Parameters:
        - node: The AVLNode for which to calculate the height.

        Returns:
        - int: The height of the AVLNode. If the node is None, returns 0.
        """
        
        # TODO: make sure to update height appropriately in the
        # recursive insert function.
        
        if not node:
            return 0
        return node.height

    def _rotate_right(self, y: AVLNode) -> AVLNode:
        """
        Performs a right rotation on the AVL tree.

        Args:
            y (AVLNode): The node to be rotated.

        Returns:
            AVLNode: The new root of the rotated subtree.
        """
        
        # TODO: implement the right rotation for AVL Tree
        a = y.left
        t3 = a.right

        a.right = y
        y.left = t3

        y.height = 1 + max(self._height(y.left), self._height(y.right))
        a.height = 1 + max(self._height(a.left), self._height(a.right))

        return a

    def _rotate_left(self, x: AVLNode) -> AVLNode:
        """
        Rotate the given node `x` to the left.
        Args:
            x (AVLNode): The node to be rotated.
        Returns:
            AVLNode: The new root of the subtree after rotation.
        """
        
        # TODO: implement the left rotation for AVL Tree
        a = x.right
        t2 = a.left

        a.left = x
        x.right = t2

        x.height = 1 + max(self._height(x.left), self._height(x.right))
        a.height = 1 + max(self._height(a.left), self._height(a.right))

        return a

    def balance(self, current: Optional[AVLNode]) -> int:
        if not current:
            return 0
        balance = self._height(current.left) - self._height(current.right)
        return balance

    def _insert_recursive(self, current: Optional[AVLNode], key: Any, value: Any) -> AVLNode:
        """
        Recursively inserts a new node with the given key and value into the AVL tree.
        Args:
            current (Optional[AVLNode]): The current node being considered during the recursive insertion.
            key (Any): The key of the new node.
            value (Any): The value of the new node.
        Returns:
            AVLNode: The updated AVL tree with the new node inserted.
        """
        # TODO: Implement a proper recursive insert function for an
        # AVL tree including updating height and balancing if a
        # new node is inserted.

        # recursive insert function taken from BST_index.py

        if not current:
            node = AVLNode(key)
            node.add_value(value)
            return node
        elif key < current.key:
            current.left = self._insert_recursive(current.left, key, value)
        elif key > current.key:
            current.right = self._insert_recursive(current.right, key, value)
        elif key == current.key:
            current.add_value(value)
            return current

        current.height = 1 + max(self._height(current.left), self._height(current.right))
        balance = self.balance(current)

        # Right Rotation
        if balance > 1 and self.balance(current.left) >= 0:
            return self._rotate_right(current)

        # Left Rotation
        if balance < - 1 and self.balance(current.right) <= 0:
            return self._rotate_left(current)

        # LR Rotation
        if balance > 1 and self.balance(current.left) < 0:
            current.left = self._rotate_left(current.left)
            return self._rotate_right(current)

        # RL Rotation
        if balance < -1 and self.balance(current.right) > 0:
            current.right = self._rotate_right(current.right)
            return self._rotate_left(current)

        return current


    def insert(self, key: Any, value: Any) -> None:
        """
        Inserts a key-value pair into the AVL tree. If the key exists, the
         value will be appended to the list of values in the node. 

        Parameters:
            key (Any): The key to be inserted.
            value (Any): The value associated with the key.

        Returns:
            None
        """
        if self.root is None:
            self.root = AVLNode(key)
            self.root.add_value(value)
        else:
            self.root = self._insert_recursive(self.root, key, value)

    # def _inorder_traversal(self, current: Optional[AVLNode], result: List[Any]) -> None:
    #     if current is None:
    #         return
        
    #     self._inorder_traversal(current.left, result)
    #     result.append(current.key)
    #     self._inorder_traversal(current.right, result)
   
    # def get_keys(self) -> List[Any]:
    #     keys: List[Any] = [] 
    #     self._inorder_traversal(self.root, keys)
    #     return keys

if __name__ == "__main__":
    avl = AVLTreeIndex()
    avl.insert(10, "A")
    avl.insert(20, "B")
    avl.insert(30, "C")
    avl.insert(15, "D")
    avl.insert(25, "E")
    avl.insert(5, "F")
    avl.insert(35, "G")

    print("Inorder traversal:", avl.get_keys_in_order())
    print("Height of tree:", avl.tree_height())
    print("Leaf nodes:", avl.get_leaf_keys())
