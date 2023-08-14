import thumby
import random
import time

# easy 10 mine 10x10, (9+)1 extra x, (5+)5 extra y
# medium 40 mine 16×16
# hard 99 mine 30×16

# focus on getting 10x10 to work to see the speed differences from Bigsweeper.py
# remove start and set 10 mines to default


thumby.display.setFPS(60)

# BITMAP: width: 8, height: 8
flagMap = bytearray([0,136,140,158,255,128,128,0])
mineMap = bytearray([231,195,129,0,0,129,195,231])
# BITMAP: width: 24, height: 24
sunglassMap = bytearray([0,0,192,112,56,28,14,135,129,129,129,129,129,129,129,131,134,12,24,48,96,192,0,0,
           14,63,255,226,3,1,1,7,15,15,15,128,128,131,135,15,15,15,1,129,195,127,62,24,
           0,0,1,3,15,30,120,240,196,140,152,177,177,177,152,140,224,124,31,3,0,0,0,0])
# BITMAP: width: 144, height: 80
explosionMap = bytearray([255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,
          255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,127,23,199,207,223,127,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,
          255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,31,127,87,207,199,63,255,255,255,255,255,255,255,255,255,191,207,167,250,220,254,255,255,255,254,233,249,187,31,127,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,127,191,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,
          255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,127,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,127,127,124,9,132,247,251,63,50,223,127,255,95,191,223,227,248,252,255,255,191,191,47,39,3,147,19,7,63,179,247,254,252,247,191,127,255,255,255,127,255,255,223,63,239,207,239,255,219,189,157,205,230,251,252,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,
          255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,254,254,251,255,255,255,254,239,251,67,222,238,63,30,62,190,254,247,254,254,254,236,226,210,134,31,119,34,33,15,15,191,24,64,1,0,65,79,7,151,207,167,81,41,17,9,128,126,166,33,81,129,47,176,227,99,79,95,255,191,190,191,204,14,143,7,199,192,241,255,255,199,241,127,252,127,127,127,255,127,127,255,127,127,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,
          255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,251,251,249,251,255,255,239,239,255,94,190,252,252,120,48,0,0,129,128,128,130,136,0,0,48,216,228,131,240,101,178,80,28,193,198,83,82,144,128,99,6,72,31,169,9,228,192,141,14,7,47,15,15,15,6,14,143,142,159,79,63,190,253,188,156,188,253,254,126,125,60,204,156,175,198,242,253,253,253,255,255,231,255,239,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,
          255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,223,111,209,253,243,253,167,50,120,52,56,189,142,230,255,87,7,255,255,254,254,52,97,1,23,69,69,98,30,137,165,130,5,14,135,6,0,0,24,6,5,0,128,200,224,192,200,142,55,127,180,177,113,115,115,243,223,247,217,89,201,237,254,95,126,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,
          255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,191,247,63,114,237,237,223,239,255,253,250,253,255,254,254,255,255,255,255,255,254,158,139,255,255,255,198,0,65,128,164,178,151,158,237,231,3,255,191,240,248,196,81,252,240,254,191,143,199,166,249,239,247,191,154,182,255,255,255,127,167,243,251,251,231,206,223,223,190,191,116,247,103,207,167,239,255,127,255,127,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,
          255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,254,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,223,191,131,126,187,63,27,215,255,244,252,255,255,255,255,255,255,253,65,15,239,255,63,15,187,219,253,248,254,255,255,255,255,255,255,254,251,247,240,193,242,255,255,255,255,255,255,255,255,255,255,255,255,255,254,254,254,255,254,253,251,231,225,251,255,175,95,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,
          255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,251,249,255,255,59,255,255,255,255,255,255,255,255,255,255,255,255,254,254,254,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255])
        
x_max = 10
y_max = 10
num_mines = 10

def get_random_coords():
    return (random.randrange(0, x_max*8, 8), random.randrange(0, y_max*8, 8))


class Square:
    def __init__(self, x=random.randrange(0, 64, 8), y=random.randrange(0, 32, 8)): 
        self.x = x
        self.y = y
        self.adj = 0 # adj to mines number
        self.mine = False
        self.flag = False
        self.visible = False
    
    def get_adjacent(self, state, exclude=None):
        all_adjacent = []
        for j in [-8, 0, 8]:
            for i in [-8, 0, 8]:
                if i == 0 and j == 0:
                    pass
                elif 0 <= self.x+i < x_max*8 and 0 <= self.y+j < y_max*8:
                    all_adjacent.append(state.board[(self.x+i, self.y+j)])
        
        for adj in all_adjacent:
            if exclude == "mine" and adj.mine == True:
                    all_adjacent.remove(adj)
        
        return all_adjacent
        
    

