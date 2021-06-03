"""
This code will:
Create Batch order's for component orders
Display all the batch numbers
View details of a particular batch number
View details of a component
Coded by Christopher McClure
"""

import json
import pickle

# create Batch class
class Batch:
    def _init_(self, batch_number, list_data_batch, manufacture_date, serial_number, serial_numbers_list, no_of_components, component_number):
        self.batch_number = batch_number
        self.list_data_batch = list_data_batch
        self.manufacture_date = manufacture_date
        self.serial_number = serial_number
        self.serial_numbers_list = serial_numbers_list
        self.no_of_components = no_of_components
        self.component_number = component_number

# create Component class
class Component:
    def _init_(self, component, list_data_component, chosen_component, chosen_size, correct_option):
        self.component = component
        self.list_data_component = list_data_component
        self.chosen_component = chosen_component
        self.chosen_size = chosen_size
        self.correct_option = correct_option

# Open or create Json files
try:
    with open('data.json', 'r') as f:
        batch_count = json.load(f)

except FileNotFoundError:
    with open('data.json', 'w') as f:
        batch_count = 0
        json.dump(batch_count, f)

try:
    with open('list_data_batch.json', 'r') as f:
        list_data_batch = json.load(f)

except FileNotFoundError:
    with open('list_data_batch.json', 'w') as f:
        list_data_batch = []
        json.dump(list_data_batch, f)

try:
    with open('list_data_component.json', 'r') as f:
        list_data_component = json.load(f)

except FileNotFoundError:
    with open('list_data_component.json', 'w') as f:
        list_data_component = []
        json.dump(list_data_component, f)

