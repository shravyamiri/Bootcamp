import pickle

class Game:
    def __init__(self, level, score):
        self.level = level
        self.score = score

    def save(self, filename="game_state.pkl"):
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @staticmethod
    def load(filename="game_state.pkl"):
        with open(filename, "rb") as f:
            return pickle.load(f)

game = Game(5, 300)
game.save()
loaded_game = Game.load()
print(loaded_game.__dict__)