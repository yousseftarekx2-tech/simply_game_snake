import random
import curses
screen=curses.initscr()
curses.curs_set(0)
screen_width , screen_higth=screen.getmaxyx()
window=curses.newwin(screen_higth , screen_width , 0 , 0)
window.keypad(1)
window.timeout(100)
snack_x=screen_width//4
snack_y=screen_higth//2
snack=[
    [snack_y , snack_x],
    [snack_y , snack_x-1],
    [snack_y , snack_x-2]
]
food=[screen_higth//2 , screen_width//2]
window.addch(food[0], food[1] , curses.ACS_PI)
key=curses.KEY_RIGHT
while True:
    next_key=window.getch()
    key=key if next_key == -1 else next_key
    if snack[0][0] in [0 , screen_higth] or snack[0][1] in [0 , screen_width] or snack[0] in snack[1:]:
        curses.endwin()
        quit()
        
    new_head =snack[0][0] ,  snack[0][1]
    if key== curses.KEY_DOWN:
        new_head[0]+=1
    if key == curses.KEY_UP:
        new_head-=1
    if key == curses.KEY_RIGHT:
        new_head+=1
    if key == curses.KEY_LEFT:
        new_head-=1
        
    snack.insert(0 , new_head)
    if snack[0]==food:
        food=None
        while food is None:
            new_food=[
                random.randint(1 , screen_higth-1),
                random.randint(1 , screen_width-1)
            ]
            food=new_food if new_food not in snack else None
        window.addch(food[0], food[1] , curses.ACS_PI)
    else:
        tail=snack.pop()
        window.addch(tail[0] , tail[1] , ' ')
    
    window.addch(snack[0][0] , curses.ACS_CKBOARD)