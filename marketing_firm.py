from user_interface import UserInterface
from sweepstakes import Sweepstakes


class Marketing_Firm:

    def __init__(self, name):
        self.marketing_firm_name = name
        self.sweepstakes_inventory = []

    def select_sweepstakes(self):
        selected_sweepstakes = user_interface.get_user_input_number()
        return selected_sweepstakes

    def create_sweepstakes(self):
        sweepstakes = Sweepstakes()
        self.sweepstakes_inventory.append(user_interface.get_user_input_string())


    @staticmethod
    def change_marketing_firm_name():
        change_marketing_firm = user_interface.get_user_input_string()
        select_new_marketing_firm = change_marketing_firm
        return select_new_marketing_firm



    def menu(self):
        user_selection = UserInterface.get_user_input_number("Please enter your selection")
        pass
        self.create_sweepstakes()
        self.change_marketing_firm_name()
        self.select_sweepstakes()
