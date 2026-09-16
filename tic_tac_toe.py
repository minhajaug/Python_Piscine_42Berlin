#!/usr/bin/env python3

# ======================================================================
#  GRAPHICS
# ======================================================================

import os
import sys

# ANSI color codes (256-color palette)

PINK = "\033[38;5;213m"
LIME = "\033[38;5;155m"
PURPLE = "\033[38;5;183m"
DARK_GRAY = "\033[38;5;240m"
LIGHT_GRAY = "\033[38;5;246m"
BOLD = "\033[1m"
RESET = "\033[0m"

BROWN = "\033[38;5;172m"   # Classic Corgi orange/brown
WHITE = "\033[38;5;255m"   # Crisp white chest/snout/paws
GRAY  = "\033[38;5;242m"   # Dark gray / black line accents
CYAN  = "\033[38;5;51m"    # Speech bubble border
TEXT  = "\033[38;5;231m"   # Speech bubble text

C = CYAN
T = TEXT
B = BROWN
W = WHITE
G = GRAY
R = RESET

TIC = f"{BOLD}{PINK}TIC{RESET}"
TAC = f"{BOLD}{LIME}TAC{RESET}"
TOE = f"{BOLD}{PURPLE}TOE{RESET}"

def center_block(text, width=50):
    return "\n".join(line.center(width) for line in text.split("\n"))

