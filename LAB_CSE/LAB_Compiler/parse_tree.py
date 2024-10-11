# -------------------------------------------------------------------------------------
#
#   Class storing parse tree nodes.
#   It keeps symbol value - terminal or non-terminal and children.
#   In case the symbol is terminal - children array must be empty.
#   It is due to the fact that a terminal symbol does not have any production rules so it can be only a leaf.
#
# -------------------------------------------------------------------------------------

class Node:
    def __init__(self, symbol):
        self.symbol = symbol
        self.children = []

    def add_children(self, node):
        self.children.append(node)

    def remove_children(self):
        self.children = []

    def print_node(self):
        print("symbol: ", self.symbol)
        print("children: ", self.children)