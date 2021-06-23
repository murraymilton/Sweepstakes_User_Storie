import random
from contestant import Contestant


class Sweepstakes:

    def __init__(self, name):
        self.sweepstakes_name = name
        self.contestants = []

    def register_contestant(self, contestant):
        self.contestants.update(self.get_registration_number(contestant))

    def get_registration_number(self, contestant):
        contestant.contestant_registration_number = 0000
        for contestant in self.contestants:
            self.contestant_registration_number += 1

    def pick_winner(self):
        winner_announced = random.randint(self.contestants)

    def view_contestants(self):
        return self.contestants

    def menu(self):
        self.register_contestant()
        self.view_contestants()
        self.announce_winner()