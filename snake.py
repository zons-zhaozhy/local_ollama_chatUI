import random
import time
import curses

# 初始化屏幕
stdscr = curses.initscr()
curses.curs_set(0)
sh, sw = stdscr.getmaxyx()
window = curses.newwin(sh, sw, 0, 0)
window.keypad(1)
window.timeout(100)

# 定义贪吃蛇的初始位置和长度
snake_x = sw//4
snake_y = sh//4
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x-1],
    [snake_y, snake_x-2]
]

# 初始化食物的位置
food = None
while food is None:
    new_food = [
        random.randint(1, sh-1),
        random.randint(1, sw-1)
    ]
    if new_food not in snake:
        food = new_food

# 定义游戏结束标志
game_over = False

# 定义按键映射
key = curses.KEY_RIGHT

while not game_over:
    window.clear()
    
    # 绘制贪吃蛇
    for i, (y, x) in enumerate(snake):
        if i == 0:
            window.addch(y, x, curses.ACS_CKBOARD)  # 头部
        else:
            window.addch(y, x, 'o')  # 身体
    
    # 绘制食物
    window.addch(food[0], food[1], '*')
    
    # 读取按键输入
    next_key = window.getch()
    if next_key == -1:
        key = key
    else:
        key = next_key
    
    # 根据按键移动贪吃蛇
    y, x = snake[0]
    if key == curses.KEY_DOWN:
        new_head = [y + 1, x]
    elif key == curses.KEY_UP:
        new_head = [y - 1, x]
    elif key == curses.KEY_LEFT:
        new_head = [y, x - 1]
    elif key == curses.KEY_RIGHT:
        new_head = [y, x + 1]
    
    # 检查是否碰撞到边界或自身
    if (new_head[0] in [0, sh] or new_head[1] in [0, sw] or new_head in snake):
        game_over = True
    else:
        snake.insert(0, new_head)  # 添加新头部
        
        # 检查是否吃到食物
        if snake[0] == food:
            food = None
            while food is None:
                nf = [
                    random.randint(1, sh-1),
                    random.randint(1, sw-1)
                ]
                if nf not in snake:
                    food = nf
        else:
            tail = snake.pop()  # 移除尾部
    
    # 刷新屏幕
    window.addch(tail[0], tail[1], ' ')  # 清除尾巴
    
    if game_over:
        stdscr.clear()
        stdscr.addstr(sh//2, sw//2 - len("Game Over!"), "Game Over!")
        stdscr.refresh()
        time.sleep(3)
        break

# 结束游戏并重置屏幕
curses.endwin()