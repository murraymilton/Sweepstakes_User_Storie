class Contestant:

    def __init__(self, first_name, last_name, email_address, registration_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.registration_number = registration_number
        self.contestant_info = ()

    # def display_contestant_entry_status(self):
    #     print(f'{self.first_name} {self.last_name}\n Email: {self.email}'
    #           f'Address: \n{self.address} \nRegistration Number:{self.registration_number}')
    #     for contestant in self.contestant_info:
    #         contestant.display_contestant_entry_status()

    def add_contestant(self, contestant):
        self.contestant_info.append(contestant)

    def notify_winner(self, winner_announced):
        winner_announced = False
        if winner_announced:
            pass
        else:
            pass