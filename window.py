from tkinter import *
import update

SIZE = 720
GRID_LEN = 4
GRID_PADDING = 10

BACKGROUND_COLOR_GAME = "#92877d"
BACKGROUND_COLOR_CELL_EMPTY = "#9e948a"
BACKGROUND_COLOR_DICT = { 2: "#eee4da", 4: "#ede0c8", 8: "#f2b179", 16: "#f59563",
                         32: "#f67c5f", 64: "#f65e3b", 128: "#edcf72", 256: "#edcc61",
                        512: "#edc850", 1024: "#edc53f", 2048: "#edc22e"}
CELL_COLOR_DICT = {2: "#776e65", 4: "#776e65", 8: "#f9f6f2", 16: "#f9f6f2",
                   32: "#f9f6f2", 64: "#f9f6f2", 128: "#f9f6f2", 256: "#f9f6f2",
                   512: "#f9f6f2", 1024: "#f9f6f2", 2048: "#f9f6f2"}
FONT = ("Verdana", 40, "bold")

class Window(Frame):
    '''
    Window class for Tk
    '''
    def __init__(self, master=None):

        ## Parent class initalization

        super(Window, self).__init__(master, height=SIZE, width=SIZE, bg=BACKGROUND_COLOR_GAME)
        self.grid()
        self.propagate(False)
        # self.frame = Frame(master, height=SIZE, width=SIZE,
        #                    bg=BACKGROUND_COLOR_GAME)
        # self.frame.grid()
        # self.master = master
        
        ## bind keys
        self.master.bind("<Left>", self.move_left)
        self.master.bind("<Right>", self.move_right)
        self.master.bind("<Up>", self.move_up)
        self.master.bind("<Down>", self.move_down)

        ## record each label of cell
        self.cell = []

        self.init_grid()
        self.init_matrix()
        self.update_matrix_cell()

        ## run the mainloop
        self.master.mainloop()

    def init_grid(self):
        for i in range(4):
            tmp_cell_list = []
            for j in range(4):
                one_grid = Frame(self, width=SIZE/GRID_LEN, height=SIZE/GRID_LEN)
                one_grid.grid(row=i, column=j, padx=GRID_PADDING, pady=GRID_PADDING)
                one_grid.propagate(False)

                label = Label(one_grid, text="", font=FONT, justify=CENTER, bg=BACKGROUND_COLOR_CELL_EMPTY)
                label.grid()
                tmp_cell_list.append(label)

            self.cell.append(tmp_cell_list)

    def init_matrix(self):
        self.Matrix = update.Matrix()
        self.Matrix.gen_new_two()

    def update_matrix_cell(self):
        for i in range(4):
            for j in range(4):
                if(self.Matrix.matrix[i][j] == 0):
                    self.cell[i][j].configure(text="", bg=BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.cell[i][j].configure(text=str(self.Matrix.matrix[i][j]), 
                                              bg=BACKGROUND_COLOR_DICT[self.Matrix.matrix[i][j]],
                                              fg=CELL_COLOR_DICT[self.Matrix.matrix[i][j]])
        self.master.update_idletasks()

    def move_left(self, event):
        self.Matrix.move_left()
        self.update_matrix_cell()
    
    def move_right(self, event):
        self.Matrix.move_right()
        self.update_matrix_cell()
    
    def move_up(self, event):
        self.Matrix.move_up()
        self.update_matrix_cell()
    
    def move_down(self, event):
        self.Matrix.move_down()
        self.update_matrix_cell()

root = Tk()
# root.geometry("{}x{}".format(SIZE, SIZE))
# root.resizable(0, 0)

window = Window(root)

#root.mainloop()

# topFrame = Frame(root)
# topFrame.pack()
# bottomFrame = Frame(root)
# bottomFrame.pack(side=BOTTOM)

# botton1 = Button(topFrame, text="button 1"
# , fg="red", bg="white")
# botton2 = Button(topFrame, text="button 2", fg="blue")
# botton3 = Button(bottomFrame, text="button 3", fg="green")

## 2nd step, display widget
# botton1.pack(side=LEFT)
# botton2.pack(side=LEFT)
# botton3.pack()

# one = Label(root, text="one", bg="red", fg="white")
# two = Label(root, text="two", bg="green", fg="black")
# three = Label(root, text="Three", bg="blue", fg="white")

# one.pack()
# two.pack(fill=X)
# three.pack(side=LEFT, fill=Y)

# ---------------- Grid Layout ----------------
# label_1 = Label(root, text="Name")
# label_2 = Label(root, text="Password")
# entry_1 = Entry(root)
# entry_2 = Entry(root)

# label_1.grid(row=0, sticky=E)
# label_2.grid(row=1)

# entry_1.grid(row=0, column=1)
# entry_2.grid(row=1, column=1)

# c = Checkbutton(root, text="Keep me logged in")
# c.grid(columnspan=2)

# ----------------- Binding Functions to Layout -----------
# def printName(event):
#     print("My name is Chia-Hao")

# button_1 = Button(root, text="Print my name")
# button_1.bind("<Button-1>", printName)
# button_1.pack()


