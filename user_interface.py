
class UserInterface:

    @staticmethod
    def display_message(message):
        print(f"Welcome")
        print(message)


    @staticmethod
    def get_user_input_string(prompt):

        user_input = input(prompt)
        return user_input

    @staticmethod
    def get_user_input_number(prompt):

        user_input = int(input(prompt))
        return user_input
        pass
