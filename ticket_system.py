# ticket_system.py

# Global variables
tickets_resolved = 0
tickets_to_solve = 0
tickets_created = 0
ticket_counter = 1
tickets = []

# Function to respond to a ticket
def respond_to_ticket():
    global tickets_resolved, tickets_to_solve, tickets_created, ticket_counter

    # Get input from the user
    ticket_number = int(input("Please enter the ticket number: "))
    print("Type: Problem resolved/ On progress/ On hold")
    response = input("Please enter your response: ")

    # Find the ticket in the list and update response and status
    for ticket in tickets:
        if ticket["ticket_number"] == ticket_number:
            ticket["response"] = response
            if ticket["response"] != "Problem resolved":
                ticket["status"] = "Open"
                print("Response submitted")
            else:
                ticket["status"] = "Closed"
                tickets_resolved += 1
                tickets_to_solve -= 1

# Function to reopen a ticket
def reopen_ticket():
    global tickets_resolved, tickets_to_solve, tickets_created, ticket_counter

    # Get input from the user
    ticket_number = int(input("Please enter the ticket number: "))

    # Find the ticket in the list and update the status
    for ticket in tickets:
        if ticket["ticket_number"] == ticket_number:
            ticket["status"] = "Open"
            tickets_resolved -= 1
            tickets_to_solve += 1

# Function to print ticket information
def print_tickets():
    for ticket in tickets:
        print(f"Ticket Number: {ticket['ticket_number']}")
        print(f"Ticket Creator: {ticket['creator_name']}")
        print(f"Staff ID: {ticket['staff_id']}")
        print(f"Email Address: {ticket['contact_email']}")
        print(f"Description: {ticket['description']}")
        print(f"Response: {ticket['response']}")
        print(f"Ticket Status: {ticket['status']}\n")

# Function to display ticket stats
def display_stats():
    global tickets_resolved, tickets_to_solve, tickets_created, ticket_counter
    print("Resolved tickets: ", tickets_resolved)
    print("Open tickets: ", tickets_to_solve)
    print("Submitted tickets: ", tickets_created)

# Function to submit a ticket
def submit_ticket():
    global tickets_resolved, tickets_to_solve, tickets_created, ticket_counter

    # Get input from the user
    creator_name = input("Please enter your name: ")
    staff_id = input("Please enter your staff ID: ")
    contact_email = input("Please enter your contact email: ")
    description = input("Please enter the description of the issue: ")

    # Create a new ticket dictionary
    new_ticket = {
        "ticket_number": ticket_counter,
        "creator_name": creator_name,
        "staff_id": staff_id,
        "contact_email": contact_email,
        "description": description,
        "response": "",
        "status": "Open"
    }

    # Add the new ticket to the list of tickets
    tickets.append(new_ticket)

    # Update counters
    ticket_counter += 1
    tickets_created += 1
