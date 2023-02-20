
import example_tubes
from collections import Counter



class TubeSorter:

    def __init__(self, matrix):
        self.heigth = len(matrix[0])
        self.width = len(matrix)
        self.tubes = self.start_removeZero(m = matrix)        # Will alter
        self.balls = self.ball_unique()
        self.movelog = {}
        self.tops = self.tubes_tops()

    def start_removeZero(self, m):
        for i in range(self.width):
            if self.tube_num(m[i]) < self.heigth:
                m[i] = [z for z in m[i] if z != 0]
        return m

    def tube_check(self, t):    # Check if tube good
        return all(elem == t[0] for elem in t)
    
    def tubes_check(self):      # Check all tubes
        return all(self.tube_check(elem) for elem in self.tubes)
    
    def tube_num(self, t):      # Return # balls
        return sum(map(lambda x : x != 0, t))

    def tube_top(self, t):      # Return top ball
        for i in reversed(range(len(t) - 3)):
            if t[i] != 0:
                return t[i]
        return t[0]

    def ball_unique(self):
        unique_list = []    
        for t in range(len(self.tubes)):
            for x in self.tubes[t]:
                # check if exists in unique_list or not
                if x not in unique_list and x != 0:
                    unique_list.append(x)
        return unique_list

    def move_check(self, t1,t2):        # Check if can move 1 from t1 to t2
        tube1 = self.tubes[t1]
        tube2 = self.tubes[t2]
        if self.tube_num(tube2) == 4:      #full tube
            return False
        elif tube2[0] == 0 :               #empty tube
            return True
        elif self.tube_top(tube1) == self.tube_top(tube2):  #tops match
            return True
        return False

    def tubes_tops(self):
        tops = []
        for i in range(self.width):
            if self.tube_num(self.tubes[i]) > 0:
                b = list(Counter(self.tubes[i]).keys())[-1]
                n = list(Counter(self.tubes[i]).values())[-1]
                tops.append([b,n])   
            else:
                tops.append([0,4]) # Empty Row
        return tops        

    def move_top(self, t1,t2):
        n1 = self.tube_num(self.tubes[t1])
        n2 = self.tube_num(self.tubes[t2])
        b = t1[n1-1]
        ## NEED to finish
      
    def solve_check(self):           # Check solvable still or solved
        if any(elem[0] == 0 for elem in self.tubes): #has empty tube
            return True
        elif all(self.tube_check(elem) for elem in self.tubes): #solved
            return True
        return False

    def Sorter(self):
        while not self.solve_check(self.tubes):
                # Random
                #   Combo of patterns and rando, with logic to not retrace to inf loop
                # Patterns
                #   Starts:
                #       Has most on tops, move them to one of opens
                #   Middle:
                #       3 in a row, 1 on top off, 4th is available, move top 1 off, complete
                #       Tube partial but all one color and finishing color available
            pass
        #     solved = tubes        
        # return solved


plz = TubeSorter(matrix = example_tubes.tubes_4x6_solved)
plz.tubes
plz.tops
plz.balls
plz.heigth
plz.width



plz = TubeSorter(matrix = example_tubes.tubes_4x6_easy)
plz.tubes
plz.tops

plz.tubes_tally()

