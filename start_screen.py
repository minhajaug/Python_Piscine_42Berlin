#!/usr/bin/env python3

import os
import sys

# ANSI color codes (256-color palette)
RESET = "\033[0m"
BROWN = "\033[38;5;172m"   # Classic Corgi orange/brown
WHITE = "\033[38;5;255m"   # Crisp white chest/snout/paws
GRAY  = "\033[38;5;242m"   # Dark gray / black line accents
CYAN  = "\033[38;5;51m"    # Speech bubble border
TEXT  = "\033[38;5;231m"   # Speech bubble text

# Colors for TIC TAC TOE
CLR_TIC = "\033[38;5;196m"  # Bright Red
CLR_TAC = "\033[38;5;226m"  # Bright Yellow
CLR_TOE = "\033[38;5;46m"   # Bright Green

C = CYAN
T = TEXT
B = BROWN
W = WHITE
G = GRAY
R = RESET

TIC = f"{CLR_TIC}TIC{R}"            # col
TAC = f"{CLR_TAC}TAC{R}"
TOE = f"{CLR_TOE}TOE{R}"

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


clear_screen()
print(CORGI_ART)
print(f"\n             Press [ENTER] to start...")
input()