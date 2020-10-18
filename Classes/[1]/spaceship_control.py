MAX_FUEL = 1000
REAL_PASSWORD = '123456'
HELLO_MESSAGE = """
WELCOME TO PIGEON SPACECRAFT CONTROL PANEL
===========================================
List of Commands:
[0] Set Destination
[1] Manage Fuel
[2] Manage Passengers
[3] Broadcast
[4] Launch Spacecraft
[5] Quit Control Panel
"""
FUEL_PER_TRIP = 500

destination = 'Earth'
status = 'Arrived'
fuel = 0
passengers = ['Spacecraft AI']

# Password Confirmation
password = input('Please Enter Password: ')
if password != REAL_PASSWORD:
    print('Wrong password, exiting...')
else:
    while True:
        print(HELLO_MESSAGE)
        print('Current Status:', status)
        command = input('Enter Command: ')
        if command == '0':
            print('Current Destination:', destination)
            new_destination = input('Enter New Destination: ')
            if new_destination != destination:
                destination = new_destination
                status = 'Not Launched'
                print('Successfully changed destination to', new_destination)
            else:
                print('Same with current destination. Nothing is changed')
        elif command == '1':
            print('Current Fuel:', fuel)
            print('Max Fuel:', MAX_FUEL)
            if fuel < MAX_FUEL:
                add_amount = int(input('Add how much fuel?'))

                if add_amount >= MAX_FUEL-fuel:
                    fuel = MAX_FUEL
                    print('Fuel set to max amount.')
                else:
                    fuel += add_amount
                    print('Fuel added.')
            else:
                print('Fuel full. Cannot add fuel.')
        elif command == '2':
            print('Current passengers:', ', '.join(passengers))
            if input('Add passenger? (y/n) ') == 'y':
                new_passenger = input('Enter New Passenger, "e" to exit: ')
                while new_passenger != 'e':
                    passengers.append(new_passenger)
                    print('Passenger added.')
                    new_passenger = input('Enter New Passenger, "e" to exit: ')
            if input('Delete passenger? (y/n) ') == 'y':
                passenger_to_delete = input('Enter Name of Passenger, "e" to exit: ')
                while passenger_to_delete != 'e':
                    passengers.remove(passenger_to_delete)
                    print('Passenger deleted')
                    passenger_to_delete = input('Enter Name of Passenger, "e" to exit: ')
        elif command == '3':
            message = input('Type broadcast message: ')
            for passenger in passengers:
                print(message, passenger)
        elif command == '4':
            if status == 'Arrived':
                print('Cannot launch. Already Arrived.')
            elif fuel < FUEL_PER_TRIP:
                print('Not enough fuel.')
            else:
                print('Spacecraft launched.')
                print('Traveling to', destination, '...')
                fuel -= 500
                status = 'Arrived'
                print('Arrived at', destination)
        elif command == '5':
            print('Exiting...')
            break
        else:
            print('Unknown Command.')

