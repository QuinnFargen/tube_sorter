
import Ex_tubes
from Status import TubeStatus
import time
import random


class TubeSorter(TubeStatus):

    def __init__(self, matrix):
        TubeStatus.__init__(self, matrix)
        self.iter = 0
        self.found = 0
        self.reset = 0
        self.bruteMAX = 2000
        self.moveMAX = 50
        self.resetMAX = 10

    def reset_tubes(self):
        print("reseting tube:"); print(self.tubes)
        self.tubes = list(self.start)
        self.tops = self.tubes_tops()
        self.cols = self.tubes_avail()
        self.movelog = []; self.iter = 0; self.found = 0; self.reset += 1

    def sort_brute(self):
        if self.tubes != self.start:    #reset if not starting from beginning.
            self.reset_tubes()
        while not self.tubes_check() and len(self.movelog) < self.moveMAX and self.iter < self.bruteMAX:
            random.shuffle(self.cols)
            for f in self.cols:
                if self.found == 1:
                    self.found  = 0; break # escape for F
                for s in self.cols:
                    if f != s:  # don't move to same column
                        self.iter += 1
                        if self.move_top(t1 = f, t2 = s):
                            self.found = 1; break # escape for S

    def Sorter(self):
        while not self.tubes_check() and self.reset <= self.resetMAX:
            self.sort_brute()
        print(self.tubes)
                







Ex_tubes.t_4x6_1234
Ex_tubes.t_4x6_easy
Ex_tubes.t_4x6_solved
Ex_tubes.t_4x14_hard


game = TubeSorter(matrix = Ex_tubes.t_4x6_easy)
game = TubeSorter(matrix = Ex_tubes.t_4x14_hard)
game.tubes
game.start
game.tops
game.cols
game.movelog

game.Sorter()

game.move_top(t1=0,t2=13)
game.reset_tubes()
game.reset




                # Random
                #   Combo of patterns and rando, with logic to not retrace to inf loop
                # Patterns
                #   Starts:
                #       Has most on tops, move them to one of opens
                #   Middle:
                #       3 in a row, 1 on top off, 4th is available, move top 1 off, complete
                #       Tube partial but all one color and finishing color available