def left_pad(text, width=50):
    return " " * max((width - len(text)) // 2, 0)

# ======================================================================
#  WELCOME PAGE
# ======================================================================

CORGI_ART = f"""
                  {G},-.{R}                    {G},-.{R}           {C}________________{R}         
                 {B}((  {G}\\\\                {G}//  {B})){R}         {C}/ {T}Hi, I'm Max!{C}   \\{R}
                 {B}((   {G}\\\\__          __//   {B})){R}      {C}_ /                  |{R}
                  {G}(\\_-)/{B}####\\      /####\\{G}(-_/){R}    {C}/   {T}Let's play{C}        |{R}
                  {G}\\_//{B}######\\___{B}######\\\\_/{R}      {C}|                    _/{R}  
                   {G}){B}###  {G}*{R}  {W}/   \\{R}  {G}*{B}  ###{G}({R}       {C}|  |{TIC} {TAC} {TOE}{C}| ___/{R}  
                  {G}({B}##{W}/   '-' (_) '-'   {B}\\{G}##){R}     {C}/   _____________{C}/{R}
                   {G}-( ({W}      \\___/      {G}) )-{R}  {C}< ___/{R}
                     {G}`=='{W}/   /`*._        {G}/\\{R}
                  {G},={B}######{W}/  {W}(      \\     {G}-*||){R}
              {G}.__//{B}########## {W}(     "  "   {G}) \\{R}
             {G}( {B}#/######^.##########{W}        : ){R}
             {G}\\{B}#(/#########\\####(#####\\{W}    : /{G}){R}
              {G}( {B}####### /{B}#####\\ ### {W}||   _/*/|{R}
              {G}({B}######_/_/#####{G},\\    {W}||-= /   ({R}
               {G}\\=*/{B}-___:){G}---' {W}(_,,)   (_,,,){R}
              
              {B}// \\\\ // \\  \\_] \\_\\\\______/__/{R}
"""

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

start_text = "Press [ENTER] to start..."
retry_text = "Press [ENTER] to start, or type STOP to quit."
prompt_text = start_text

while True:
    clear_screen()
    print(CORGI_ART)
    start_input = input("\n" + left_pad(prompt_text) + prompt_text + " ")
    if start_input == "STOP":
        print(center_block("\nTschüss!\n"))
        sys.exit()
    if start_input == "":
        break
    prompt_text = retry_text

# ======================================================================
#  ENTER PLAYER NAMES
# ======================================================================

def valid_name(prompt, other_name = None, prior_lines = None):
    while True:
        clear_screen()
        print(CORGI_ART)
        print(center_block("\nWelcome to\n"))
        print(left_pad("TIC TAC TOE") + f"{TIC} {TAC} {TOE}")
        print(center_block("\nPlease enter your names\n"))

        if prior_lines:
            for line in prior_lines:
                print(line)

        name = input(left_pad(prompt) + prompt).strip()

        if name == "STOP":
            print(center_block("\nTschüss!\n"))
            sys.exit()

        error_msg = ""
        if not name.replace(" ", "").replace("-", "").isalpha():
            error_msg = "Name must contain letters only."
        elif other_name and name.lower() == other_name.lower():
            error_msg = "Names must be different."

        if error_msg:
            print(center_block(error_msg))
            input(left_pad("Press [ENTER] to try again...") + "Press [ENTER] to try again...")
            continue

        return name

p1_name = valid_name("Player 'X' Name: ")
p1_line = left_pad("Player 'X' Name: ") + "Player 'X' Name: " + p1_name
p2_name = valid_name("Player 'O' Name: ", other_name=p1_name, prior_lines=[p1_line])

# ======================================================================
#  SETUP
# ======================================================================

def show_board():
    def cell(val):
        if val == "X":
            return f"{BOLD}{LIME}X{RESET}"
        elif val == "O":
            return f"{BOLD}{PURPLE}O{RESET}"
        return val

    row1 = f" {cell(board[0])} | {cell(board[1])} | {cell(board[2])} "
    row2 = f" {cell(board[3])} | {cell(board[4])} | {cell(board[5])} "
    row3 = f" {cell(board[6])} | {cell(board[7])} | {cell(board[8])} "
    sep = "---+---+---"

    pad = left_pad(sep)
    print()
    print(pad + row1)
    print(pad + sep)
    print(pad + row2)
    print(pad + sep)
    print(pad + row3)
    print()

def check_win():
    for a, b, c in wins:
        if board[a] == board[b] == board[c]:
            return True
    return False

# ======================================================================
#  SCOREBOARD SETUP
# ======================================================================
p1_score = 0
p2_score = 0

def score_board(p1_name, p1_score, p2_name, p2_score):
    header = "CURRENT SCORE"
    plain_line = f"{p1_name}   {p1_score}:{p2_score}   {p2_name}"
    colored_line = f"{BOLD}{LIME}{p1_name}{RESET}   {BOLD}{p1_score}:{p2_score}{RESET}   {BOLD}{PURPLE}{p2_name}{RESET}"

    print(left_pad(header) + header + RESET)
    print(left_pad(plain_line) + colored_line)
    print()


wins = [(0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)]

while True:
    board = ["1","2","3","4","5","6","7","8","9"]
    curr_mark = "X"
    moves = 0

    while True:
        os.system('cls' if os.name == "nt" else "clear")
        print(left_pad("TIC TAC TOE") + f"{TIC} {TAC} {TOE}\n")
        score_board(p1_name, p1_score, p2_name, p2_score)
        show_board()

        curr_player = p1_name if curr_mark == "X" else p2_name
        mark_color = LIME if curr_mark == "X" else PURPLE
        plain_turn_msg = f"{curr_player}'s turn!"
        colored_turn_msg = f"{BOLD}{mark_color}{curr_player}{RESET}'s turn!"
        instruction = "Enter a number 1 - 9, or 'STOP' to exit the game. "

        move = input(f"\n {left_pad(plain_turn_msg)} {colored_turn_msg} \n{instruction}")

        if move == "STOP":
            print(center_block("\nTschüss!\n"))
            sys.exit()

        if move not in ["1","2","3","4","5","6","7","8","9"]:
            print("Invalid move.")
            input("Press [ENTER] to continue...")
            continue

        if board[int(move) - 1] in ("X", "O"):
            print("That space is already taken.")
            input("Press [ENTER] to continue...")
            continue

        board[int(move) - 1] = curr_mark
        moves += 1

        if check_win():
            os.system('cls' if os.name == "nt" else "clear")
            print(left_pad("TIC TAC TOE") + f"{TIC} {TAC} {TOE}\n")
            if curr_player == p1_name:
                p1_score += 1
            else:
                p2_score += 1
            score_board(p1_name, p1_score, p2_name, p2_score)
            show_board()
            win_msg_plain = f"{curr_player} wins!"
            win_msg_colored = f"{BOLD}{mark_color}{curr_player}{RESET} wins!"
            print(f"\n{left_pad(win_msg_plain)} {win_msg_colored}")
            break

        if moves == 9:
            os.system('cls' if os.name == "nt" else "clear")
            print(left_pad("TIC TAC TOE") + f"{TIC} {TAC} {TOE}\n")
            score_board(p1_name, p1_score, p2_name, p2_score)
            show_board()
            print(center_block("Draw!"))
            curr_mark = "O" if curr_mark == "X" else "X"

            break

        curr_mark = "O" if curr_mark == "X" else "X"

    if input("ENTER = next round, STOP = exit: ") == "STOP":
        break