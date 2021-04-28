import chess.pgn
import chess.variant
import chess
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd


def parseToGames(file):
    pgn = open("C:\\Users\\Dennis\\PycharmProjects\\pythonProject1\\games-bank\\%s" % file)
    result = []
    while True:
        game = chess.pgn.read_game(pgn)
        if game is None:
            break
        result.append(game)
    return result


if __name__ == '__main__':
    games = parseToGames("2021-03.pgn")
    board = games[0]
    print(board)




