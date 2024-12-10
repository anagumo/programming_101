
from enum import Enum
from typing import Tuple

# You can be efficient when you are already effective

"""
    Impure/async function that does not takes arguments as input but interactues with the user 
    to calculate the price of the zoo ticket.
"""

class Ticket(Enum):
    FREE = 1
    CHILD = 2
    ADULT = 3
    RETIRED = 4

tickets = []

def calculate_ticket(age:int) -> Tuple[int, Ticket, int]:
    """
    Pure and total function that takes a number as input and returns a tuple
    grouping the type of ticket and the price.
    Corner cases:
    - If the input is a negative number, the function should return Ticke.Free, 0
    """
    type = Ticket.FREE
    price = 0

    if age >= 3 and age <= 12:
        type, price = Ticket.CHILD, 14
    elif age >= 13 and age < 65:
        type, price = Ticket.ADULT, 23
    elif age >= 65:
        type, price = Ticket.RETIRED, 18
    else:
        type, price = Ticket.FREE, 0

    return type, price

def is_integer(input_text:str) -> bool:
    """
    Predicate function that takes a string as input and checks if it is a
    postive integer.
    Corner cases:
    - If the input is not a number, the function should handle the error.
    """
    is_integer: False

    try:
        int(input_text)
        is_integer = True
    except:
        is_integer = False
    return is_integer

def calculate_total_price(tickets: Tuple[Ticket, int]) -> Tuple[int, list, list]:
    """
    Conversor function that takes a tuple as input and returns another one.
    The new tuple should include the total price, total tickets by group and sobtotal by group.
    """
    tickets_by_group = [0,0,0,0]
    subtotal_by_group = [0,0,0,0]
    total_price = 0

    for type, price in tickets:
        if type == Ticket.FREE:
            tickets_by_group[0] = tickets_by_group[0] + 1
            subtotal_by_group[0] = subtotal_by_group[0] + price
        elif type == Ticket.CHILD:
            tickets_by_group[1] = tickets_by_group[1] + 1
            subtotal_by_group[1] = subtotal_by_group[1] + price
        elif type == Ticket.ADULT:
            tickets_by_group[2] = tickets_by_group[2] + 1
            subtotal_by_group[2] = subtotal_by_group[2] + price
        elif type == Ticket.RETIRED:
            tickets_by_group[3] = tickets_by_group[3] + 1
            subtotal_by_group[3] = subtotal_by_group[3] + price
        
        total_price = total_price + price

    return total_price, tickets_by_group, subtotal_by_group

def get_invoice(total_price_details: Tuple[int, list, list]) ->int:
    """
    Conversor function that takes a tuple as input and returns a string.
    The string should concatente the price information of each ticket.
    Corner cases:
    - If the total price is equal to zero, the function should return an empty string
    - If the tickets by group is equal to zero, the function should not display the list
    """
    tickets_by_type = ["Children (<2 years old)", "Children (3-12 years old)", "Adult (13-64 years old)", "Retired (65+ years old)"]
    tickets_by_price = [0,14,23,18]
    total_price, tickets_by_group, subtotal_by_group = total_price_details
    invoice = ""

    if total_price > 0:
        invoice = f"Total price of the group: {total_price:.2f} euros\nDetails for age:\n" + invoice
        for index, tickets_by_group in enumerate(tickets_by_group):
            if tickets_by_group > 0:
                ticket_info = f"{tickets_by_type[index]}: {tickets_by_group} x {tickets_by_price[index]} euros = {subtotal_by_group[index]} euros\n"
                invoice = invoice + ticket_info
    else:
        invoice = "¡See you!"

    return invoice

PROMPT = "Enter the age of visitor (Leave empty to continue):"
print(PROMPT)

while True:
    response = input()

    if response == "":
        break
    elif is_integer(response):
        ticket = calculate_ticket(int(response))
        tickets.append(ticket)

total_price_details = calculate_total_price(tickets)