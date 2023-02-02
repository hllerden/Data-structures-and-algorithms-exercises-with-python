import curses

def main(stdscr):
    curses.curs_set(False)
    curses.start_color()

    stdscr.addstr(0, 0, "A_BLINK", curses.A_BLINK)
    stdscr.addstr(1, 0, "A_BOLD", curses.A_BOLD)
    stdscr.addstr(2, 0, "A_STANDOUT", curses.A_STANDOUT)
    stdscr.addstr(3, 0, "A_UNDERLINE", curses.A_UNDERLINE)
    stdscr.addstr(4, 0, "A_DIM", curses.A_DIM)
    stdscr.addstr(5, 0, "A_INVIS", curses.A_INVIS)

    stdscr.addstr(6, 0, "BLINK | BOLD | UNDERLINE", curses.A_BLINK | curses.A_BOLD | curses.A_UNDERLINE)

    stdscr.refresh()
    stdscr.getkey()
    
curses.wrapper(main)