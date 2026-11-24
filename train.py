import datetime


# 1. Passenger Class
class Passenger:
    def ___init__(self, name, age, gender, phone):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone


# 2. Train Class
class Train:
    def __init__(self, train_num, train_name, source,
                 destination, total_seats):

        self.train_num = train_num
        self.train_name = train_name
        self.source = source
        self.destination = destination
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.waiting_list = []

    # Book Ticket
    def book_ticket(self, passenger):

        ticket = Ticket(self, passenger)

        if self.available_seats > 0:
            self.available_seats -= 1
            ticket.status = "CONFIRMED"
        #else:
            ticket.status = "WAITING"
            self.waiting_list.append(ticket)

        return ticket

    # Cancel Ticket
    def cancel_ticket(self, ticket):

        if ticket.status == "CANCELLED":
            return "Already Cancelled"

        if ticket.status == "WAITING":
            self.waiting_list.remove(ticket)

        elif ticket.status == "CONFIRMED":

            if self.waiting_list:
                next_ticket = self.waiting_list.pop(0)
                next_ticket.status = "CONFIRMED"
                print("Waiting List Passenger Confirmed!")
                print("PNR:", next_ticket.pnr)
        #else:
                self.available_seats += 1

        ticket.status = "CANCELLED"
        return "Ticket Cancelled Successfully"


# 3. Ticket Class
class Ticket:

    next_pnr = 100001

    def __init__(self, train, passenger):

        self.pnr = Ticket.next_pnr
        Ticket.next_pnr += 1

        self.train = train
        self.passenger = passenger
        self.booking_date = datetime.datetime.now()
        self.status = "PENDING"

    # Display Ticket
    def display_info(self):

        print("\n========== TICKET DETAILS ==========")

        print("PNR Number:", self.pnr)
        print("Train Number:", self.train.train_num)
        print("Train Name:", self.train.train_name)
        print("Source:", self.train.source)
        print("Destination:", self.train.destination)

        print("Passenger Name:", self.passenger.name)
        print("Age:", self.passenger.age)
        print("Gender:", self.passenger.gender)
        print("Phone:", self.passenger.phone)

        print("Booking Date:",
              self.booking_date.strftime("%d-%m-%Y %I:%M %p"))

        print("Status:", self.status)

        if self.status == "WAITING":
            position = self.train.waiting_list.index(self) + 1
            print("Waiting List Position:", position)

        print("====================================")


# 4. Create Train Objects
trains = [

    Train(101, "Express", "Hyderabad",
          "Chennai", 3),

    Train(102, "Super Fast", "Hyderabad",
          "Bangalore", 2),

    Train(103, "Passenger Express", "Vijayawada",
          "Hyderabad", 4)
]



# Store All Tickets
tickets = {}


# 5. Display Available Trains
def show_trains():

    print("\n========== AVAILABLE TRAINS ==========")

    for train in trains:

        print("\nTrain Number:", train.train_num)
        print("Train Name:", train.train_name)
        print("Source:", train.source)
        print("Destination:", train.destination)
        print("Total Seats:", train.total_seats)
        print("Available Seats:", train.available_seats)
        print("Waiting List:", len(train.waiting_list))


# 6. Get Passenger Details
def get_passenger():

    while True:

        try:

            name = input("Enter Passenger Name: ").strip()

            if not name:
                raise ValueError("Name cannot be empty")

            age = int(input("Enter Age: "))

            if age <= 0 or age > 120:
                raise ValueError("Invalid Age")

            gender = input("Enter Gender: ").strip()

            if not gender:
                raise ValueError("Gender cannot be empty")
            phone = input("Enter Phone Number: ").strip()

            if len(phone) != 10 or not phone.isdigit():
                raise ValueError("Enter valid 10 digit phone number")

            return Passenger(name, age, gender, phone)

        except ValueError as e:

            print("Invalid Input:", e)


# 7. Book Tickets
def book_tickets():

    show_trains()

    try:

        train_num = int(input("\nEnter Train Number: "))

        train = None

        for t in trains:

            if t.train_num == train_num:
                train = t
                break

        if train is None:
            print("Invalid Train Number.")
            return

        num_tickets = int(input("Enter Number of Tickets: "))

        if num_tickets <= 0 or num_tickets > 6:
            print("Enter tickets between 1 and 6.")
            return

        for i in range(num_tickets):

            print("\nPassenger", i + 1)

            passenger = get_passenger()

            ticket = train.book_ticket(passenger)

            tickets[str(ticket.pnr)] = ticket

            print("\nBooking Status:", ticket.status)
            print("PNR Number:", ticket.pnr)

        print("\nBooking Process Completed!")

    except ValueError:
        print("Please enter valid numbers.")


# 8. Search Ticket Using PNR
def search_ticket():

    pnr = input("Enter PNR Number: ").strip()

    ticket = tickets.get(pnr)

    if ticket is None:
        print("Invalid PNR Number.")
    else:
     ticket.display_info()


# 9. Cancel Ticket
def cancel_ticket():

    pnr = input("Enter PNR Number to Cancel: ").strip()

    ticket = tickets.get(pnr)

    if ticket is None:
        print("Invalid PNR Number.")
        return

    result = ticket.train.cancel_ticket(ticket)

    print(result)


# 10. Main Menu
def main():

    while True:

        print("\n================================")
        print("     TRAIN TICKET BOOKING")
        print("================================")

        print("1. Show Available Trains")
        print("2. Book Tickets")
        print("3. Search Ticket")
        print("4. Cancel Ticket")
        print("5. Exit")

        choice = input("\nEnter Your Choice: ").strip()

        if choice == "1":

            show_trains()

        elif choice == "2":

            book_tickets()

        elif choice == "3":

            search_ticket()

        elif choice == "4":

            cancel_ticket()

        elif choice == "5":

             print("\nThank You!")
             print("Safe Journey!")
             break

    else:

            print("Invalid Choice. Try Again.")


# 11. Run Program
if __name__ == "__main__":
 main()