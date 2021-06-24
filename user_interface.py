class UserInterface:

    @staticmethod
    def display_message(message):
        print(message)
        user_selection = UserInterface.get_user_input_number("Please enter your selection:")
        if user_selection == 1:
            UserInterface.display_marketing_firm_menu_options(message)
        elif user_selection == 2:
            UserInterface.display_sweepstakes_menu_options()



    @staticmethod
    def get_user_input_string(prompt):
        user_input = input(prompt)
        return user_input

    @staticmethod
    def get_user_input_number(prompt):
        try:
            user_pick = int(input(prompt))
            return user_pick
        except ValueError:
            print("Enter a number")
            return UserInterface.get_user_input_number(prompt)

    @staticmethod
    def display_contestant_info(sweepstakes):
        print(f'There are{len(sweepstakes.contestants)}.')
        for contestant in sweepstakes.view_contestants():
            print(f'First Name:{contestant.first_name}, Last Name:{contestant.last_name}, \nE-Mail: {contestant.email_address},\nRegistration I.D{contestant.registration_number()}')

    @staticmethod
    def display_sweepstakes_info(sweepstakes_name, contestants):
        print(f"{sweepstakes_name} sweepstakes.")
        print(f"{sweepstakes_name} has {len(contestants)}")

    @staticmethod
    def display_sweepstakes_selection_menu(sweepstakes_inventory):
        print("Sweeps-N-Stakes menu:")
        print(f'{sweepstakes_inventory}')
        sweepstakes_name = UserInterface.get_user_input_string("Please enter sweepstakes name:")
        return UserInterface.display_sweepstakes_menu_options(sweepstakes_name)

    @staticmethod
    def display_marketing_firm_menu_options(marketing_firm_name):
        print(f'{marketing_firm_name} menu:')
        print('To create a sweepstakes enter -1-.')
        print('To change the marketing firms name enter -2-.')
        print('To select a sweepstakes enter -3-.')


    @staticmethod
    def display_sweepstakes_menu_options(sweepstakes):
        print(f'{sweepstakes.sweepstakes_name} menu')
        print(f'{UserInterface.display_sweepstakes_info()}')
        print('To register a contestant enter -1-.')
        print('To view contestants enter -2-.')
        print('To select a winner of the sweepstakes enter -3-.')