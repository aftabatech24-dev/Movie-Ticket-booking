from random import randint

movies={
    "Avengers":250,
    "Pushpa":100,
    "KGF":300,
    "Sultan":150
}
seats=["a1","a2","a3","a4","a5","m1","m2","m3","m4","m5"]
history=[]
print("Welcome to Movie Ticket Booking System")
def Show_Movies():
    for movie,price in movies.items():
        print(f"{movie} : ₹{price}")
def Book_ticket():
    found=False
    Movie_name=input("Enter movie name to book : ")
    tickets=int(input("Enter number of tickets to book :"))
    print("Available Seats :")
    for seat in seats:
        print(seat, end=" ")
    print()

    selected_seats = input("Enter the seat numbers you want to book (comma separated): ").replace(" ", "").split(",")
    if len(selected_seats) != tickets:
        print("Selected seats must be equal to booked tickets")
        return

    for seat in selected_seats:
        if seat not in seats:
            print(f"Invalid seat selected: {seat}. Please select available seats.")
            return

    for seat in selected_seats:
        seats.remove(seat)

    Booking_id = randint(100, 999)
    for movie, price in movies.items():
        if Movie_name.lower() == movie.lower():
            total = tickets * price
            print(f"Total Amount ₹{total}")
            history.append(f"id{Booking_id} {Movie_name} * {tickets} = {total} Seats booked: {', '.join(selected_seats)}")
            found = True
            break

    if not found:
        print("Invalid movie Name.")
        return
    else:
        print("Ticket booked successfully")
        return total
def Cancel_ticket():
    found=False
    Movie_name=input("Enter movie name to cancel : ")
    tickets=int(input("Enter number of tickets to cancel :"))
    selected_seats = input("Enter the seat numbers you want to cancel (comma separated): ").replace(" ", "").split(",")
    if len(selected_seats) != tickets:
        print("Selected seats must be equal to cancelled tickets")
        return

    for seat in selected_seats:
        if seat in seats:
            print(f"Seat {seat} is not booked. Cannot cancel.")
            return

    for seat in selected_seats:
        seats.append(seat)

    for movie, price in movies.items():
        if Movie_name.lower() == movie.lower():
            total = tickets * price
            history.append(f"Cancelled {Movie_name} * {tickets} = {total} Seats cancelled: {', '.join(selected_seats)}")
            print(f"Cancelled {Movie_name} * {tickets} = {total}")
            found = True
            break

    if not found:
        print("Invalid movie Name.")
        return
    else:
        print("Ticket cancelled successfully")
def Show_History():
    print("Booking History:")
    if len(history) == 0:
        print("No booking found")
        return
    for records in history:
        print(records)
def menu():
    print("1. Show Movies")
    print("2. Book Ticket")
    print("3. Cancel Ticket")
    print("4. Show Booking History")  
    print("5. Exit")
while True:
    menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        Show_Movies()
    elif choice == "2":
        Book_ticket()
    elif choice == "3":
        Cancel_ticket()
    elif choice == "4":
        Show_History()
    elif choice == "5":
        print("Thank you for using the Movie Ticket Booking System.")
        break
    else:
        print("Invalid choice. Please try again.")      