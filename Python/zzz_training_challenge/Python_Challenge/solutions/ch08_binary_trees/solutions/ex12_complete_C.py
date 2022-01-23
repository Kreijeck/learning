# Beispielprogramm für das Buch "Python Challenge"
#
# Copyright 2020 by Michael Inden


from ch05_datastructures.util.queue import Queue
from ch08_binary_trees.util import TreeUtils
from ch08_binary_trees.intro.intro_binary_tree_node import BinaryTreeNode


def levelorder_is_complete(start_node):
    if start_node is None:
        return False

    to_process = Queue()
    to_process.enqueue(start_node)

    # Indikator, dass ein Knoten nicht zwei Nachfolger hat   full nodes
    missing_node = False

    while not to_process.is_empty():
        current = to_process.dequeue()

        # Nur Nachfahren auf der rechten Seite
        if current.left is None and current.right is not None:
            return False

        # Wenn zuvor ein fehlender Knoten entdeckt wurde,
        # dann darf der nächste nur ein Blatt sein
        if missing_node and not current.is_leaf():
            return False

        # Nimm Subelemente auf, markiere, falls nicht vollständig
        if current.left is not None:
            to_process.enqueue(current.left)
        else:
            missing_node = True

        if current.right is not None:
            to_process.enqueue(current.right)
        else:
            missing_node = True

    # Alle Knoten erfolgreich getestet
    return True


def main():
    F = create_completness_example_tree()
    TreeUtils.nice_print(F)
    print("levelorder_is_complete?", levelorder_is_complete(F))

    # Modifikation: entferne Blätter unter H
    #F.right.left = None
    F.right.right = None
    TreeUtils.nice_print(F)
    print("levelorder_is_complete?", levelorder_is_complete(F))

    # Modifikation: entferne Blätter unter H
    F.right.left = None
    TreeUtils.nice_print(F)
    print("levelorder_is_complete?", levelorder_is_complete(F))


def create_completness_example_tree():
    F = BinaryTreeNode("F")
    TreeUtils.insert(F, "D")
    TreeUtils.insert(F, "H")
    TreeUtils.insert(F, "B")
    TreeUtils.insert(F, "E")
    TreeUtils.insert(F, "A")
    TreeUtils.insert(F, "C")
    TreeUtils.insert(F, "G")
    TreeUtils.insert(F, "I")
    return F


if __name__ == "__main__":
    main()
