from board import *
from connectFour import *
import time
import random
from numpy import sqrt, log as ln

class Node:
    def __init__(self, state, player=None) -> None:
        self.state = state
        self.parent = None
        self.children = []
        self.wins = 0
        self.visits = 0
        self.player = player #player que irá jogar no estado atual
    
    def __str__(self) -> str:
        string = "Pai: " + str(isinstance(self.parent, Node)) + '\n'
        string += "Filhos: " + str(len(self.children)) + '\n'
        string += "Vitórias: " + str(self.wins) + '\n'
        string += "Visitas: " + str(self.visits) + '\n'
        string += "Jogador: " + str(self.player) + '\n'
        return string
    
    def add_child(self, child) -> None:
        self.children.append(child)
        child.parent = self
        if self.player == 'X':
            child.player = 'O'
        else: child.player = 'X'

    def increase_win_value(self, player: str):
        self.visits += 1
        if self.player == player:
            self.wins += 1
        if self.parent:
            self.parent.increase_win_value(player)
    
    def get_score(self):
        parent = self.parent
        if self.visits != 0:
            exploitation = self.wins / self.visits
            exploration = sqrt(2) * sqrt(2 * ln(parent.visits) / self.visits) if parent else 0
            return exploitation + exploration
        return 0
    
    def get_best_child(self):
        best_score = float('-inf')
        best_child = []
        for child in self.children:
            score = child.get_score()
            if best_score < score:
                best_child = [child]
                best_score = score
            elif best_score == score:
                best_child.append(child)
        return random.choice(best_child)

def new_childs(node: Node):
    board = node.state
    moves = possibleMoves(board, node.player)
    for state, row, col in moves:
        child = Node(state)
        node.add_child(child)
        
def selection(node: Node):
    return node.get_best_child()
    
def expansion(node: Node):
    new_childs(node)
       
def simulation(node: Node) -> None:
    while node.state.finished() == False:
        new_childs(node)
        node = random.choice(node.children)

def monte_carlo(root: Node, maxTime):
    start = time.time()
    while time.time() - start < maxTime:
        node = root
        new_childs(node)
        # Selection
        while node.children:
            node = selection(node)
        # Expansion
        if isinstance(node.state.finished(), bool):
            expansion(node)
            node = random.choice(node.children)
        # Simulation
        simulation(node)
    return root.get_best_child()

def game_monte_carlo(board: Board, order: list):
    print(board)
    while True:
        #checks winner
        if winnerAi(board, order):
            return None
        
        print('Tua vez.')
        turn, col, line = askForNextMove(board, order[0])
        move(board, turn, col, line)
        print(board)
        
        #checks winner
        if winnerAi(board, order):
            return None
        
        board = monte_carlo(Node(board, order[1]), 2).state
        print(board)

b=Board()
player = ['X', 'O']
for i in range(10):
    moves = possibleMoves(b, player[0])
    b, line, col = random.choice(moves)
    player.reverse()
print(b)

n=Node(b, player[0])
p=monte_carlo(n, 2)
print(p.state)