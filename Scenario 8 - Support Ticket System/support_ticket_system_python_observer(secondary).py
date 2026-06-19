# Observer

# What is being observed (subject)
# Whenever a ticket is created, all subscribed observers are notified
class TicketSystem:
    def __init__(self):
        self.observers = []

    # Allows support levels to subscribe to ticket events
    def subscribe(self, observer):
        self.observers.append(observer)

    # Notifies every subscribed observer about the event
    def notify(self, ticket):
        for observer in self.observers:
            observer.update(ticket)

    # Creates a ticket and informs all observers.
    def create_ticket(self, ticket):
        print(f"{ticket.category.capitalize()} ticket created")
        self.notify(ticket)


# Mocked staff handling functions (identical to the Chain of Responsibility implementation)
# In a real application this is where each level of staff would be able to close or talk to the user for example
def level_1_staff_mock(ticket):
    print("Handled by Level 1 staff")
    print(f"Ticket with description: {ticket.description}")
    print("")

def level_2_staff_mock(ticket):
    print("Handled by Level 2 staff")
    print(f"Ticket with description: {ticket.description}")
    print("")

def level_3_staff_mock(ticket):
    print("Handled by Level 3 staff")
    print(f"Ticket with description: {ticket.description}")
    print("")


# Different support level observers
class Level_1_Observer:
    def update(self, ticket):
        if ticket.category == "simple":
            level_1_staff_mock(ticket)
        else:
            print("Level 1 ignored ticket")


class Level_2_Observer:
    def update(self, ticket):
        if ticket.category == "complex":
            level_2_staff_mock(ticket)
        else:
            print("Level 2 ignored ticket")


class Level_3_Observer:
    def update(self, ticket):
        if ticket.category == "management":
            level_3_staff_mock(ticket)
        else:
            print("Level 3 ignored ticket")


# Ticket information (identical to the Chain of Responsibility implementation)
class Ticket:
    def __init__(self, category, description):
        self.category = category
        self.description = description

def create_ticket_structure():
    simple_ticket = Ticket("simple", "A user can't find the power button on their PC.")
    complex_ticket = Ticket("complex", "A user has accidentally downloaded multiple viruses.")
    management_ticket = Ticket("management", "A shareholder wants to sell all of their shares!")
    unknown_ticket = Ticket("unknown", "t̴h̸e̵ ̷s̵t̴a̵r̴s̷ ̶a̴r̵e̴ ̶n̵o̷t̷ ̵w̵h̶a̶t̶ ̵t̵h̶e̵y̷ ̷s̸e̴e̷m̴")
    return simple_ticket, complex_ticket, management_ticket, unknown_ticket

if __name__ == "__main__":
    # Create ticket system subject
    ticket_system = TicketSystem()
    
    # create example ticket types
    simple_ticket, complex_ticket, management_ticket, unknown_ticket = create_ticket_structure()

    # Support levels subscribe to ticket creation events
    ticket_system.subscribe(Level_1_Observer())
    ticket_system.subscribe(Level_2_Observer())
    ticket_system.subscribe(Level_3_Observer())

    ticket_system.create_ticket(simple_ticket)
    print("\n\n")
    
    ticket_system.create_ticket(complex_ticket)
    print("\n\n")
    
    ticket_system.create_ticket(management_ticket)
    print("\n\n")
    
    ticket_system.create_ticket(unknown_ticket)
    print("\n\n")