class AVL_Tree_Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class AVL_Tree:

    def __init__(self):
        self.root = None

    def _max_height(self, node):
        if not node:
            return 0
        return 1+max(self._max_height(node.left), self._max_height(node.right))

    def _rotate_right(self, skew_point):
        skew_point.left.parent = skew_point.parent
        if(skew_point.left.parent == None):
            self.root = skew_point.left
        else:
            skew_point.parent.left = skew_point.left
        curr_node = skew_point.left
        skew_point.left = None
        while(curr_node.right):
            curr_node = curr_node.right
        curr_node.right = skew_point
        skew_point.parent = curr_node

    def _rotate_left(self, skew_point):
        skew_point.right.parent = skew_point.parent
        if(skew_point.right.parent == None):
            self.root = skew_point.right
        else:
            skew_point.parent.right = skew_point.right
        curr_node = skew_point.right
        skew_point.right = None
        # import pdb; pdb.set_trace()
        while(curr_node.left):
            curr_node = curr_node.left
        curr_node.left = skew_point
        skew_point.parent = curr_node

    def insert(self, val, curr_node, parent_node):
        if(not curr_node):
            node = AVL_Tree_Node(val)
            node.parent = parent_node
            return node

        if(val < curr_node.val):
            curr_node.left = self.insert(val, curr_node.left, curr_node)
        else:
            curr_node.right = self.insert(val, curr_node.right, curr_node)
        return curr_node

    def find_point_of_rotation(self, node):
        if(not node):
            return None
        left_height = 0
        if(node and node.left):
            left_height = self._max_height(node.left)
        right_height = 0
        if(node and node.right):
            right_height = self._max_height(node.right)

        left_subtree_node = self.find_point_of_rotation(node.left)
        right_subtree_node = self.find_point_of_rotation(node.right)

        if(abs(left_height-right_height) > 1):
            return left_subtree_node or right_subtree_node or node
        else:
            return left_subtree_node or right_subtree_node
        
    def rotate_tree(self, node):
        left_height = 0
        if(node and node.left):
            left_height = self._max_height(node.left)
        right_height = 0
        if(node and node.right):
            right_height = self._max_height(node.right)

        if(abs(left_height-right_height) > 1):
            if(left_height > right_height):
                new_node = self._rotate_right(node)
            else:
                new_node = self._rotate_left(node)
        

    def preorder(self, node, array):
        if(node):
            array.append(node.val)
            self.preorder(node.left, array)
            self.preorder(node.right, array)

tree = AVL_Tree()

nums = [2, 3, 4, 5, 6, 7]

for i in nums:
    tree.root = tree.insert(i, tree.root, None)
    node = tree.find_point_of_rotation(tree.root)
    while node:
        print(node.val)
        tree.rotate_tree(node)
        node = tree.find_point_of_rotation(tree.root)

    p = []
    tree.preorder(tree.root, p)
    print(p)





