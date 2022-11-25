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


def read_nonempty_string(prompt):
    while True:
        users_input = input(prompt)
        if len(users_input) > 0 and users_input.isalpha():
            break
    return users_input


def read_integer(prompt):
    while True:
        try:
            users_input = int(input(prompt))
            if users_input >= 0:
                return users_input
        except ValueError:
            print("Sorry -number only please")


def race_venues():
    with open("races.txt") as input:
        lines = input.readlines()
    races_location = []
    for line in lines:
        races_location.append(line.strip("\n"))
    return races_location


def runners_data():
    with open("runners.txt") as input:
        lines = input.readlines()
    runners_name = []
    runners_id = []
    for line in lines:
        if not line.isspace():
            split_line = line.split(",")
            runners_name.append(split_line[0])
            id = split_line[1].strip("\n")
            runners_id.append(id)
    return runners_name, runners_id


def competitors_by_county(name, id):
    print("=" * 20)
    print("Cork runners")
    print("=" * 20)
    for i in range(len(name)):
        if id[i].startswith("CK"):
            print(f"{name[i]} ({id[i]})")
    print("=" * 20)
    print("Kerry runners")
    print("=" * 20)
    for i in range(len(name)):
        if id[i].startswith("KY"):
            print(f"{name[i]} ({id[i]})")


def main():
    races_location = race_venues()
    runners_name, runners_id = runners_data()
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
            competitors_by_county(runners_name, runners_id)
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
