from user_interface import UserInterface
from sweepstakes import Sweepstakes


class Marketing_Firm:

    def __init__(self, name):
        self.marketing_firm_name = name
        self.sweepstakes_inventory = []

    def select_sweepstakes(self):
        selected_sweepstakes = UserInterface.get_user_input_string("Select your sweepstakes")
        return selected_sweepstakes

    def create_sweepstakes(self):
        self.sweepstakes_inventory.append(UserInterface.get_user_input_string("Enter the sweepstakes name"))

    def change_marketing_firm_name(self):
        self.marketing_firm_name = UserInterface.get_user_input_string("Enter your firm name")

    def menu(self):
        user_selection = UserInterface.get_user_input_number("Please enter your selection")
        if user_selection == 1:
            return self.create_sweepstakes()
        elif user_selection == 2:
            return self.change_marketing_firm_name()
        elif user_selection == 3:
            print(self.sweepstakes_inventory)
            return self.select_sweepstakes()
