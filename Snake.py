import thumby
import time
import random

# fight mode where there is another snake and you need to hit it? either in head or in body
# and you cut it in 2 if hit in body

# BITMAP: width: 4, height: 4
snakeHeadMap = bytearray([14,7,7,4])

# thumby.display.width 72
# thumby.display.height 40

# bug - snake dies when in a line

BLACK = 0
WHITE = 1

BLOCK = 4

thumby.display.setFPS(60)

class State:
    def __init__(self):
        self.frame = 0
        self.frame_mod = 12 # speed; lower number is faster
        self.direction = "R"
        # prevent going back on self by hitting down then left quickly when going right
        self.previous_direction = "" 
        self.snake = Snake(36, 20)
        self.fruit = Fruit(52, 8)
        self.dead = False

class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.segments = [(self.x-BLOCK*2, self.y), (self.x-BLOCK, self.y), (self.x, self.y)]

class Fruit:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def get_random_coords():
    return (random.randrange(0, 72, BLOCK), random.randrange(0, 40, BLOCK))


state = State()

def display_start():
    thumby.display.fill(0)
    thumby.display.setFont("/lib/font8x8.bin", 8, 8, 0)
    text_width_placement = (thumby.display.width-(8*5))//2
    text_height_placement = (thumby.display.height-int(8/2))//2
    thumby.display.drawText("SNAKE", text_width_placement, text_height_placement, WHITE)
    thumby.display.update()
    time.sleep(1)

def display_end(state):
    time.sleep(1)
    thumby.display.fill(BLACK)
    thumby.display.setFont("/lib/font8x8.bin", 8, 8, 0)
    text_len = 8*(6+len(str(len(state.snake.segments))))
    text_height = 8//2
    text_width_placement = (thumby.display.width-text_len)//2
    text_height_placement = (thumby.display.height-text_height)//2
    thumby.display.drawText(f"SCORE {len(state.snake.segments)}", text_width_placement, text_height_placement, WHITE)
    thumby.display.update()
    time.sleep(4)
    thumby.reset()
    
        


def update(state):
    if thumby.buttonL.justPressed() and not state.previous_direction == "R":
        state.direction = "L"
    elif thumby.buttonR.justPressed() and not state.previous_direction == "L":
        state.direction = "R"
    elif thumby.buttonU.justPressed() and not state.previous_direction == "D":
        state.direction = "U"
    elif thumby.buttonD.justPressed() and not state.previous_direction == "U":
        state.direction = "D"
    
    elif thumby.buttonA.justPressed():
        state.dead = True
    
    
    # state.frame_mod goes from 12 -> 8, lower = faster
    if state.frame % state.frame_mod == 0:
        state.previous_direction = state.direction
        new_segment = state.snake.segments[0] # only needed if snake eats fruit
        
        # copy each segment to the one in front of it
        # for i in range(len(state.snake.segments)-1):
            # state.snake.segments[i] = state.snake.segments[i+1]
        
        head = state.snake.segments[-1] # define head
        
        # move head
        if state.direction == "R":
            new_head = (head[0]+BLOCK, head[1])
        elif state.direction == "L":
            new_head = (head[0]-BLOCK, head[1])
        elif state.direction == "U":
            new_head = (head[0], head[1]-BLOCK)
        elif state.direction == "D":
            new_head = (head[0], head[1]+BLOCK)
            
        # end game if head hits body
        if (new_head[0], new_head[1]) in state.snake.segments[1:-1]:
            state.dead = True
            return
        else:
            # cut off tail
            state.snake.segments = state.snake.segments[1:]
            
            # append if cutting off tail
            state.snake.segments.append((new_head[0]%thumby.display.width, new_head[1]%thumby.display.height))
        
        # eat fruit, add to snake, add new fruit
        if (new_head[0], new_head[1]) == (state.fruit.x, state.fruit.y):
            state.snake.segments.insert(0, new_segment)
            
            (new_fruit_x, new_fruit_y) = get_random_coords()
            # new_fruit_x = random.randrange(0, 72, 2)
            # new_fruit_y = random.randrange(0, 40, 2)
            while (new_fruit_x, new_fruit_y) in state.snake.segments:
                (new_fruit_x, new_fruit_y) = get_random_coords()
            state.fruit = Fruit(new_fruit_x, new_fruit_y)

            
            # speed up as snake gets bigger
            if state.frame_mod > 8 and len(state.snake.segments) % 6 == 0:
                state.frame_mod -= 1
        
        



def render(state):
    empty_color = BLACK
    fill_color = WHITE
    if state.dead == True:
        empty_color = WHITE
        fill_color = BLACK
        
    thumby.display.fill(empty_color)
    head = state.snake.segments[-1]
    # (width, height, bitmapData, x, y, key, mirrorX, mirrorY)
    snakeHeadSprite = thumby.Sprite(BLOCK, BLOCK, snakeHeadMap, head[0], head[1], empty_color)
    
    thumby.display.drawSprite(snakeHeadSprite)
    for s in state.snake.segments[:-1]:
        thumby.display.drawFilledRectangle(s[0], s[1], BLOCK, BLOCK, fill_color)
    thumby.display.drawRectangle(state.fruit.x, state.fruit.y, BLOCK, BLOCK, fill_color)
    thumby.display.update()

display_start()

while True:
    if state.dead == False:
        update(state)
        render(state)
        state.frame += 1
    else:
        time.sleep(1)
        break

display_end(state)

