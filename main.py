import chess.pgn
import chess.variant
import chess
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

def 

if __name__ == '__main__':
    print("hello")
    pgn = open("C:\\Users\\Dennis\\PycharmProjects\\pythonProject1\\games-bank\\2021-03")
    first_game = chess.pgn.read_game(pgn)
    board = first_game.board()
    print(board)

