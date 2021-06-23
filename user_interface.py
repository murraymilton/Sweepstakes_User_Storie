
class UserInterface:

    @staticmethod
    def display_message(message):
        print(message)


    @staticmethod
    def get_user_input_string(prompt):
        user_input = input(prompt)
        return user_input

    @staticmethod
    def get_user_input_number(prompt):
        response = int(input(prompt))
        return response

    @staticmethod
    def display_contestant_info(contestant):
        print(contestant.first_name)
        print(contestant.last_name)
        print(contestant.email_address)
        print(contestant.registration_number)

    @staticmethod
    def display_sweepstakes_info(sweepstakes):
        print(sweepstakes.sweepstakes_name)
        print(f'{len(sweepstakes.contestants)} contestants')

    @staticmethod
    def display_marketing_firm_menu_options(marketing_firm_name):
        return marketing_firm_name


    @staticmethod
    def display_sweepstakes_menu_options(sweepstakes_name):
        return sweepstakes_name