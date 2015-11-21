from collections import namedtuple


Player = namedtuple('Player', 'team name age position')


class Team():
    def __init__(self, name, pic, players, opponent, wins, losses):
        self.name = name
        self.pic = pic
        self.players = players
        self.opponent = opponent
        self.wins = wins
        self.losses = losses

    def team_to_str(self):
        return (self.name)
