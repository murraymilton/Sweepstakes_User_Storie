import random
from contestant import Contestant
from marketing_firm import MarketingFirm
from user_interface import UserInterface


class Sweepstakes:

    def __init__(self, name):
        self.sweepstakes_name = name
        self.contestants = {}

    contestant = Contestant()

    def register_contestant(self, contestant):
        self.contestants.append(contestant)

    def get_registration_number(self, contestant):
        contestant.contestant_registration_number = 0000
        for contestant in self.contestants:
            contestant.contestant_registration_number += 1

    def pick_winner(self):
        winner_choice_random = random.randint(0, len(self.contestants) -1)
        for index in range(0, len(self.contestants)):
            if index == winner_choice_random:
                self.contestants[index].key['contestant_wins'] = True
        for the_contestants in self.contestants:
            the_contestants.notify_winner(the_contestants)
        Contestant.notify_winner()

    def view_contestants(self):
        return UserInterface.display_contestant_info()

    def menu(self):
        UserInterface.display_sweepstakes_menu_options(MarketingFirm.select_sweepstakes(self))
        user_selection = UserInterface.get_user_input_number("Please make a selection.")
        if user_selection == 1:
            self.register_contestant()
        elif user_selection == 2:
            self.view_contestants()
        elif user_selection == 3:
            self.pick_winner()
