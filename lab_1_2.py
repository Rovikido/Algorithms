import os


class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self, root_data):
        self.root = Node(root_data)

    def SearchNode(self, data):
        return self.__SearchNode(data, self.root)[0]

    def __SearchNode(self, data, root, parent=None):
        if root is None or root.data == data:
            return root, parent
        if data > root.data:
            return self.__SearchNode(data, root.right, root)
        if data < root.data:
            return self.__SearchNode(data, root.left, root)

    def InsertNode(self, data):
        node, parent = self.__SearchNode(data, self.root)
        if node is not None:
            print("Node already exist!")
        if data < parent.data:
            parent.left = Node(data, parent)
        elif data > parent.data:
            parent.right = Node(data, parent)

    def DeleteNode(self, data):
        node, parent = self.__SearchNode(data, self.root)
        if node.left is None and node.right is None:
            if self.root.data == data:
                print("Last object cannot be deleted!")
                return
            if data < parent.data:
                parent.left = None
            elif data > parent.data:
                parent.right = None
        elif (node.left is not None) ^ (node.right is not None):
            if self.root.data == data:
                self.root = node.left if node.left else node.right
            elif data < parent.data:
                parent.left = node.left if node.left else node.right
                parent.left.parent = parent
            elif data > parent.data:
                parent.right = node.left if node.left else node.right
                parent.right.parent = parent
        else:
            new = self.__DeleteNode_2с(node, data)
            if node is self.root:
                self.root = self.root.right

    def __DeleteNode_2с(self, node, data):
        min = self.__get_min(node.right)
        min.left = node.left
        print(min.data)
        if node is not self.root:
            if data < node.parent.data:
                node.parent.left = min
            else:
                node.parent.right = min
        # if node is self.root:
        #     self.root = node.
        min.parent = node.parent
        print(node.data)
        return min

    def __get_min(self, node):
        rec_node = node
        while rec_node.left is not None:
            rec_node = rec_node.left
        return rec_node


COUNT = [10]


def print2DUtil(root, space):
    if (root == None):
        return

    space += COUNT[0]
    print2DUtil(root.right, space)
    print()
    for i in range(COUNT[0], space):
        print(end=" ")
    print(root.data)
    print2DUtil(root.left, space)


def print2D(root):
    print2DUtil(root, 0)


def print_values(root):
    if root is None:
        return
    print(root.data)
    print_values(root.left)
    print_values(root.right)


def create_tree():
    data = int(input("Enter data for root: "))
    return BST(data)

def insert_node(tree):
    data = int(input("Enter data: "))
    tree.InsertNode(data)
    return tree

def delete_node(tree):
    data = int(input("Enter data to be deleted: "))
    tree.DeleteNode(data)
    return tree

def find_node(tree):
    data = int(input("Enter node to be found: "))
    res = tree.SearchNode(data)
    print("Node was found" if res is not None else "Node was not found")
    return tree

def menu():
    action = input("Chose action:\n"
                   + "1. Create tree\n"
                   + "2. Insert Node\n"
                   + "3. Delete Node\n"
                   + "4. Find Node\n")
    return action


if __name__ == '__main__':
    act_dict = {"1": create_tree, "2": insert_node, "3": delete_node, "4": find_node}
    tree = create_tree()
    while True:
        try:
            print("\n" * 20)
            print2D(tree.root)
            print("\n" * 3)
            tree = act_dict[menu()](tree)
        except KeyError:
            print("Key not found")
        except Exception as e:
            print(e)