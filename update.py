#!/bin/python

import random

class Matrix(object):
    def __init__(self):
        '''
        Unfortunately shortening this to something like 5*[5*[0]] 
        doesn't really work because you end up with 5 copies of the same list, 
        so when you modify one of them they all change"
        '''
        self.matrix = [[0]*4 for i in range(4)]

    def gen_new_two(self):
        done = False
        while(not done):
            gen_i = random.randint(0,3)
            gen_j = random.randint(0,3)
            if(self.matrix[gen_i][gen_j] == 0):
                self.matrix[gen_i][gen_j] = 2
                done = True

    ''' This function updates the empty region'''
    def lefty_update(self):
        new_matrix = [[0]*4 for i in range(4)]
        for i in range(4):
            update_loc = 0
            for j in range(4):
                if(self.matrix[i][j] != 0):
                    new_matrix[i][update_loc] = self.matrix[i][j]
                    update_loc += 1
        
        self.matrix = new_matrix

    def transpose(self):
        for i in range(4):
            for j in range(i+1):
                self.matrix[i][j], self.matrix[j][i] = self.matrix[j][i], self.matrix[i][j]
        for i in range(4):
            for j in range(2):
                self.matrix[i][j], self.matrix[i][3-j] = self.matrix[i][3-j], self.matrix[i][j]
    
    def reverse(self):
        for i in range(2):
            for j in range(4):
                self.matrix[i][j], self.matrix[3-i][j] = self.matrix[3-i][i], self.matrix[i][j]

    def merge(self):
        for i in range(4):
            for j in range(3):
                if(self.matrix[i][j] == self.matrix[i][j+1]):
                    self.matrix[i][j] *= 2
                    self.matrix[i][j+1] = 0
    
    def move_left(self):
        ## all moving left firstly
        self.lefty_update()
        ## merge
        self.merge()
        self.lefty_update()
        self.gen_new_two()

    def move_right(self):
        self.transpose()
        self.transpose()
        self.move_left()
        self.transpose()
        self.transpose()

    def move_up(self):
        self.transpose()
        self.transpose()
        self.transpose()
        self.move_left()
        self.transpose()

    def move_down(self):
        self.transpose()
        self.move_left()
        self.transpose()
        self.transpose()
        self.transpose()

    def print_matrix(self):
        for i in range(4):
            print(self.matrix[i])
    
    def self_test(self):
        move_func = [self.move_up, self.move_down, self.move_left, self.move_right]
        move_str=["UP", "DOWN", "LEFT", "RIGHT"]
        while(True):
            direction = random.randint(0,3)
            move_func[direction]()
            print(move_str[direction])
            self.print_matrix()
            input()
