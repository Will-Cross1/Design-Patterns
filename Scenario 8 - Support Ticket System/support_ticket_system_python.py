# Chain-of-responsibility
class Handler:
    def __init__(self, next_handler=None):
        # each handler stores a reference to the next handler
        self.next_handler = next_handler

    def handle(self, ticket):
        # base logic that allows the passing of the task to the next highest in the chain
        if self.next_handler:
            self.next_handler.handle(ticket)
        else:
            print(f"No handler available for '{ticket.category}' tickets")


# Mocked staff handling functions
# In a real application this is where each level of staff would be able to close or talk to the user for example
def level_1_staff_mock(ticket):
    print("Handled by Level 1 staff")
    print(f"Ticket with description: {ticket.description}")

def level_2_staff_mock(ticket):
    print("Handled by Level 2 staff")
    print(f"Ticket with description: {ticket.description}")

def level_3_staff_mock(ticket):
    print("Handled by Level 3 staff")
    print(f"Ticket with description: {ticket.description}")


# Each support level can only know what it can handle and who is the next handler for low coupling
# Level 3 can be made to catch all remaining ticket types (by removing the if else block), but I added an option to escalate further to show what happens if there is no more handlers in the chain
# to show that even if a handler didn't work, the ticket wouldn't silently fail.
class Level_1(Handler):
    def handle(self, ticket):
        # All simple tickets are handled here
        # If a ticket is anything other than simple, it gets escalated
        if ticket.category == "simple":
            level_1_staff_mock(ticket)
        else:
            super().handle(ticket)

class Level_2(Handler):
    def handle(self, ticket):
        # All complex tickets are handled here
        # If a ticket is anything other than complex, it gets escalated
        if ticket.category == "complex":
            level_2_staff_mock(ticket)
        else:
            super().handle(ticket)

class Level_3(Handler):
    def handle(self, ticket):
        # All management tickets are handled here
        # If a ticket is anything other than management, it gets escalated
        # There are no other handlers available so a suitable error message should be displayed.
        if ticket.category == "management":
            level_3_staff_mock(ticket)
        else:
            super().handle(ticket)


# ticket class with information about each ticket
# In production, category would likely use an enum instead of a string to avoid typos.
class Ticket:
    def __init__(self, category, description):
        self.category = category
        self.description = description


# Example use prints
if __name__ == "__main__":
    # create linked complexity chain
    chain = Level_1(Level_2(Level_3()))

    # a simple ticket has been made and needs to be handled (should be sent to level 1)
    simple_ticket = Ticket("simple", "A user can't find the power button on their PC.")
    print(f"{simple_ticket.category.capitalize()} ticket created:")
    chain.handle(simple_ticket)
    print("")
    
    # a complex ticket has been made and needs to be handled (should be sent to Level 2)
    complex_ticket = Ticket("complex", "A user has accidentally downloaded multiple viruses.")
    print(f"{complex_ticket.category.capitalize()} ticket created:")
    chain.handle(complex_ticket)
    print("")
    
    # a ticket for management has been created and should be sent to level 3
    management_ticket = Ticket("management", "A shareholder wants to sell all of their shares!")
    print(f"{management_ticket.category.capitalize()} ticket created:")
    chain.handle(management_ticket)
    print("")

    # a ticket with unknown complexity has been made, should cause an error as no handler is available
    unknown_ticket = Ticket("unknown", "t̴h̸e̵ ̷s̵t̴a̵r̴s̷ ̶a̴r̵e̴ ̶n̵o̷t̷ ̵w̵h̶a̶t̶ ̵t̵h̶e̵y̷ ̷s̸e̴e̷m̴")
    print(f"{unknown_ticket.category.capitalize()} ticket created:")
    chain.handle(unknown_ticket)
    print("")