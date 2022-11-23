def read_integer_between_numbers(prompt, mini, maximum):
    while True:
        try:
            users_input = int(input(prompt))
            if mini <= users_input <= maximum:
                return users_input
            else:
                print(f"Numbers from {mini} to {maximum} only.")
        except ValueError:
            print("Sorry - numbers only please")


def main():
    menu = "1. Show the results for a race \n2. Add results for a race \n3. Show all competitors by county " \
           "\n4. Show the winner of each race \n5. Show all the race times for one competitor " \
           "\n6. Show all competitors who have won a race \n7. Show all competitors who have not taken a " \
           "podium-position in any race \n8. Quit \n>>> "
    input_menu = read_integer_between_numbers(menu, 1, 8)
    while input_menu != 8:
        if input_menu == 1:
            print("Show the results for a race ")
        elif input_menu == 2:
            print("Add results for a race ")
        elif input_menu == 3:
            print("Show all competitors by county ")
        elif input_menu == 4:
            print("Show the podium-places for each race ")
        elif input_menu == 5:
            print("Show all the race times and finishing-positions for one competitor ")
        elif input_menu == 6:
            print("Show all competitors who have won a race ")
        elif input_menu == 7:
            print("Show all competitors who have not taken a podium-position in any race ")
        input_menu = read_integer_between_numbers(menu, 1, 8)


main()
