def main():
    menu = "1. Show the results for a race \n2. Add results for a race \n3. Show all competitors by county " \
           "\n4. Show the winner of each race \n5. Show all the race times for one competitor " \
           "\n6. Show all competitors who have won a race \n7. Quit \n>>> "
    print(menu)
    input_menu = int(input("Select option: "))

    while input_menu != 7:
        if input_menu == 1:
            print("option 1")
        elif input_menu == 2:
            print("option 2")
        elif input_menu == 3:
            print("option 3")
        elif input_menu == 4:
            print("option 4")
        elif input_menu == 5:
            print("option 5")
        elif input_menu == 6:
            print("option 6")
        input_menu = int(input("Select option: "))

main()