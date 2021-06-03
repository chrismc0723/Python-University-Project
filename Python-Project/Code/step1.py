"""
Create Batch order's for component orders
Coded by Christopher McClure
"""

import json

# create Batch class
class Batch:
    def _init_(self, batch_number, manufacture_date, serial_numbers, serial_numbers_list, no_of_components, component_number):
        self.batch_number = batch_number
        self.manufacture_date = manufacture_date
        self.serial_numbers = serial_numbers
        self.serial_numbers_list = serial_numbers_list
        self.no_of_components = no_of_components
        self.component_number = component_number

#create Component class
class Component:
    def _init_(self, chosen_component, chosen_size, correct_option):
        self.chosen_component = chosen_component
        self.chosen_size = chosen_size
        self.correct_option = correct_option


# Open or create a Json file
try:
    with open('data.json', 'r') as f:
        batch_count = json.load(f)

except FileNotFoundError:
    with open('data.json', 'w') as f:
        batch_count = 0
        json.dump(batch_count, f)

# start program by asking user to either create a batch or exit the program
while True:
    print("please select an option")
    print("1 = create a batch")
    print("0 = exit")

    choice = input("> ")
    if choice == '1':
        # if 1 is selected then the process of creating a batch begins
        # batch_count tallys up how many batches there are
        batch_count = batch_count + 1
        print("welcome to the program")

        from datetime import date

        # create the date the components are manufactured
        manufacture_date = date.today().strftime('%Y%m%d')
        print("this is the manufacture date " + manufacture_date)

        # create the batch number using the date
        batch_number = date.today().strftime('%Y%m%d') + str(batch_count).zfill(4)
        print("this is your batch number " + batch_number)
        print()

        # have user input how many components will be in the batch
        no_of_components = input("how many components are in this batch?")
        print("These will be the serial numbers for the components")

        # create serial numbers for each component inside the batch
        serial_numbers_list = []
        for i in range(int(no_of_components)):
            i = i + 1
            serial_numbers = batch_number + str(i).zfill(4)
            serial_numbers_list.append(serial_numbers)
            print(serial_numbers)
        print("-----------------------------")

        # DECLARING OUR LISTS
        components_list = ["1 = Winglet Strut", "2 = Door Handle", "3 = Rudder Pin"]
        sizes_list3 = ["1 = 10mm diameter by 75mm length", "2 = 12mm diameter by 100mm length",
                       "3 = 16mm diameter by 15mm length"]

        while True:
            # after creating serial numbers now user inputs what component these serial numbers will be assigned to
            print(components_list)
            print("what component?")

            # have user select size of the component
            chosen_component = input("> ")

            # if component is winglet strut do this
            if chosen_component == '1':
                print("you have selected Winglet Strut.")
                chosen_component = "Winglet Strut"
                sizes_list1 = ["1 = A320 Series", "2 = A380 Series"]
                print(sizes_list1)
                print("Please select the size of the of the component")

                # if size equels A320 series do this
                size1 = input("> ")
                if size1 == '1':
                    print("you have selected Winglet Strut A320 Series")
                    chosen_size = "A320 Series"
                    print()
                    break

                # if size equels A380 series do this
                if size1 == '2':
                    print("you have selected Winglet Strut A380 Series")
                    chosen_size = "A380 Series"
                    print()
                    break

                # if size does not equel A320 or A380 do this
                if size1 != '1' and size1 != '2':
                    print("invalid option for Winglet Strut size")
                    size1 = input("> ")

                print("--------------------------------")
                break

            # if component is door handle do this
            elif chosen_component == '2':
                print("you have selected the Door Handle")
                chosen_component = "Door Handle"
                chosen_size = "Universal size"
                break

            # if component is rudder pin do this
            elif chosen_component == '3':
                print("you have selected Rudder Pin")
                chosen_component = "Rudder Pin"
                print(sizes_list3)
                print("Please select the size of the of the component")
                size3 = input("> ")
                # if size is 10mm by 75mm do this
                if size3 == '1':
                    print("you have selected Rudder Pin 10mm diameter by 75mm length")
                    chosen_size = "10mm by 75mm"
                    print()
                    break

                # if size is 12mm by 100mm do this
                elif size3 == '2':
                    print("you have selected Rudder Pin 12mm diameter by 100mm length")
                    chosen_size = "12mm by 100mm"
                    print()
                    break

                # if size is 16mm by 150mm do this
                elif size3 == '3':
                    print("you have selected Rudder Pin 16mm diameter by 150mm length")
                    chosen_size = "16mm by 150mm"
                    break

                # if invalid re-ask
                else:
                    print("invalid option selected for Rudder Pin size")
                    size3 = input("> ")
                    print("-------------------------------")

            # if invalid re-ask
            else:
                print("invalid option chosen for component")
                chosen_component = input("> ")

        # after user has sorted the batch details output them to allow user to check them
        while True:
            print("Batch Number: " + batch_number)
            print("Manufacture Date: " + manufacture_date)
            print("Component Type: " + chosen_component)
            print("Component Size: " + chosen_size)
            print("number of components in this batch: " + no_of_components)
            print("Serial Numbers: " + str(serial_numbers_list))
            print("Are these details correct?")
            print("1 = yes", "0 = no")
            correct_option = input("> ")

            # if details are correct store the batch_count in a json file
            if correct_option == '1':
                with open('data.json', 'w') as f:
                    json.dump(batch_count, f)
                break

            elif correct_option == '0':
                print(2)
                continue
            else:
                print("invalid choice")

            print("Reached end of program")

    # if user selects to exit program
    elif choice == '0':
        print("you have selected to exit program")
        print()
        break
    else:
        # if user doesnt select 0 or 1 ask them if they want to try again
        print("invalid choice4")
        print("do you want to try again, 1 = yes and 0 = no")
        retry = input("> ")
        if retry == '1':
            print()
            continue
        elif retry == '0':
            print()
            break
        else:
            print("invalid choice")
        print()

