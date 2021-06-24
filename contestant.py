class Contestant:

    def __init__(self, first_name, last_name, email, registration_number):
        self.key = {
             "contestant_first_name": first_name,
             "contestant_last_name": last_name,
             "contestant_email_address": email,
             "contestant_registration_number": registration_number,
             "contestant_wins": False
        }

    def notify_winner(self, winner_announced):
        if winner_announced['contestant_wins']:
            print(f"\n\t\t{winner_announced.key['contestant_first_name']} {winner_announced['contestant_last_name']}!\n"
                  f"\tCongratulations! You are the lucky winner!")
        else:
            print(f"\n\t\t{winner_announced.key['contestant_first_name']} {winner_announced['contestant_last_name']}\n"
                  f"Unfortunately you were not the winner.")


# Create the observer design for event notification using a k value dictionary?
