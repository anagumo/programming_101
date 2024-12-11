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

tickets = {
    Ticket.FREE: {"price": 0, "e_umbral": 3, "desc": "Children (<2 years old)"},
    Ticket.CHILD: {"price": 14, "e_umbral": 13, "desc": "Children (3-12 years old)"},
    Ticket.ADULT: {"price": 65, "e_umbral": 23, "desc": "Adult (13-64 years old)"},
    Ticket.RETIRED: {"price": 18, "e_umbral": float('inf'), "desc": "Retired (65+ years old)"}
}
total_tickets = []

def calculate_ticket(age:int) -> Tuple[Ticket, int]:
    """
    Pure and total function that takes a number as input and returns a tuple
    grouping the type of ticket and the price.
    Corner cases:
    - If the input is a negative number, the function should return Ticke.Free, 0
    """
    type = Ticket.FREE
    price = 0

    for type in tickets:
        if age < tickets[type]['e_umbral']:
            price = tickets[type]['price']
            break

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

def calculate_total_price(total_tickets: Tuple[Ticket, int]) -> Tuple[int, dict]:
    """
    Conversor function that takes a tuple as input and returns another one.
    The new tuple should include the total price, total tickets by group and sobtotal by group.
    """
    total_price = 0
    invoice = {
        Ticket.FREE: 0,
        Ticket.CHILD: 0,
        Ticket.ADULT: 0,
        Ticket.RETIRED: 0
    }
    
    for type, price in total_tickets:
        total_price = total_price + price
        invoice[type] = invoice[type] + 1
        
    return total_price, invoice

def get_invoice_desc(total_price_details: Tuple[int, dict]) -> int:
    """
    Conversor function that takes a tuple as input and returns a string.
    The string should concatente the price information of each ticket.
    Corner cases:
    - If the total price is equal to zero, the function should return an empty string
    - If the tickets by group is equal to zero, the function should not display the list
    """
    total_price, invoice = total_price_details
    invoice_details = ""

    if total_price > 0:
        invoice_details = f"Total price of the group: {total_price:.2f} euros\nDetails for age:\n" + invoice_details
        for ticket_key in invoice:
            ticket_desc = f"{tickets[ticket_key]['desc']}: {invoice[ticket_key]} x {tickets[ticket_key]['price']} euros = {invoice[ticket_key] * tickets[ticket_key]['price']} euros\n"
            invoice_details = invoice_details + ticket_desc
    else:
        invoice_details = "¡See you!"

    return invoice

PROMPT = "Enter the age of visitor (Leave empty to continue):"
print(PROMPT)

while True:
    response = input()

    if response == "":
        break
    elif is_integer(response):
        ticket = calculate_ticket(int(response))
        total_tickets.append(ticket)

total_price_details = calculate_total_price(total_tickets)
print(total_price_details)