from Algorithm import Algorithm
from Board import Board

import random
import copy


class K_beam(Algorithm):
    def __init__(self):
        super().__init__()
    
    def solve(self, config,K,max_iteration = 100):
        queen_loc = self.queens_indices(config)
        if(self.count_conflicts(queen_loc) == 0):
            return config, 0
        #generate random k states
        successors = self.generate_random_states(queen_loc,K-1)
        successors.append(queen_loc)
        conflict_count = self.count_conflicts(queen_loc)
        expanded = 0
        iterations = max_iteration
        
        while conflict_count > 0 and iterations > 0: 
            expanded += len(successors)
            new_successor = []
            #found the successor of K states
            for elem in successors:
                suc = self.get_successors(elem)
                for s in suc:
                    if s not in new_successor:
                        new_successor.append(s)
            #count conflict for each successor
            conflict_num = []
            for suc in new_successor:
                conflict = self.count_conflicts(suc)
                if conflict == 0:
                    return self.create_board(suc),expanded,max_iteration-iterations
                conflict_num.append((conflict,suc))
            conflict_num.sort(key= lambda tup: tup[0])
            conflict_count = conflict_num[0][0]
            if(len(conflict_num) > K):
                successors = [elem[1] for elem in conflict_num[:K]]
            else:
                successors = [elem[1] for elem in conflict_num]
            iterations -= 1
        return None,expanded,max_iteration

    def create_board(self,queen_loc):
        board = Board()
        conf = ''
        for i in range(8):
            for j in range(8):
                if (i,j) in queen_loc:
                    conf += 'Q'
                else:
                    conf += '#'
                if j < 7:
                    conf += ' '
            if i < 7:
                conf += '\n'
        board.config = conf
        return board

    def count_conflicts(self,successor):
        conflict_count = 0
        for i in range(8):
            for j in range(i+1,8):
                if successor[i][0] == successor[j][0]:
                    conflict_count += 1
                if successor[i][1] == successor[j][1]:
                    conflict_count += 1
                if abs(successor[i][0]-successor[j][0]) == abs(successor[i][1]-successor[j][1]) :
                    conflict_count += 1
        return conflict_count

    def get_successors(self,queens_loc):
        moves = [(-1,-1),(-1,0),(-1,1),
        (0,-1),(0,1),
        (1,-1),(1,0),(1,1)]
        sucessors = []
        original_config = [elem for elem in queens_loc]
        for loc in queens_loc:
            original_config.remove(loc)
            for move in moves:
                new_config = (loc[0]+move[0],loc[1]+move[1])
                if new_config in original_config:
                    continue
                if new_config[0] >= 8 or new_config[0] < 0:
                    continue
                if new_config[1] >= 8 or new_config[1] < 0:
                    continue
                original_config.append(new_config)
                sucessors.append(copy.deepcopy(original_config))
                original_config.remove(new_config)
            original_config.append(loc)
        return sucessors

    def queens_indices(self,config):
        index = []
        for i in range(len(config)):
            for j in range(len(config)):
                if config[i][j] == 1:
                    index.append((i,j))
        return tuple(index)

    def generate_random_states(self,queen_loc,K):
        suc = self.get_successors(queen_loc)
        random.shuffle(suc)
        if len(suc) > K:
            successor = copy.deepcopy(suc[0:K])
        else:
            successor = copy.deepcopy(suc)
        
        return successor

    def possible(self,loc,queen_loc):
        moves = [(-1,-1),(-1,0),(-1,1),
        (0,-1),(0,1),
        (1,-1),(1,0),(1,1)]
        p = []
        for m in moves:
            new_loc = (loc[0]+m[0],loc[1]+m[1])
            if new_loc[0] >= 8 or new_loc[0] < 0:
                continue
            if new_loc[1] >= 8 or new_loc[1] < 0:
                continue
            if new_loc in queen_loc:
                continue
            p.append(m)
        return p