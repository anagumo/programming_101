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
    Ticket.FREE: {'price': 0, 'e_umbral': 3},
    Ticket.CHILD: {'price': 14, 'e_umbral': 13},
    Ticket.ADULT: {'price': 23, 'e_umbral': 65},
    Ticket.RETIRED: {'price': 18, 'e_umbral': float('inf')}
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
        Ticket.FREE: {'count': 0, 'desc': "Children (<2 years old)"},
        Ticket.CHILD: {'count': 0, 'desc': "Children (3-12 years old)"},
        Ticket.ADULT: {'count': 0, 'desc': "Adult (13-64 years old)"},
        Ticket.RETIRED: {'count': 0, 'desc': "Retired (65+ years old)"}
    }
    
    for ticket_type, price in total_tickets:
        total_price = total_price + price
        invoice[ticket_type]['count'] = invoice[ticket_type]['count'] + 1
        
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
        invoice_details = f"Total price of the group: {total_price:.2f}€\nDetails for age:\n" + invoice_details
        for ticket_key in invoice:
            desc = invoice[ticket_key]['desc']
            count = invoice[ticket_key]['count']
            price = tickets[ticket_key]['price']
            ticket_desc = f"{desc}: {count} x {price:.2f}€ = {count * price:.2f}€\n"
            invoice_details = invoice_details + ticket_desc
    else:
        invoice_details = "¡See you!"

    return invoice_details

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
print(get_invoice_desc(total_price_details))