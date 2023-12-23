# Define constants
BOAT_COUNT = 10 #you can increase boaTs count
BOAT_HIRE_COST_PER_HOUR = 20
BOAT_HIRE_COST_PER_HALF_HOUR = 12
OPENING_TIME = 10
CLOSING_TIME = 17

# Initialize data structures to store boat information
boat_data = []
for boat_number in range(1, BOAT_COUNT + 1):
    boat_data.append({
        'boat_number': boat_number,
        'total_money_taken': 0,
        'total_hours_hired': 0,
        'next_available_time': OPENING_TIME,
    })

# Task 1: Calculate money taken for one boat
def calculate_money_taken(boat):
    hire_duration = float(input(f"Enter the hire duration for Boat {boat['boat_number']} (in hours): "))
    
    if hire_duration <= 0:
        print("Invalid input. Hire duration must be positive.")
        return
    
    if boat['next_available_time'] + hire_duration > CLOSING_TIME:
        print(f"Boat {boat['boat_number']} cannot be hired for that duration at this time.")
        return
    
    if hire_duration >= 1:
        cost = BOAT_HIRE_COST_PER_HOUR * hire_duration  #calculate cost for 1 hour
    else:
        cost = BOAT_HIRE_COST_PER_HALF_HOUR * (hire_duration * 2) #calculate cost for half hour
    
    boat['total_money_taken'] += cost
    boat['total_hours_hired'] += hire_duration
    boat['next_available_time'] += hire_duration

# Task 2: Find the next available boat
def find_next_available_boat(current_time):
    available_boats = [boat for boat in boat_data if boat['next_available_time'] <= current_time]
    
    if not available_boats:
        earliest_available_time = min(boat['next_available_time'] for boat in boat_data)
        print(f"No boats available right now. Next available time is at {earliest_available_time:.2f} o'clock.")
    else:
        print(f"{len(available_boats)} boats are available for hire right now.")
        for boat in available_boats:
            print(f"Boat {boat['boat_number']} is available for hire.")

# Task 3: Calculate money taken for all boats at the end of the day
def calculate_total_money_taken():
    total_money = sum(boat['total_money_taken'] for boat in boat_data)
    total_hours_hired = sum(boat['total_hours_hired'] for boat in boat_data)
    unused_boats = [boat for boat in boat_data if boat['total_hours_hired'] == 0]
    most_used_boat = max(boat_data, key=lambda boat: boat['total_hours_hired'])
    
    print(f"Total money taken for all boats today: ${total_money:.2f}")
    print(f"Total number of hours boats were hired today: {total_hours_hired:.2f}")
    print(f"Number of boats not used today: {len(unused_boats)}")
    print(f"Boat {most_used_boat['boat_number']} was used the most today with {most_used_boat['total_hours_hired']:.2f} hours.")

# Main program loop
while True:
    current_time = float(input("Enter the current time (24-hour format, e.g., 10.30 for 10:30 AM): "))
    
    if current_time < OPENING_TIME or current_time >= CLOSING_TIME:
        print("The boat hire service is closed at this time.")
        break
    
    option = input("Select an option (1 - Calculate money for one boat, 2 - Find next available boat, 3 - End of day report, 4 - Quit): ")
    
    if option == '1':
        boat_number = int(input("Enter the boat number: "))
        if 1 <= boat_number <= BOAT_COUNT:
            calculate_money_taken(boat_data[boat_number - 1])
        else:
            print("Invalid boat number.")
    elif option == '2':
        find_next_available_boat(current_time)
    elif option == '3':
        calculate_total_money_taken()
    elif option == '4':
        break
    else:
        print("Invalid option. Please select a valid option (1-4).")

