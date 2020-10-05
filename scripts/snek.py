import random
import curses
from time import sleep


DELAY = .075
SNEK_SIZE = 8

EMPTY_COLOR = 1
BORDER_COLOR = 2
SNAKE_COLOR = 3
FOOD_COLOR = 4


# https://gist.github.com/claymcleod/b670285f334acd56ad1c#file-pycurses-py-L69
def draw_menu(stdscr):
    height, width = stdscr.getmaxyx()
    # declare strings
    title = "  Snake  "
#    subtitle = "move using arrow keys"[:width-1]
    statusbarstr = "  Exit : q  "
    # centering calculations
    start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
#   start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
    start_y = height // 2

    # render status bar
    stdscr.attron(curses.color_pair(BORDER_COLOR))
    stdscr.addstr(height-1, (width - len(statusbarstr) - 2), statusbarstr)
    # render title
    stdscr.attron(curses.A_BOLD)
    stdscr.addstr(0, start_x_title, title)
    stdscr.attroff(curses.A_BOLD)
    stdscr.attroff(curses.color_pair(BORDER_COLOR))


# paint 2x1 block at x,y color pair c
def paint(stdscr, x, y, c):
    stdscr.attron(curses.color_pair(c))
    stdscr.addstr(y, x, ' ')
    stdscr.addstr(y, x-1, ' ')
    stdscr.attroff(curses.color_pair(c))


def slither(stdscr, lst, k):
    height, width = stdscr.getmaxyx()
    height -= 1
    width -= width % 2

    head_x, head_y = lst[0]

    # paint over old head
    paint(stdscr, head_x, head_y, SNAKE_COLOR)

    # move
    if k == curses.KEY_DOWN or k == ord('s'):
        head_y += 1
    elif k == curses.KEY_UP or k == ord('w'):
        head_y -= 1
    elif k == curses.KEY_RIGHT or k == ord('d'):
        head_x += 2
    elif k == curses.KEY_LEFT or k == ord('a'):
        head_x -= 2

    # loop board
    thresh_x, thresh_y = 2, 1
    head_x = (head_x % width) if head_x >= thresh_x else (width - thresh_x)
    head_x = max(thresh_x, head_x)
    head_y = (head_y % height) if head_y >= thresh_y else (height - thresh_y)
    head_y = max(thresh_y, head_y)

    # if biting itself then game over
    if (head_x, head_y) in lst[2:]:
        return False

    # insert new head
    lst.insert(0, (head_x, head_y))
    # remove tail
    x2, y2 = lst.pop()

    # draw head
    paint(stdscr, head_x, head_y, SNAKE_COLOR)
    # erase tail
    paint(stdscr, x2, y2, EMPTY_COLOR)

    return True


def genFood(stdscr, lst):
    if not lst:
        return

    height, width = stdscr.getmaxyx()
    height -= height % 2
    width -= width % 2

    def first(t): return t[0]
    def second(t): return t[1]

    food_x = random.choice(
        [i for i in range(4, width-2, 2) if i not in list(map(first, lst))])
    food_y = random.choice(
        [i for i in range(2, height-1) if i not in list(map(second, lst))])

    # draw food
    paint(stdscr, food_x, food_y, FOOD_COLOR)

    return (food_x, food_y)


def start_color():
    curses.start_color()
    curses.init_pair(SNAKE_COLOR, curses.COLOR_GREEN, curses.COLOR_GREEN)  # body
    curses.init_pair(FOOD_COLOR, curses.COLOR_RED, curses.COLOR_RED)  # food
    curses.init_pair(EMPTY_COLOR, curses.COLOR_BLACK, curses.COLOR_BLACK)  # empty space
    curses.init_pair(BORDER_COLOR, curses.COLOR_WHITE, curses.COLOR_BLACK)  # status bar


def main(stdscr):
    height, width = stdscr.getmaxyx()

    start_color()

    # controls
    opposites = {
        curses.KEY_DOWN: curses.KEY_UP,
        curses.KEY_UP: curses.KEY_DOWN,
        curses.KEY_RIGHT: curses.KEY_LEFT,
        curses.KEY_LEFT: curses.KEY_RIGHT,
        ord('s'): ord('w'),
        ord('w'): ord('s'),
        ord('d'): ord('a'),
        ord('a'): ord('d')
    }

    def print_score(score):
        height, width = stdscr.getmaxyx()
        score_str = str(score)
        score_str = "  %s  " % score_str.zfill(4)
        stdscr.attron(curses.color_pair(BORDER_COLOR))
        stdscr.addstr(0, (width - len(score_str) - 2), score_str)
        stdscr.attroff(curses.color_pair(BORDER_COLOR))

    # default direction
    k = curses.KEY_LEFT

    while k != ord('q'):
        score = 0
        k = curses.KEY_LEFT

        # init snek
        head_x, head_y = width // 2, height // 2
        snek = [(x, head_y) for x in range(head_x, head_x + 2 * SNEK_SIZE, 2)]

        # clear screen
        stdscr.clear()
        # draw borders
        stdscr.attron(curses.color_pair(BORDER_COLOR))
        stdscr.border()
        stdscr.attroff(curses.color_pair(BORDER_COLOR))
        # draw menu
        draw_menu(stdscr)
        # print score
        print_score(score)
        # init food
        food = genFood(stdscr, snek)
        # draw snek
        for x, y in snek[1:]:
            paint(stdscr, x, y, SNAKE_COLOR)
        paint(stdscr, head_x, head_y, SNAKE_COLOR)
        # move cursor
        stdscr.move(food[1], food[0])
        # refresh screen
        stdscr.refresh()

        # wait for input
        stdscr.nodelay(0)
        inp = stdscr.getch()
        # disable waiting for input
        stdscr.nodelay(1)
        if inp == ord('q'):
            k = inp

        # loop
        while k != ord('q') and slither(stdscr, snek, k):

            # get user input
            inp = stdscr.getch()
            # set direction
            if (inp > 0 and inp != k and
                    (inp == ord('q') or
                     (inp in opposites and inp != opposites[k]))):
                k = inp

            # if eat food
            head = snek[0]
            if head[1] == food[1] and abs(head[0]-food[0]) <= 1:
                # grow
                snek.append(snek[-1])
                snek.append(snek[-1])
                snek.append(snek[-1])
                # update score
                score += 1
                print_score(score)
                # generate new food
                food = genFood(stdscr, snek)

            # move cursor
            # stdscr.move(food[1], food[0])
            stdscr.move(height-1, 0)
            # refresh screen
            stdscr.refresh()

            sleep(DELAY)


if __name__ == "__main__":
    curses.wrapper(main)
