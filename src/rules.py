from src.irules import EndGameInterface
from irules import RulesInterface

class RuleAdjacentPiecesDifferentColors(RulesInterface):
    def is_legal_board(self):
        # $TODO
        return True

class GameEndCheckAllSquaresFilled(EndGameInterface):
    def is_game_ended(self):
        # $TODO
        return True
