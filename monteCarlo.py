from board import *
from connectFour import *
import time
from numpy import sqrt, log as ln

def ucb(node):
    children = node.children()
    best_node = [node, -1]
    for child in children:
        value = child.victories / child.total + 2 * sqrt(2 * ln(node.total) / children.total)
        if value > best_node[1]:
            best_node = [child, value]
    return best_node[0]

def depth_limit(root, node=None, turn):
    if depth == 0:
        return node
    moves = possibleMoves(node.state)
    for move in moves:
        node.addChild(depth_limit(root, ))

def monteCarloSearch():
    start = time.time()
    while time.time() - start < 10:
        return None

def pickBestNode(root):
    node = root
    while node.children():
        node = ucb(node)