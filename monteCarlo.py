from board import Board
from connectFour import askForNextMove, winnerAi, possibleMoves
from numpy import sqrt, log as ln
from copy import deepcopy
import random
import time

class Node:
    def __init__(self, state) -> None:
        self.state = state
        self.parent = None
        self.children = []
        self.c = 100
        self.visits = 0
        self.wins = 0
    
    # def __eq__(self, other) -> bool:
    #     return self.state == other.state
    
    def __str__(self) -> str:
        string = "Estado: " + str(type(self.state)) + '\n'
        string += "Pai: " + str(self.parent != None) + '\n'
        string += "Filhos: " + str(len(self.children)) + '\n'
        string += "Vitórias: " + str(self.wins) + '\n'
        string += "Total: " + str(self.visits) + '\n'
        string += "Constante: " + str(self.c) + '\n'
        string += "Pontuação: " + str(self.uct()) + '\n'
        return string
    
    def copy(self):
        new_state = self.state.boardCopy()
        new_node = Node(new_state)
        new_node.visits = self.visits
        new_node.wins = self.wins
        return new_node
    
    def add_child(self, child) -> bool:
        #se o estado já estiver como filho
        if any(child.state == node.state for node in self.children):
            return False

        self.children.append(child)
        child.parent = self
        return True
    
    def add_children(self, children) -> None:
        for child in children:
            self.add_child(child)

    def uct(self) -> float:
        if self.visits == 0:
            return float('inf')
        exploitation = self.wins / self.visits
        exploration = self.c * sqrt(2 * ln(self.parent.visits) / self.visits) if self.parent else 0
        return exploitation + exploration
    
class MCTS:
    def __init__(self, root:Node) -> None:
        self.root = root

    def best_child(self, node=None) -> Node:
        if node is None:
            node = self.root

        if not node.children:
            return None

        best_child = []
        best_score = float('-inf')

        for child in node.children:
            score = child.uct()
            if score > best_score:
                best_child = [child]
                best_score = score
            elif score == best_score:
                best_child.append(child)
        return random.choice(best_child)
    
    def update_state(self, state) -> None:
        for child in self.root.children:
            if child.state == state:
                self.root = child
                self.root.parent = None
                return 
        self.root = Node(state)
        
    def select(self) -> Node:
        node = self.root

        while len(node.children) > 0:
            node = self.best_child(node)
        return node

    def expand(self, node:Node) -> Node:
        child_moves = possibleMoves(node.state)
        for line, col in child_moves:
            child_state = node.state.boardCopy()
            child_state.setPos(line, col, child_state.player)
            if len(node.children) > 0:
                for child in node.children:
                    if child_state != child.state:
                        node.add_child(Node(child_state))
            else:
                node.add_child(Node(child_state))
        return random.choice(node.children)
        
    def rollout(self, node:Node) -> str:
        state = node.state.boardCopy()
        while state.finished() == False:
            state = self.rollout_policy(state)
        return state.finished()

    def rollout_policy(self, state):
        line, col = random.choice(possibleMoves(state))
        state.setPos(line, col, state.player)
        return state

    def back_propagation(self, node:Node, winner_symbol:str) -> None:
        while node:
            node.visits += 1
            if winner_symbol == node.state.player:
                node.wins += 1
            node = node.parent

    def search(self, max_time:int) -> Node:
        start_time = time.time()
        # while time.time() - start_time < max_time:
        while time.time() - start_time < max_time:
            
            selected = self.select()
            expanded = self.expand(selected)
            result = self.rollout(expanded)
            self.back_propagation(expanded, result)
        return self.best_child()

def gameMonteCarlo(board:Board, order):
    print(board)
    m =MCTS(board)
    while True:
        print('Tua vez.')
        askForNextMove(board, board.player)
        m.root = Node(board)
        print(board)
        
        #checks winner
        if winnerAi(board, order):
            return None
        
        board = m.search(10).state
        m.update_state(board)
        print(board)
        
        #checks winner
        if winnerAi(board, order):
            return None
        
        
gameMonteCarlo(Board('X'), ['X', 'O'])

# b = Board('X')
# b.setPos(5,3,'X')
# b.setPos(5,2,'O')
# b.setPos(5,4,'X')
# b.setPos(4,3,'O')
# b.setPos(5,5,'X')
# m = MCTS(Node(b))
# child = m.search(10)

# for c in m.root.children:
#     print(c.visits)
# print(child.state)

# p = Node(b)
# for line, col in possibleMoves(b):
#     copy = b.boardCopy()
#     copy.setPos(line, col, 'O')
#     p.add_child(Node(copy))
# node = p
# while len(node.children) > 0:
#     node = random.choice(node.child)
#     print(1)