# ideas to clean up vars in state:
#   can get high_bound from low_bound and vice-versa, so don't all need to have their own variables
class State:
    def __init__(self):
        self.win = False
        self.lose = False
        self.cursor = Square() # cursor starting at random location for flavor
        self.previous_cursor = None
        self.x_offset = 0
        self.y_offset = 0
        self.x_high_bound = 64
        self.x_low_bound = 0
        self.y_high_bound = 32
        self.y_low_bound = 0
        self.flags = set()
        self.mines = set()
        self.adjacent_to_mines = set()
        self.board = None
        self.display_squares = {}
        self.render = True # render() will only run if true to save resources
        self.counter = 0
        



def create_board(state, fixed_mines=False):
    thumby.display.fill(0)
    
    state.board = {(x, y): Square(x, y) for y in range(0, y_max*8, 8) for x in range(0, x_max*8, 8)}
    state.display_squares = {(x, y): state.board[x, y] for y in range(state.y_low_bound, state.y_high_bound+1, 8) for x in range(state.x_low_bound, state.x_high_bound+1, 8)}  

    # fixed_mines mines for debugging
    if fixed_mines == True:
        mines = [(8, 0), (48, 0), (16, 8), (0, 24), (56, 24), (24, 32), (72, 32), (0, 40), (16, 40), (16, 56)]
        for mine in mines:
            state.board[(mine)].mine = True
    # random mines
    else:
        mines = []
        while len(mines)<num_mines:
            mine = get_random_coords()
            mines.append(mine)
            state.board[(mine)].mine = True
            state.mines.add(state.board[(mine)])
    
    # calc adj to mines
    for mine in state.mines:
        # print((mine.x, mine.y)) # for debugging
        all_adjacent = mine.get_adjacent(state, exclude="mine")
        for adj in all_adjacent:
            adj.adj += 1