# Start program by giving user 5 options to choose from
while True:
    print("please select an option")
    print("1 = create a batch")
    print("2 = List all batches")
    print("3 = View details of a batch")
    print("4 = View details of a component")
    print("0 = exit")

    choice = input("> ")
    # If 1 is selected then start creating a batch process
    if choice == '1':
        # start count of batches
        batch_count = batch_count + 1
        print("welcome to the program")
        from datetime import date

        # Create batch number, manufacture date and serial numbers
        manufacture_date = date.today().strftime('%Y%m%d')
        print("this is the manufacture date " + manufacture_date)
        batch_number = date.today().strftime('%Y%m%d') + str(batch_count).zfill(4)
        print("this is your batch number " + batch_number)
        print()
        no_of_components = input("how many components are in this batch?")
        print("These will be the serial numbers for the components")
        serial_numbers_list = []
        for i in range(int(no_of_components)):
            i = i + 1
            serial_number = batch_number + '_' + str(i).zfill(4)
            serial_numbers_list.append(serial_number)
            print(serial_number)
        print("-----------------------------")

        # DECLARING OUR LISTS
        components_list = ["1 = Winglet Strut", "2 = Door Handle", "3 = Rudder Pin"]
        sizes_list3 = ["1 = 10mm diameter by 75mm length", "2 = 12mm diameter by 100mm length",
                       "3 = 16mm diameter by 15mm length"]

        while True:
            print(components_list)
            print("what component?")
            chosen_component = input("> ")

            # If Winglet Strut is selected do this
            if chosen_component == '1':
                print("you have selected Winglet Strut.")
                chosen_component = "Winglet Strut"
                sizes_list1 = ["1 = A320 Series", "2 = A380 Series"]
                print(sizes_list1)
                print("Please select the size of the of the component")

                size1 = input("> ")
                # If A320 series is selected do this
                if size1 == '1':
                    print("you have selected Winglet Strut A320 Series")
                    chosen_size = "A320 Series"
                    print()
                    break

                # If A380 series is selected do this
                if size1 == '2':
                    print("you have selected Winglet Strut A380 Series")
                    chosen_size = "A380 Series"
                    print()
                    break

                # re-try if invalid option
                if size1 != '1' and size1 != '2':
                    print("invalid option for Winglet strut")
                    size1 = input("> ")

                print("--------------------------------")
                break

            # If Door Handle is selected do this
            elif chosen_component == '2':
                print("you have selected the Door Handle")
                chosen_component = "Door Handle"
                chosen_size = "Universal size"
                break

            # If Rudder Pin is selected do this
            elif chosen_component == '3':
                print("you have selected Rudder Pin")
                chosen_component = "Rudder Pin"
                print(sizes_list3)
                print("Please select the size of the of the component")

                size3 = input("> ")
                # If size is 10mm by 75mm do this
                if size3 == '1':
                    print("you have selected Rudder Pin 10mm diameter by 75mm length")
                    chosen_size = "10mm by 75mm"
                    print()
                    break
                # If size is 12mm by 100mm do this
                elif size3 == '2':
                    print("you have selected Rudder Pin 12mm diameter by 100mm length")
                    chosen_size = "12mm by 100mm"
                    print()
                    break

                # If size is 16mm by 150mm do this
                elif size3 == '3':
                    print("you have selected Rudder Pin 16mm diameter by 150mm length")
                    chosen_size = "16mm by 150mm"
                    break

                # re-try if invalid option was selected
                else:
                    print("invalid option for Rudder Pin size")
                    size3 = input("> ")
                    print("-------------------------------")
            # re-try if invalid option
            else:
                print("invalid option for Component")
                chosen_component = input("> ")

        # Print some sort of confirmation and then return to main menu

        # Confirm the details are correct, print out all the order

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

            # if 1 is selected add new data to files
            if correct_option == '1':
                with open('data.json', 'w') as f:
                    json.dump(batch_count, f)

                batch = Batch
                component = Component

                list_data_batch.append(batch_number)
                print(list_data_batch)

                with open('list_data_batch.json', 'w') as f:
                    json.dump(list_data_batch, f)

                # pickle file
                with open(str(batch_number) + '.pickle', 'wb') as batch_file:
                    pickle.dump(batch, batch_file)

                    component = Component
                for i in range(int(no_of_components)):
                    i = i + 1

                    component_number = batch_number + str(i).zfill(4)
                    list_data_component.append(component_number)

                with open(component_number + '.pickle', 'wb') as component_file:
                    pickle.dump(component_number, component_file)
                    break

            # if details arent incorrect start a new batch
            elif correct_option == '0':
                print(2)
                continue

            # if choice was invalid re-ask
            else:
                print("invalid choice")

        print("Reached end of program")

    # if choice selected is 2 then list all batch numbers
    elif choice == '2':
        batch_print = list_data_batch
        print("listing all batches")
        print(batch_print)

    # if choice selected is 3 then list details of a batch
    elif choice == '3':

        # ask for batch number
        batch_number = str(input("Enter batch number: "))

        # obtain data for batch number received
        if batch_number in list_data_batch:
            batch_file = open(batch_number + '.pickle', 'rb')
            batch = pickle.load(batch_file)
            component_file = open(batch_number + '.pickle', 'rb')
            component = pickle.load(component_file)

            print("Batch number: " + batch_number)
            print("Manufacture date: " + manufacture_date)
            print("Number of components in batch: " + no_of_components)
            print("Serial numbers: " + str(serial_numbers_list))

        # if batch number is wrong re try
        else:
            print("Batch not found")

    # if choice selected is 4 then view details of a component
    elif choice == '4':
        print("View details of a component")
        serial_number = str(input("Enter component number: "))

        if component_number in list_data_batch:
            component_file = open(component_number + '.pickle', 'rb')
            component = pickle.load(component_file)

            print("Component type: " + chosen_component)
            print("Component size/fitment type: " + chosen_size)

        # if serial number is wrong re-try
        else:
            print("Component not found")

    # if choice selected is 0 then exit the program
    elif choice == '0':
        print("you have selected to exit program")
        print()
        break
    # if invalid option then ask if they want to try again
    else:
        print("invalid option")
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

