import random
from contestant import Contestant
from user_interface import UserInterface


class Sweepstakes:

    def __init__(self, name):
        self.sweepstakes_name = name
        self.contestants = {}
        contestant = Contestant()

    def register_contestant(self, contestant):
        self.contestants.update(self.get_registration_number(contestant))

    def get_registration_number(self, contestant):
        contestant.contestant_registration_number = 0000
        for contestant in self.contestants:
            contestant.contestant_registration_number += 1

    def pick_winner(self):
        winner_announced = random.randint(self.contestants)
        Contestant.notify_winner()
        return winner_announced

    def view_contestants(self):
        return UserInterface.display_contestant_info()

    def menu(self):
        user_selection = UserInterface.get_user_input_number("Please make a selection:")
        self.register_contestant()
        self.view_contestants()
        self.announce_winner()
        pass