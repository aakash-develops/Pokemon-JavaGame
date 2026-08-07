from typing import get_overloads


def gameover():
    from kolyre import Kolyre
    Kolyre.enable_ansi_support()
    import time, sys
    game = """
 ██████╗  █████╗ ███╗   ███╗███████╗
██╔════╝ ██╔══██╗████╗ ████║██╔════╝
██║  ███╗███████║██╔████╔██║█████╗  
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝

                                     """
    over = """
 ██████╗ ██╗   ██╗███████╗██████╗ 
██╔═══██╗██║   ██║██╔════╝██╔══██╗
██║   ██║██║   ██║█████╗  ██████╔╝
██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
 ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
                                                 """
    icon = """
⢰⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀
⠀⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣾⣿
⠀⠘⢿⣿⣿⣿⣿⣦⣀⣀⣀⣄⣀⣀⣠⣀⣤⣶⣿⣿⣿⣿⣿⠇
⠀⠀⠈⠻⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀
⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠋⠀⠀⠀
⠀⠀⠀⢠⣿⣿⡏⠆⢹⣿⣿⣿⣿⣿⣿⠒⠈⣿⣿⣿⣇⠀⠀⠀
⠀⠀⠀⣼⣿⣿⣷⣶⣿⣿⣛⣻⣿⣿⣿⣶⣾⣿⣿⣿⣿⡀⠀⠀
⠀⠀⠀⡁⠀⠈⣿⣿⣿⣿⢟⣛⡻⣿⣿⣿⣟⠀⠀⠈⣿⡇⠀⠀
⠀⠀⠀⢿⣶⣿⣿⣿⣿⣿⡻⣿⡿⣿⣿⣿⣿⣶⣶⣾⣿⣿⠀⠀
⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀
⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀
    """

    esc = "\x1b"

    def clear():
        sys.stdout.write(f'{esc}[2J')

    def goto(r, c):
        sys.stdout.write(f"{esc}[{r};{c}H")

    def draw_art(r, c, text):
        line = text.strip("\n").splitlines()
        for k, l in enumerate(line):
            goto(r + k, c)
            sys.stdout.write(l)

    def color_split(ascii_art: str, split_rows: int, top=Kolyre.RED, bottom=Kolyre.foreground_256(15)):
        raw_lines = ascii_art.splitlines()
        # Find the real text
        start = 0
        end = len(raw_lines) - 1
        while start < len(raw_lines) and raw_lines[start] == "":
            start += 1
        while end >= 0 and raw_lines[end] == "":
            end -= 1
        # return print(start),print(end)
        text = []
        index_ascii = -1
        for i, line in enumerate(raw_lines):
            if start <= i <= end:
                index_ascii += 1
                paint = top if index_ascii <= split_rows else bottom
            else:
                paint = top
            text.append(f"{paint}{line}{Kolyre.RESET}")

        return "\n".join(text)

    clear()

    # draw_art(10,40,color_split(poke,3))
    def animation(game_xy, over_xy, icon_xy):
        game_fixed = False
        over_fixed = False
        icon_fixed = False
        game_col = 0
        over_row = 0
        icon_col = 130
        while not game_fixed:
            clear()
            game_col += 2
            draw_art(game_xy[0], game_col, color_split(game, 2))
            sys.stdout.flush()
            time.sleep(0.01)
            if game_col >= game_xy[1]:
                game_col = game_xy[1]
                game_fixed = True
        while not over_fixed:
            clear()
            draw_art(game_xy[0], game_xy[1], color_split(game, 2))
            # draw_art(icon_xy[0],icon_xy[1],color_split(icon,4))
            over_row += 1
            draw_art(over_row, over_xy[1], color_split(over, 2))

            sys.stdout.flush()
            time.sleep(0.01)
            sys.stdout.write(f'{esc}[?25l')

            if over_row >= over_xy[0]:
                over_row = over_xy[0]
                over_fixed = True
        while not icon_fixed:
            clear()
            draw_art(game_xy[0], game_xy[1], color_split(game, 2))
            draw_art(over_row, over_xy[1], color_split(over, 2))

            icon_col -= 7
            draw_art(icon_xy[0], icon_col, f"{Kolyre.BOLD}{icon}{Kolyre.RESET}")
            sys.stdout.flush()
            time.sleep(0.01)
            sys.stdout.write(f'{esc}[?25l')

            if icon_col <= icon_xy[1]:
                icon_col = icon_xy[1]
                icon_fixed = True

    # lm = 0
    # while lm != 5:
    #     lm=+1
    animation([10, 20], [10, 60], [5, 100])

