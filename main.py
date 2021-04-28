import chess.pgn
import chess.variant
import chess
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import time
import datatable as dt


def parseToGames(file):
    pgn = open("C:\\Users\\Dennis\\PycharmProjects\\pythonProject1\\games-bank\\%s" % file) # Add correct column names
    df = pd.DataFrame(columns=['PGN', 'Result', 'Avarage Rating', 'Rating Difference', 'Termination Type', 'Starting Position'])
    dataPGN = []
    dataStartPos = []
    while True:
        # start = time.time()
        game = chess.pgn.read_game(pgn)
        game
        # end = time.time()
        # print(end - start)
        if game is None:
            break
        dataStartPos.append(game.board()) # Adds starting position
        #dataPGN.append(game.)
    return result


if __name__ == '__main__':
    games = parseToGames("2021-03.pgn")
    board = games[0]
    print(board)
