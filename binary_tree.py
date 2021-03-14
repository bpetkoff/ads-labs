def BinaryTree(r):
    return [r, [], []]

def insertLeft(root, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root


def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root, newVal):
    root[0] = newVal


def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

def preorder_traverse(tree):
    """This is preorder traverse of the tree"""
    print(getRootVal(tree))
    if getLeftChild(tree):
        preorder_traverse(getLeftChild(tree))
    if getRightChild(tree):
        preorder_traverse(getRightChild(tree))

def get_size(root):
    """This is preorder traverse of the tree"""
    if getRootVal(root) is None:
        return 0
    return [getRootVal(root)] + get_size(getLeftChild(root)) + get_size(getRightChild(root))



def postorder_traverse(tree):
    """This should be postorder traverse, but is not working yet"""
    if getLeftChild(tree):
        postorder_traverse(getLeftChild(tree))
    if getRightChild(tree):
        postorder_traverse(getRightChild(tree))
    print(getRootVal(tree))


if __name__ == "__main__":

    root = BinaryTree("a")
    insertLeft(root, "b")
    insertRight(getLeftChild(root), "d")


    insertRight(root, "c")
    insertLeft(getRightChild(root), "e")
    insertRight(getRightChild(root), "f")


    print(root)
    # print(getRootVal(root))
    # print(getRootVal(getLeftChild(root)))
    # print(getRootVal(getRightChild(getLeftChild(root))))
    # print(getRootVal(getRightChild(root)))
    # print(getRootVal(getLeftChild(getRightChild(root))))
    # print(getRootVal(getRightChild(getRightChild(root))))

    print(get_size(root))
    # postorder_traverse(root)
