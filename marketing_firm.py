from sweepstakes import Sweepstakes
from user_interface import UserInterface


class MarketingFirm:

    def __init__(self, name):
        self.marketing_firm_name = name
        self.sweepstakes_inventory = []

    def change_marketing_firm_name(self):
        self.marketing_firm_name = UserInterface.get_user_input_string("Enter your firm name")

    def create_sweepstakes(self):
        self.sweepstakes_inventory.append(UserInterface.get_user_input_string("Enter the sweepstakes name"))

    def select_sweepstakes(self):
        selected_sweepstakes = UserInterface.get_user_input_string("Select your sweepstakes")
        return selected_sweepstakes

    def menu(self):
        UserInterface.display_marketing_firm_menu_options(UserInterface.get_user_input_string("Enter firm name:"))
        user_selection = UserInterface.get_user_input_number("Please make a selection")
        if user_selection == 1:
             self.create_sweepstakes(Sweepstakes)
        elif user_selection == 2:
             self.change_marketing_firm_name(MarketingFirm)
        elif user_selection == 3:
             UserInterface.display_sweepstakes_selection_menu(self.sweepstakes_inventory)
             self.select_sweepstakes()
