import user_interface
from sweepstakes import Sweepstakes


class Marketing_Firm:

    def __init__(self, name):
        self.marketing_firm_name = name
        self.sweepstakes_inventory = []

    def create_sweepstakes(self):
        sweepstakes = Sweepstakes()
        self.sweepstakes_inventory.append(user_interface.get_user_input_string())

    def select_sweepstakes(self):
        selected_sweepstakes = user_interface.get_user_input_number()
        return selected_sweepstakes

    def change_marketing_firm_name(self):
        self.marketing_firm_name = user_interface.get_user_input_string()


    def menu(self):
        self.create_sweepstakes()
        self.change_marketing_firm_name()
        self.select_sweepstakes()
