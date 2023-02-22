
import Ex_tubes
from Status import TubeStatus
# from collections import Counter
# import time
import random


class TubeSorter(TubeStatus):

    def __init__(self, matrix):
        TubeStatus.__init__(self, matrix)

        #Sort Loop:
        self.iter = 0
        self.iterMAX = 2000
        self.found = 0
        # ADD LATER: reset feature if deadend, counter to limit resets


    def move_top(self, t1, t2):
            # 1 check oposite move wasn't just performed
            # Shouldn't be able to move back though with check of them not matching #2
            # ADD LATER: more extensive check on multi recent that there isn't an endless loop of backtracking
        lastMove = []
        if self.movelog != []: 
            lastMove = self.movelog[-1] 

        if lastMove == [t2,t1]:  # Don't check on first move
            # print("Opp Move Canceled")
            return False
            # 2 check top balls match and is empty in t2
        elif self.tops[t1][0] != self.tops[t2][0] and self.tops[t2][0] != 0:
        # elif self.tops[t1][0] != self.tops[t2][0] or (self.tops[t1] == [] and self.tops[t2] == []):
            # print("Top Balls don't match")
            return False
            # 3 check num of ball t1 fits in t2 or moving empty
        elif self.tops[t1][1] > self.tops[t2][2] or self.tops[t1][0] == 0:
            # print("Num Ball Dont Fit")
            return False
            # 4 remove balls from t1, add to t2, log move, update tops & cols
        else:
            b1 = self.tops[t1][0]
            n1 = self.tops[t1][1]
            self.tubes[t1] = self.tubes[t1][: len(self.tubes[t1]) - n1]
            for n in range(n1):
                self.tubes[t2].append(b1)
            self.movelog.append([t1,t2])
            self.tops = self.tubes_tops()
            self.cols = self.tubes_avail()
            return True

    def sort_brute(self):
        while not self.tubes_check() and len(self.movelog) < 100 and self.iter < self.iterMAX:
            random.shuffle(self.cols)
            for f in self.cols:
                if self.found == 1:
                    self.found  = 0; break # escape for F
                for s in self.cols:
                    if f != s:  # don't move to same column
                        self.iter += 1
                        # time.sleep(1); print([f,s])
                        if self.move_top(t1 = f, t2 = s):
                            # print(self.tubes); print(self.tops); print(self.cols)
                            self.found = 1; break # escape for S
                            # print(self.tops)
                    # print(self.movelog)
        print(self.tubes)


    def Sorter(self):
        while not self.tubes_check():
            self.sort_brute()
        print(self.tubes)
                


Ex_tubes.t_4x6_1234
Ex_tubes.t_4x6_easy
Ex_tubes.t_4x6_solved
Ex_tubes.t_4x14_hard


game = TubeSorter(matrix = Ex_tubes.t_4x14_hard)
game.tubes
game.tops
game.cols
game.movelog

game.Sorter()

game.move_top(t1=4,t2=5)




                # Random
                #   Combo of patterns and rando, with logic to not retrace to inf loop
                # Patterns
                #   Starts:
                #       Has most on tops, move them to one of opens
                #   Middle:
                #       3 in a row, 1 on top off, 4th is available, move top 1 off, complete
                #       Tube partial but all one color and finishing color available