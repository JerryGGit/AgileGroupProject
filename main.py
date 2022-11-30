def read_integer_between_numbers(prompt, mini, maximum):
    while True:
        try:
            users_input = int(input(prompt))
            if mini <= users_input <= maximum:
                return users_input
            else:
                print(f"Numbers from {mini} to {maximum} only.")
        except ValueError:
            print("Sorry - Numbers only please")


def read_nonempty_string(prompt):
    while True:
        users_input = str(input(prompt))
        if len(users_input) > 0 and users_input.isalpha():
            break
        else:
            print("Sorry - Letters only and no blanks allowed")
    return users_input


def read_integer(prompt):
    while True:
        try:
            users_input = int(input(prompt))
            if users_input >= 0:
                return users_input
        except ValueError:
            print("Sorry -number only please")


def format_secs_to_minSecs(secs):
    secs = int(secs)
    minutes = secs // 60
    secs_remaining = secs % 60
    formatted_time = f"{minutes} m, {secs_remaining} s"
    return formatted_time


def strip_spaces_from_list(list):
    updated_list = []
    for item in list:
        item = item.strip(" ")
        updated_list.append(item)
    return updated_list


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
            id = split_line[1].strip()
            runners_id.append(id)
    return runners_name, runners_id


def race_results_data(chosen_race):
    race_data_dict = {}
    with open(
            f"{chosen_race}.txt") as file:  # Open the file for the race using the chosen_name variable as a name for the text file
        results = file.readlines()
    for line in results:  # for loop to check if the line is empty space or not, then print the ones that aren't
        if line.isspace():
            continue
        else:
            line = line.strip(
                "\n")  # This line and next 2 lines just format the individual objects to have a nice formatted output
            runner = line.split(",")[0]
            time = line.split(",")[1]
            race_data_dict[runner] = time
    return race_data_dict


# Function shows list of races to choose from, then lists the results of chosen race
def show_race_result(races):
    prompt = ""
    print("\nWhich race would you like to see the results of?")  # Menu Prompt
    for i, race in enumerate(races):  # Iterate through races to create menu options
        race = race.split(',')[0]
        prompt += f"{i + 1}. {race}\n"
    prompt += ">>>"
    race_input = read_integer_between_numbers(prompt, 1,
                                              len(races))  # Actually print the menu using read_integer_between_numbers function
    chosen_race = races[race_input - 1].split(",")[0]  # Tie the input of the menu to the name of an actual race
    print(f"\n-- The results for {chosen_race} --")
    results = race_results_data(chosen_race)
    for key in results:
        formatted_time = format_secs_to_minSecs(results[key])
        print(f"{key}, {formatted_time}")


def competitors_by_county(name, id):
    with open("County_codes.txt") as input:
        lines = input.readlines()
    counties = {}
    for line in lines:
        if not line.isspace():
            split_line = line.split(",")
            cid = split_line[1].strip()
            if split_line[0] not in counties:
                counties[split_line[0]] = cid
    for county in counties:
        print("=" * 20)
        print(county)
        print("=" * 20)
        for i in range(len(name)):
            if id[i].startswith(counties[county]):
                print(f"{name[i]} ({id[i]})")


def users_venue(races_location, runners_name, runners_id):
    while True:
        user_location = read_nonempty_string("Where will the new race take place? ").capitalize()
        if user_location not in races_location:
            race_target = read_integer("What is the race target time? ")
            connection = open("Races.txt", "a")
            races_location.append(user_location)
            print(f"{user_location}, {race_target}", file=connection)
            connection.close()
            break
    connection = open(f"{user_location}.txt", "a")
    time_taken = []
    updated_runners = []
    for i in range(len(runners_name)):
        time_taken_for_runner = read_integer(f"Time for {runners_name[i]} >> ")
        if time_taken_for_runner != 0:
            time_taken.append(time_taken_for_runner)
            updated_runners.append(runners_id[i])
            print(f"{runners_id[i]},{time_taken_for_runner},", file=connection)
    connection.close()


# This function displays all runners who have won a race
def show_all_winners(races, runners_name, runners_id):
    print("\n-- These are all the Runners who have won atleast 1 race! --")  # Title for the display
    for race in races:  # iterating through all races
        race = race.split(",")[0]  # using .split() method to get only the name of the race
        results = race_results_data(race)  # getting the results for all races upon iteration
        times = []
        for time in results.values():  # this for loop appends results of runners who actually ran the race (aka had more than 0 seconds)
            if int(time) != 0:
                times.append(int(time))
        times.sort()  # sorts the race from lowest number to highest to easily get fastest time
        for result in results:
            if times[0] == int(results[
                                   result]):  # if statement just declares the winners id based on the fastest time (using times[0])
                winner_id = result
        updated_ids = strip_spaces_from_list(
            runners_id)  # using strip_spaces_from_list function to get rid of spaces to properly parse through list
        for name in runners_name:
            if runners_name.index(name) == updated_ids.index(
                    winner_id):  # getting index of winner_id in updated_ids list, then applying that index to runners.name list to get winners name
                winner_name = name
        print(f"{winner_id}, {winner_name}")  # Actually displaying all winners using winner_id and winner_name


def main():
    races_location = race_venues()
    runners_name, runners_id = runners_data()
    menu = "\n1. Show the results for a race \n2. Add results for a race \n3. Show all competitors by county " \
           "\n4. Show the podium-places of each race \n5. Show all the race times for one competitor " \
           "\n6. Show all competitors who have won a race \n7. Show all competitors who have not taken a " \
           "podium-position in any race \n8. Quit \n>>> "
    input_menu = read_integer_between_numbers(menu, 1, 8)
    while input_menu != 8:
        if input_menu == 1:
            show_race_result(races_location)
        elif input_menu == 2:
            users_venue(races_location, runners_name, runners_id)
        elif input_menu == 3:
            competitors_by_county(runners_name, runners_id)
        elif input_menu == 4:
            print("This feature is not available at the moment.\n Please choose another option.")
        elif input_menu == 5:
            print("Show all the race times and finishing-positions for one competitor ")
        elif input_menu == 6:
            show_all_winners(races_location, runners_name, runners_id)
        elif input_menu == 7:
            print("Show all competitors who have not taken a podium-position in any race ")
        input_menu = read_integer_between_numbers(menu, 1, 8)


main()
