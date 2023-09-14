# main.py
from ticket_system import submit_ticket, respond_to_ticket, reopen_ticket, print_tickets, display_stats

# Main loop
while True:
    # Get input from the user
    action = input("Please select an action: Submit ticket (1), Respond to ticket (2), Reopen ticket (3), Print tickets (4), Display tickets stats (5), Exit (6): ")

    # Call appropriate function based on input
    if action == "1":
        submit_ticket()
    elif action == "2":
        respond_to_ticket()
    elif action == "3":
        reopen_ticket()
    elif action == "4":
        print_tickets()
    elif action == "5":
        display_stats()
    elif action == "6":
        break
    else:
        print("Invalid")
