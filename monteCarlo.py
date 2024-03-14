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
        child.player = 'O' if self.player == 'X' else 'X'
    
    def uct(self, exploration_factor:int):
        if self.visits == 0:
            return float('inf')
        parent = self.parent
        
        if not parent or parent.visits == 0:
            parent_visits = 1
        else:
            parent_visits = parent.visits
        exploitation = self.wins / self.visits
        exploration = exploration_factor * sqrt(ln(parent_visits) / self.visits)
        return exploitation + exploration
    
    def get_best_child(self):
        scores = [(child, child.uct()) for child in self.children]
        best_score = float('-inf')
        best_childs = []
        for child, score in scores:
            if best_score < score: 
                best_score = score
                best_childs = [child]
            elif best_score == score:
                best_childs.append(child)
        return random.choice(best_childs)

class MCTS:
    def __init__(self, state:Board, player:str, exploration_factor:int) -> None:
        self.root = Node(state, player)
        self.exploration_factor = exploration_factor
        
    def refresh_state(self, state:Board):
        player = 'X' if self.root.player == 'O' else 'O'
        if len(self.root.children) != 0:
            for child in self.root.children:
                if child.state == state:
                    self.root = child
                    return
        self.root = Node(state)
        self.root.player = player
        
    def select(self) -> Node:
        node = self.root
        while len(node.children) != 0:
            best_score = float('-inf')
            best_child = None
            for child in node.children:
                # Calculate UCT score for each child
                uct_score = child.uct(self.exploration_factor)
                if uct_score > best_score:
                    best_child = child
                    best_score = uct_score
            node = best_child
            if node.visits == 0:
                return node
        if self.expand(node):
            node = random.choice(node.children)
        return node
      
    def expand(self, node:Node) -> bool:
        if isinstance(self.root.state.finished(), str):
            return False
        oponnent = 'O' if self.root.player == 'X' else 'X'
        children = [child for child, *_ in possibleMoves(self.root.state, self.root.player)]
        for child_state in children:
            node.add_child(Node(child_state, oponnent))
        return True
    
    def simulate(self, node:Node) -> str:
        state = node.state
        player = ['X', 'O'] if node.player == 'X' else ['O', 'X']
        while isinstance(state.finished(), bool):
            results = [cur[0] for cur in possibleMoves(state, player[0])]
            state = random.choice(results)
            player.reverse()
        return state.finished()
    
    def back_propagation(self, node:Node, result:str) -> None:
        while node.parent:
            point = 1 if node.player == result else 0
            node.visits += 1
            node.wins += point
            node = node.parent
        
    def search(self, max_time:int):
        start = time.time()
        while time.time() - start < max_time:
            node = self.select()
            result = self.simulate(node)
            self.back_propagation(node, result)
        
    def best_move(self) -> Node:
        best_score = float('-inf')
        best_child = []
        for child in self.root.children:
            score = child.uct(self.exploration_factor)
            if best_score < score:
                best_child = [child]
                best_score = score
            elif best_score == score:
                best_child.append(child)
        print(best_child)
        return random.choice(best_child)

def game_monte_carlo(board: Board, order: list):
    print(board)
    mcts = MCTS(board, order[0], sqrt(2))
    while True:
        #checks winner
        if winnerAi(board, order):
            return None
        
        print('Tua vez.')
        askForNextMove(board, order[0])
        mcts.refresh_state(board) #estado é atualizado
        print(board)
        
        #checks winner
        if winnerAi(board, order):
            return None
        
        print('IA')
        mcts.search(3)
        best_node = mcts.best_move()
        board = best_node.state
        mcts.refresh_state(board)
        print(board)
