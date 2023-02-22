


class TubeStatus:

    def __init__(self, matrix):
        self.heigth = len(matrix[0])
        self.width = len(matrix)
        self.tubes = self.start_removeZero(m = matrix)        # Will alter
        self.start = self.start_removeZero(m = list(matrix))  # Wont alter
        self.balls = self.ball_unique()
        self.movelog = []
        self.tops = self.tubes_tops()
        self.cols = self.tubes_avail()

    def start_removeZero(self, m):
        for i in range(self.width):
            if self.start_tubenum(m[i]) < self.heigth:
                m[i] = [z for z in m[i] if z != 0]
        return m

    def start_tubenum(self, t):      # Return # balls
        return sum(map(lambda x : x != 0, t))   #used to remove zero, so not blank yet

    def tube_check(self, tn):    # Check if tube good, all match or empty
        if self.tubes[tn] == []:
            return True
        elif len(self.tubes[tn]) == self.heigth: # Full tube to all match
            return all(elem == self.tubes[tn][0] for elem in self.tubes[tn])
        else:
            False

    def tubes_check(self):      # Check all tubes
        for t in range(self.width):
            if not self.tube_check(tn = t):     # if one tube fails, False
                return False
        return True
    

    def tubes_avail(self):
        avail = []
        for i in range(self.width):
            if self.tubes[i] == []:
                avail.append(i)
            elif not self.tube_check(tn = i):
                avail.append(i)
        return avail

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
        if len(tube2) == 4:      #full tube
            return False
        elif tube2[0] == 0 :               #empty tube
            return True
        elif self.tube_top(tube1) == self.tube_top(tube2):  #tops match
            return True
        return False

    def tubes_tops(self):
        tops = []
        for i in range(self.width):
            if len(self.tubes[i]) > 0:
                ball = self.tubes[i][-1]
                num = 0
                for b in reversed(self.tubes[i]):
                    if b == ball:
                        num += 1
                    else:
                        break
                avl = self.heigth - len(self.tubes[i])
                tops.append([ball,num,avl])   
            else:
                tops.append([0,4,4]) # Empty Row
        return tops        


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


    # def solve_check(self):           # Check solvable still or solved
    #     """
        
    #     """
    #     if self.tubes_check():
    #         # all(self.tube_check(t = elem) for elem in self.tubes): #solved
    #         return True
    #     return False

