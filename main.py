import chess.pgn
import chess.variant
import chess
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import time
import csv


def write_csv(data):
    with open('2021-03.csv', 'a') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(data)


def parseToGames(fromfile):
    pgn = open("C:\\Users\\Dennis\\PycharmProjects\\pythonProject1\\games-bank\\%s" % fromfile)
    colnames = ['PGN', 'Event', 'Result', 'BlackElo', 'WhiteElo',
                'FEN', 'Termination', 'TimeControl', 'UTCTime']
    write_csv(colnames)
    while True:
        game = chess.pgn.read_game(pgn)
        if game is None:
            break
        gameNode = game.game().headers
        exporter = chess.pgn.StringExporter(headers=False, variations=True, comments=True)  # Game as string
        pgn_string = game.accept(exporter)
        write_csv([pgn_string, gameNode["Event"], gameNode["Result"], gameNode["BlackElo"], gameNode["WhiteElo"],
                   gameNode["FEN"], gameNode["Termination"], gameNode["TimeControl"], gameNode["UTCTime"]])


if __name__ == '__main__':
    parseToGames("2021-03.pgn")