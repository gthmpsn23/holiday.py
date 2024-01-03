"""First, get the following user inputs:
○ city_flight: The city they will be flying to. (You can create some options for them. Remember each city will have different flight costs.)
○ num_nights: The number of nights they will be staying at a hotel
○ rental_days: The number of days for which they will be hiring a
car.

Next, create the following four functions:
● hotel_cost: This function will take num_nights as an argument, and return a total cost for the hotel stay (you can choose the price per night charged at the hotel).
 
● plane_cost: This function will take city_flight as an argument and return a cost for the flight. (Hint: use if/else if statements in the function to retrieve a price based on the chosen city.)
● car_rental: This function will take rental_days as an argument and return the total cost of the car rental (you can choose the daily rental cost.)
● holiday_cost: This function will take the three arguments hotel_cost, plane_cost, car_rental. Using these three arguments, you can call all three of the above functions with respective arguments and finally return a total cost for your holiday.


"""

# List of destinations

destinations = [
{'Name': 'Berlin', 'hotel_cost': 80, 'plane_cost': 200, 'car_rental': 30},
{'Name': 'Paris', 'hotel_cost': 100, 'plane_cost': 250, 'car_rental': 55},
{'Name': 'Rome', 'hotel_cost': 75, 'plane_cost': 300, 'car_rental': 25},
{'Name': 'Barcelona', 'hotel_cost': 95, 'plane_cost': 150, 'car_rental': 35},
{'Name': 'Krakow', 'hotel_cost': 55, 'plane_cost': 125, 'car_rental': 15},
]

# Function that loops through dictionary to find relevant information on destinations

def find_destination(destination_name):
   for destination in destinations:
      if destination['Name'].lower() == destination_name.lower():
         return destination
   return None


#Function that calculates the cost of the hotel, multiplies the price per night by amount of nights 

def hotel_cost(destination_name, num_nights):
    destination = find_destination(destination_name)
    if destination:
       return destination['hotel_cost'] * num_nights



# function that returns the flight cost

def plane_cost(destination_name):
   destination = find_destination(destination_name)
   if destination: 
      return destination['plane_cost']


# Function that calculates the car rental cost

def car_rental(destination_name, rental_days):
   destination = find_destination(destination_name)
   if destination:
      return destination['car_rental']
 

      
# Function that calculates the total cost of the holiday

def holiday_cost(hotel_total_cost, total_plane_cost, car_rental_cost):
   total_holiday_cost = hotel_total_cost + total_plane_cost + car_rental_cost
   return total_holiday_cost
   


print("Welcome to City Breaks R US!\n")

print("Please select from the list of destinations:\n")

for destination in destinations:
   print(destination['Name'])


# Prints list of destinations

# print("Please select your destination from the following options:", ", ".join(destinations))

# Handles user input and ensures they input a valid destinations, returns error if they don't

while True:
    city_flights = input("Enter your destination: ")
   
    if city_flights.lower() in [destination['Name'].lower() for destination in destinations]:
     print(f"Great choice, Preparing for your trip to {city_flights}......")
     break
    else:
       print("Please enter a valid destination.")

   
# Handles user input for num_night and rental_days, returns error for incorrect input.

while True:
    try:
     num_nights = int(input("\nEnter how many days you will be visiting for: "))
     rental_days = int(input("\nEnter how many days you will like to hire a car for: "))
     break
    except ValueError:
       print("Please enter a valid number")

# Prints the total hotel cost according to the number of nights

hotel_total_cost = hotel_cost(city_flights, num_nights)

print(f"\nThe Hotel Cost for {num_nights} nights in {city_flights} is: £{hotel_total_cost}\n")

# Prints the total plane cost

total_plane_cost = plane_cost(city_flights)
print(f"Your flights are: £{total_plane_cost}\n")

# prints car rental cost, returns "No car required if the user types 0"

car_rental_cost = 0

while True:
   if rental_days == 0:
        print("No car required.\n")
        break
   else:
        car_rental_cost = car_rental(city_flights, rental_days)
        print(f"Your car rental will be: £{car_rental_cost}\n")
        break
   
# Calculates the total cost of the holiday

total_holiday_cost = holiday_cost(hotel_total_cost, total_plane_cost, car_rental_cost)
print(f"The total cost for your holiday is: £{total_holiday_cost}")

print("\nThank you for using City Breaks R US!")