

checklist = []


def create(item):
    checklist.append(item)

def read(index):
    return checklist[index]

def update(index, item):
    checklist[index] = item


def destroy(index):
    checklist.pop(index)


def list_all_items():
    index = 0
    for list_items in checklist:
        print("{} {}".format(index, list_items))
        index += 1


def mark_completed(index):
    update(index, "{} {}".format('√',  checklist[index]))



def select(function_code):
    if function_code == "A" or function_code == "a":
        input_item = user_input("Input item:\n")
        create(input_item)

    elif function_code == "R" or function_code == "r":
        try:
            if index > len(checklist)-1:
                input_index = int(user_input("Input number:\n"))
                mark_completed(input_index)
                read(input_index)


    elif function_code == "D" or function_code == "d":
        list_all_items()

    elif function_code == "Q" or function_code == "q":
        return False

    else:
        print("Unknown Option")

    return True



def user_input(prompt):
    user_input = input(prompt)

    return user_input

running = True
while running:
    selection = user_input(
    "Press A to add to list, R to Read from list and D to display list\n")
    running = select(selection)
