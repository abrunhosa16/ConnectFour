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
        self.c = 1
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
        string += "Probabilidade de vitória: " + str(self.win_probability()) + '\n'
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
    
    def win_probability(self) -> float:
        return self.wins /self.visits
    
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
    
    def winner(self):
        best_child = []
        best_score = float('-inf')

        for child in self.root.children:
            score = child.win_probability()
            if score > best_score:
                best_child = [child]
                best_score = score
            elif score == best_score:
                best_child.append(child)
        return random.choice(best_child)

    def update_state(self, state) -> None:
        self.root = Node(state)
        
    def select(self) -> Node:
        node = self.root

        while len(node.children) > 0:
            node = self.best_child(node)
        return node

    def expand(self, node:Node) -> Node:
        child_moves = possibleMoves(node.state)
        if len(child_moves) == 0:
            print(node.state)
            print('--------ERRO--------')

        for line, col in child_moves:
            child_state = node.state.boardCopy()
            child_state.setPos(line, col, child_state.player)
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
            if winner_symbol != node.state.player and winner_symbol != 'Tie':
                node.wins += 1
            node = node.parent

    def search(self, max_time:int) -> Node:
        start_time = time.time()
        count = 0
        while time.time() - start_time < max_time:
            count += 1
            selected = self.select()
            result = selected.state.finished()
            if isinstance(result, bool):
                expanded = self.expand(selected)
                result = self.rollout(expanded)
                self.back_propagation(expanded, result)
            else:
                self.back_propagation(selected, result)
            
        print('Foram feitas ' + str(count) + ' simulações.')
        return self.winner()

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
