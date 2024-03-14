from board import Board
from connectFour import possibleMoves
from numpy import sqrt, log as ln
from copy import deepcopy
import random

class Node:
    def __init__(self, state) -> None:
        self.state = state
        self.parent = None
        self.children = []
        self.c = sqrt(2)
        self.visits = 0
        self.wins = 0
    
    def __str__(self) -> str:
        string = "Estado: " + str(type(self.state)) + '\n'
        string += "Pai: " + str(self.parent != None) + '\n'
        string += "Filhos: " + str(len(self.children)) + '\n'
        string += "Constante: " + str(self.c)
        return string
    
    def add_child(self, child) -> bool:
        #se o estado já estiver como filho
        for node in self.children:
            if node.state == child.state:
                return False
            
        self.children.append(child)
        child.parent = self
        return True
    
    def add_children(self, children) -> None:
        for child in children:
            self.add_child(child)

    def uct(self) -> float:
        if self.wins == 0:
            return float('inf')
        exploitation = self.wins / self.visits
        exploration = self.c * sqrt(2 * ln(self.parent.visits) / self.visits)
        return exploitation + exploration
    
class MCTS:
    def __init__(self, root:Node) -> None:
        self.root = root

    def select(self) -> Node:
        node = deepcopy(self.root)
        #se tivver filhos
        while len(node.children) > 0:
            best_childs = []
            best_uct = float('-inf')
            for child in node.children:
                uct = child.uct()
                if uct > best_uct:
                    best_uct = uct
                    best_childs = [child]
                elif uct == best_uct:
                    best_childs.append(child)
        return node

    def expand(self, node:Node) -> Node:
        child_states = [child_state for child_state, *_ in possibleMoves(node.state, node.state.player)]
        expanded_node = Node(random.choice(child_states))
        node.add_child(expanded_node)
        return expanded_node
        
    def rollout(self, node:Node) -> str:
        state = node.state
        while state.finshed() == False:
            state = self.rollout_policy(state)
        return state.finished()

    def rollout_policy(self, state):
        return random.choice([child_state for child_state, *_ in possibleMoves(state, state.player)])

    def back_propagation(self, node:Node, winner_symbol:str) -> None:
        while node.parent:
            node.visits += 1
            if winner_symbol == node.state.player:
                node.wins += 1
            node = node.parent
