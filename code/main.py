# ---------- TUNINGS: ----------
# This program allows a user to|
# enter a guitar tuning, and   |
# outputs scales relative to   |
# that tuning.                 |
# ------------------------------

# takes a 2D array of integers and prints it out
# as notes on a fretboard
def print_board(given_board):
    for i in range(len(given_board)):
        print("|", end='')
        for j in range(len(given_board[0])):
            if given_board[i][j] == 0:
                print("   |", end='')
            else:
                note = numsToNotes[int(given_board[i][j])]
                if "#" in note:
                    print(" " + note + "|", end='')
                else:
                    print(" " + note + " |", end='')
        print("   " + str(i))
        print("-------------------------")


# Allows a user to enter the notes that make up a
# guitar tuning. Tuning is returned as an integer array.
def get_tuning():
    print("-----------------------------------------------------------------")
    print("| Enter \"n\" for a new tuning, or \"l\" to load a saved tuning |")
    print("-----------------------------------------------------------------")
    tuning_option = input("-> ")
    notes = []
    if tuning_option.lower() == "n":
        for i in range(6):
            notes.append(input("Please enter the note of string " + str(6 - i) + " ->  "))
    elif tuning_option.lower() == "l":
        notes = load_tuning()
    else:
        print("--option not recognized, try again--")
        return get_tuning()
    for i in range(len(notes)):
        notes[i] = notesToNum[notes[i]]
    return notes


# Lets a user load a previously saved tuning.
# Result is returned to get_tuning().
def load_tuning():
    print("Available tuning: ")
    tuning_names = []
    tuning_notes = []
    with open('stored_tunings.txt') as f:
        switch = 0
        for line in f:
            if switch % 2 == 0:
                tuning_names.append(line.strip())
            else:
                tuning_notes.append(line.strip())
            switch += 1

    for i in range(len(tuning_names)):
        print(tuning_names[i])

    choice = input("enter tuning choice, or \'b\' to go back -> ")
    if choice == 'b':
        return get_tuning()
    else:
        if choice not in tuning_names:
            print("---tuning not recognized, please try again---")
            return load_tuning()
        else:
            for i in range(len(tuning_names)):
                if choice == tuning_names[i]:
                    split_notes = tuning_notes[i].split(',')
                    for j in split_notes:
                        j = notesToNum[j]
    return split_notes


# Lets the user save the current tuning. Catches duplicate tunings.
def save_tuning(current_tuning):
    tuning_name = input("Enter tuning name -> ")
    tuning_notes = ""
    for i in current_tuning:
        tuning_notes = tuning_notes + numsToNotes[i] + ","
    tuning_notes = tuning_notes[:-1]

    duplicate_name = False
    duplicate_tuning = False
    with open('stored_tunings.txt') as f:
        for line in f:
            if line == tuning_name:
                duplicate_name = True
            if line == tuning_notes:
                duplicate_tuning = True

    if duplicate_name and duplicate_tuning:
        print("Tuning and tuning name already saved.")
    elif duplicate_name:
        print("Tuning name already saved.")
    elif duplicate_tuning:
        print("Tuning already saved.")
    else:
        with open('stored_tunings.txt', "a") as f:
            f.write(tuning_name)
            f.write(tuning_notes)


# generates a full fretboard of notes from
# a tuning. Returns fretboard as 2D int array.
def generate_fretboard(tuning_array):
    fretboard_array = [[]]
    for i in tuning_array:
        fretboard_array[0].append(i)
    for i in range(13):
        temp = [(j % 12)+1 for j in fretboard_array[i]]
        fretboard_array.append(temp)
    return fretboard_array


# Allows user to enter a key
def get_key():
    entered_key = input("Please enter key -> ")
    if entered_key in notesToNum.keys():
        return notesToNum[entered_key]
    else:
        print("--Key not recognized, try again--")
        return get_key()


# Allows user to enter a mode
def get_mode():
    entered_mode = input("Please enter mode -> ")
    if entered_mode in modeToSteps.keys():
        return modeToSteps[entered_mode]
    else:
        print("--Mode not recognized, try again--")
        return get_mode()


# Takes the current key and mode and returns the notes
# of the scale as an integer array.
def generate_scale_numbers(given_key, given_mode):
    scale_nums = [given_key]
    for i in range(len(given_mode)):
        previous_num_in_scale = scale_nums[i]
        next_number = previous_num_in_scale + given_mode[i]
        corrected_number = (next_number % 13) + (next_number // 13)
        scale_nums.append(corrected_number)
    return scale_nums


# Takes the current fretboard and scale notes to create
# a fretboard of just the notes in the scale.
def generate_scale_board(given_scale, given_fretboard):
    board = [[]]
    for i in range(12):
        if i > 0:
            board.append([])
        for j in range(6):
            if given_fretboard[i][j] in given_scale:
                board[i].append(given_fretboard[i][j])
            else:
                board[i].append(0)
    return board


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # used for turning a note name into a
    # numeric representation
    notesToNum = {
        "a": 1,
        "a#": 2,
        "bb": 2,
        "b": 3,
        "c": 4,
        "c#": 5,
        "db": 5,
        "d": 6,
        "d#": 7,
        "eb": 7,
        "e": 8,
        "f": 9,
        "f#": 10,
        "gb": 10,
        "g": 11,
        "g#": 12,
        "ab": 12
    }

    # Used for turning a number representation of a
    # note into the note name.
    numsToNotes = {
        1: "a",
        2: "a#",
        3: "b",
        4: "c",
        5: "c#",
        6: "d",
        7: "d#",
        8: "e",
        9: "f",
        10: "f#",
        11: "g",
        12: "g#"
    }

    # Used for turning mode into steps
    modeToSteps = {
        "major": [2, 2, 1, 2, 2, 2],
        "ma": [2, 2, 1, 2, 2, 2],
        "minor": [2, 1, 2, 2, 1, 2],
        "mi": [2, 1, 2, 2, 1, 2],
        "dorian": [2, 1, 2, 2, 2, 1],
        "d": [2, 1, 2, 2, 2, 1],
        "mixolydian": [2, 2, 1, 2, 2, 1],
        "mx": [2, 2, 1, 2, 2, 1],
        "minorPentatonic": [3, 2, 2, 3],
        "mip": [3, 2, 2, 3],
        "majorPentatonic": [2, 2, 3, 2],
        "map": [2, 2, 3, 2]
    }

    # Gets tuning as int array
    tuning = get_tuning()

    # Creates fretboard as 2D array
    fretboard = generate_fretboard(tuning)

    while True:

        # gives user th possible options
        print("----------------------------------------------------------------")
        print("| Enter \'c\' change tuning, \'s\' to save the current tuning, |")
        print("| \'p\' to print the fretboard, \'k\' to enter a key and mode, |")
        print("| or \'q\' to quit.                                            |")
        print("----------------------------------------------------------------")
        user_choice = input("-> ")

        # change tuning
        if user_choice == "c":
            tuning = get_tuning()
            fretboard = generate_fretboard(tuning)

        # save tuning
        elif user_choice == "s":
            save_tuning(tuning)

        # print fretboard
        elif user_choice == "p":
            print_board(fretboard)

        # enter key and mode
        elif user_choice == "k":
            key = get_key()
            mode = get_mode()
            scale_nums = generate_scale_numbers(key, mode)
            generate_scale_board(scale_nums, fretboard)

        # quit
        elif user_choice == "q":
            break

        # unrecognized input
        else:
            print("--Option not recognized, please try again--")

    print("Have a good day, bye!")


