def display_start(state):
    thumby.display.fill(0)
    thumby.display.setFont("/lib/font8x8.bin", 8, 8, 0)
    thumby.display.drawText("Mineswepr", 0, ((thumby.display.height//2)-3)//2, 1)
    thumby.display.setFont("/lib/font5x7.bin", 5, 7, 0)
    thumby.display.drawText(f"Find {num_mines} mines", 4, (3*thumby.display.height//4-4), 1)
    thumby.display.update()
    time.sleep(1.5)
    

def display_win():
    time.sleep(1)
    thumby.display.fill(0)
    thumby.display.drawSprite(thumby.Sprite(24, 24, sunglassMap, thumby.display.width//2-12, thumby.display.height//2-12, 0))
    thumby.display.update()
    

def display_lose(state):
    for flag in state.flags:
        if flag not in state.mines and flag in state.display_squares.values(): # x over flagged squares that aren't mines
            flag.x -= state.x_offset
            flag.y -= state.y_offset
            thumby.display.drawLine(flag.x, flag.y, flag.x+8, flag.y+8, 1)
            thumby.display.drawLine(flag.x+8, flag.y, flag.x, flag.y+8, 1)
    for mine in state.mines:
        if mine not in state.flags and mine in state.display_squares.values(): # display all mines not flagged
            thumby.display.drawSprite(thumby.Sprite(8, 8, mineMap, mine.x - state.x_offset, mine.y - state.y_offset, 0))
    thumby.display.update()
    time.sleep(.5)
    
    for i in range(3): # flashes squares with mines
        thumby.display.drawFilledRectangle(state.cursor.x - state.x_offset, state.cursor.y - state.y_offset, 8, 8, 1)
        thumby.display.update()
        time.sleep(.2)
        thumby.display.drawSprite(thumby.Sprite(8, 8, mineMap, state.cursor.x - state.x_offset, state.cursor.y - state.y_offset, 1))
        thumby.display.update()
        time.sleep(.2)
    time.sleep(.5)
    
    thumby.display.fill(0) # display boom
    thumby.display.drawSprite(thumby.Sprite(144, 80, explosionMap, 0, 0, 0))
    thumby.display.setFont("/lib/font8x8.bin", 8, 8, 0)
    thumby.display.drawText("boom", 8, 8, 0)
    thumby.display.update()
    

# if you make a visible set() could more quickly find visible squares, much smaller for loop
def reveal(state, selection):
    try:
        selection.visible = True # makes selection visible
        all_adjacent = selection.get_adjacent(state) # gets all adjacent to square 
        for adj in all_adjacent:
            if adj.flag == True: # skips flags and acts as block
                pass
            elif adj.adj == 0 and adj.visible == False: # reveal empty squares that are not visible yet
                reveal(state, adj)
            elif adj.adj != 0: # number so should be visible no matter what
                adj.visible = True

    except RuntimeError:
        reveal(state, adj)
        
def render_cursor(state):
    # reset cursor via setting previous_cursor pixels to black
    if state.previous_cursor != None:
        previous_cursor_x = state.previous_cursor.x - state.x_offset
        previous_cursor_y = state.previous_cursor.y - state.y_offset
        for i in range(3):
            thumby.display.setPixel(previous_cursor_x+7, previous_cursor_y+i, 0)
            thumby.display.setPixel(previous_cursor_x, previous_cursor_y+i, 0)
        for i in range(5, 9):
            thumby.display.setPixel(previous_cursor_x+7, previous_cursor_y+i, 0)
            thumby.display.setPixel(previous_cursor_x, previous_cursor_y+i, 0)
        for i in range(2):
            thumby.display.setPixel(previous_cursor_x+i, previous_cursor_y, 0)
            thumby.display.setPixel(previous_cursor_x+i, previous_cursor_y+7, 0)
        for i in range(6, 9):
            thumby.display.setPixel(previous_cursor_x+i, previous_cursor_y, 0)
            thumby.display.setPixel(previous_cursor_x+i, previous_cursor_y+7, 0)
            
    
    display_cursor_x = state.cursor.x - state.x_offset
    display_cursor_y = state.cursor.y - state.y_offset

    # turn cursor black when it's over a scroll bar
    # draw new cursor
    thumby.display.drawRectangle(display_cursor_x, display_cursor_y, 8, 8, 1)
    for i in range(3, 5):
        thumby.display.setPixel(display_cursor_x+7, display_cursor_y+i, 0)
        thumby.display.setPixel(display_cursor_x, display_cursor_y+i, 0)
    for i in range(2, 6):
        thumby.display.setPixel(display_cursor_x+i, display_cursor_y, 0)
        thumby.display.setPixel(display_cursor_x+i, display_cursor_y+7, 0)

        
def render_scrollbar(state):
    # reset scrollbars
    thumby.display.drawLine(0, 39, 71, 39, 0)
    thumby.display.drawLine(71, 0, 71, 39, 0)
    # scroll correction so it reaches the end of the screen. need to adjust so it moves smoothly
    
    num_x_offsets = 2 # (x_max-9)+1
    horiz_scroll_len = 72//num_x_offsets
    x1 = horiz_scroll_len*(state.x_offset//8)
    x2 = x1 + horiz_scroll_len
    
    if 72 % num_x_offsets != 0:
        for i in range(72%num_x_offsets):
            if x2 > 72//3:
                x1 += 1
                x2 += 1
        thumby.display.drawLine(x1, 39, x2, 39, 1)
    else:
        thumby.display.drawLine(x1, 39, x2, 39, 1)
    
    
    num_y_offsets = 6 # (y_max-5)+1
    vert_scroll_len = 40//num_y_offsets
    y1 = vert_scroll_len*(state.y_offset//8)
    y2 = y1 + vert_scroll_len
    
    if 40 % num_y_offsets != 0:
        for i in range(40%num_y_offsets):
            if y2 > 40//3:
                y1 += 1
                y2 += 1
        thumby.display.drawLine(71, y1, 71, y2, 1)
    else:
        thumby.display.drawLine(71, y1, 71, y2, 1)


def update(state):
    # instead of creating new display_squares from scratch every time, could remove one row and add new row depending on offset
    state.previous_cursor = Square(state.cursor.x, state.cursor.y)
    state.render = False # True if button is pressed to change screen
    
    
    if thumby.buttonL.justPressed() and state.cursor.x > 0:
        state.cursor.x -= 8
        if state.cursor.x < state.x_low_bound:
            state.x_low_bound = state.cursor.x
            state.x_high_bound -= 8
            state.x_offset -= 8
            for y in range(state.y_low_bound, state.y_high_bound+1, 8):
                del state.display_squares[(state.x_high_bound+8, y)]
                state.display_squares[state.x_low_bound, y] = state.board[state.x_low_bound, y]
        state.render = True
    elif thumby.buttonR.justPressed() and state.cursor.x < (8*x_max-8):
        state.cursor.x += 8
        if state.cursor.x > state.x_high_bound:
            state.x_high_bound = state.cursor.x
            state.x_low_bound += 8
            state.x_offset += 8
            for y in range(state.y_low_bound, state.y_high_bound+1, 8):
                del state.display_squares[(state.x_low_bound-8, y)]
                state.display_squares[state.x_high_bound, y] = state.board[state.x_high_bound, y]
        state.render = True
    elif thumby.buttonU.justPressed() and state.cursor.y > 0:
        state.cursor.y -= 8
        if state.cursor.y < state.y_low_bound:
            state.y_low_bound = state.cursor.y
            state.y_high_bound -= 8
            state.y_offset -= 8
            for x in range(state.x_low_bound, state.x_high_bound+1, 8):
                del state.display_squares[(x, state.y_high_bound+8)]
                state.display_squares[(x, state.y_low_bound)] = state.board[x, state.y_low_bound]
        state.render = True
    elif thumby.buttonD.justPressed() and state.cursor.y < (8*y_max-8):
        state.cursor.y += 8
        if state.cursor.y > state.y_high_bound:
            state.y_high_bound = state.cursor.y
            state.y_low_bound += 8
            state.y_offset += 8
            for x in range(state.x_low_bound, state.x_high_bound+1, 8):
                del state.display_squares[(x, state.y_low_bound-8)]
                state.display_squares[(x, state.y_high_bound)] = state.board[x, state.y_high_bound]
        state.render = True
    
        
    # SELECTING USING A BUTTON
    if thumby.buttonA.justPressed():
        selection = state.board[(state.cursor.x, state.cursor.y)] # selection is a square
        if selection.flag == True:
            pass
        elif selection.mine == True:
            state.lose = True
        elif selection.adj != 0:
            selection.visible = True
        else:
            reveal(state, selection)
            
        # state.win = True if all non-mines are visible
        state.win = all(square.visible == True for square in state.board.values() if square.mine == False)
        state.render = True
    
    if thumby.buttonB.justPressed():
        selection = state.board[(state.cursor.x, state.cursor.y)]
        if selection.visible == True:
            return
        
        if selection.flag == True:
            selection.flag = False
        else:
            selection.flag = True
                    
        # creating set of flags squares, only runs if B is pressed
        state.flags = set(square for square in state.board.values() if square.flag == True)
        # check if set of flags = mines
        if state.flags == state.mines:
            if len(state.flags) > len(state.mines):
                state.too_many_flags = True
            else:
                state.win = True
        state.render = True
        
    
    if state.win == True:
        for mine in state.mines.difference(state.flags):
            mine.flag = True
            state.flags.add(mine)
    

# runs if to_render != set(), since only need to clear screen if adding multiple items
def render(state):
    # render cursor, scroll bar every time
    thumby.display.fill(0)
    render_cursor(state)
    render_scrollbar(state)
    
    if state.render == True:
        for square in state.display_squares.values():
            if square.visible == True:
                if square.adj > 0:
                    # filling in numbers; offset for x = 2, offset for y = 1
                    thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
                    thumby.display.drawText(str(square.adj), square.x+3 - state.x_offset, square.y+1 - state.y_offset, 1)
                elif square.adj == 0:
                    thumby.display.drawRectangle(square.x+3 - state.x_offset, square.y+3 - state.y_offset, 2, 2, 1)
            
            elif square.flag == True:
                thumby.display.drawSprite(thumby.Sprite(8, 8, flagMap, square.x - state.x_offset, square.y - state.y_offset, 0))
    
    thumby.display.update()


state = State()

display_start(state)
create_board(state)
render(state)

while state.win == False and state.lose == False:
    update(state)
    if state.render == True:
        render(state)
    if state.win == True:
        display_win()
    elif state.lose == True:
        display_lose(state)
    
time.sleep(3)
thumby.reset()

