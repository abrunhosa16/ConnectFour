from board import Board
from connectFour import possibleMoves
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
    #     return self.state == other.state and self.visits == other.visits and self.wins == other.wins
    
    def __str__(self) -> str:
        string = "Estado: " + str(type(self.state)) + '\n'
        string += "Pai: " + str(self.parent != None) + '\n'
        string += "Filhos: " + str(len(self.children)) + '\n'
        string += "Vitórias: " + str(self.wins) + '\n'
        string += "Total: " + str(self.visits) + '\n'
        string += "Constante: " + str(self.c) + '\n'
        string += "Pontuação: " + str(self.uct()) + '\n'
        return string
    
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
        best_child = max(self.root.children, key=lambda child: child.uct())  
        return best_child
    
    def select(self) -> Node:
        node = self.root
        while len(node.children) > 0 and all(child.visits > 0 for child in node.children):
            node = self.best_child(node)
        return node

    def expand(self, node:Node) -> Node:
        child_states = [child_state for child_state, *_ in possibleMoves(node.state, node.state.player)]
        for child_state in child_states:
            node.add_child(Node(child_state))
        return random.choice(node.children)
        
    def rollout(self, node:Node) -> str:
        state = node.state
        while state.finished() == False:
            state = self.rollout_policy(state)
        return state.finished()

    def rollout_policy(self, state):
        return random.choice([child_state for child_state, *_ in possibleMoves(state, state.player)])

    def back_propagation(self, node:Node, winner_symbol:str) -> None:
        while node:
            node.visits += 1
            if winner_symbol == node.state.player:
                node.wins += 1
            node = node.parent

    def search(self, max_time:int) -> Node:
        start_time = time.time()
        # while time.time() - start_time < max_time:
        for _ in range(max_time):
            selected = self.select()
            expanded = self.expand(selected)
            result = self.rollout(expanded)
            self.back_propagation(expanded, result)
        return self.best_child()

b = Board('X')
b.setPos(5,3,'X')
n = Node(b)
m = MCTS(n)
best = m.search(10)
print(m.best_child())


