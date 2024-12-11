import zoo

def test_calculate_ticket():
    ticket_free = zoo.calculate_ticket(-2)
    ticket_retired = zoo.calculate_ticket(90)

    assert ticket_free == (zoo.Ticket.FREE, 0), "Ticket do not match"
    assert ticket_retired == (zoo.Ticket.RETIRED, 18), "Ticket do not match"

def test_input():
    assert zoo.is_integer(90)
    assert zoo.is_integer("4")
    assert not zoo.is_integer("zsh")

def test_total_price():
    total_tickets = [(zoo.Ticket.RETIRED, 18),
                     (zoo.Ticket.CHILD, 14),
                     (zoo.Ticket.CHILD, 14),
                     (zoo.Ticket.ADULT, 23)]
    invoice = {zoo.Ticket.FREE: {'count': 0, 'desc': "Children (<2 years old)"},
               zoo.Ticket.CHILD: {'count': 2, 'desc': "Children (3-12 years old)"},
               zoo.Ticket.ADULT: {'count': 1, 'desc': "Adult (13-64 years old)"},
               zoo.Ticket.RETIRED: {'count': 1, 'desc': "Retired (65+ years old)"}}
    assert zoo.calculate_total_price(total_tickets) == (69, invoice), "Invoice do not match"

def test_invoice_desc():
    total_tickets = [(zoo.Ticket.CHILD, 14),
                     (zoo.Ticket.CHILD, 14),
                     (zoo.Ticket.ADULT, 23)]
    total_price_details = zoo.calculate_total_price(total_tickets)
    actual_invoice_desc = zoo.get_invoice_desc(total_price_details)
    expected_invoice_desc = "Total price of the group: 51.00€\nDetails for age:\nChildren (<2 years old): 0 x 0.00€ = 0.00€\nChildren (3-12 years old): 2 x 14.00€ = 28.00€\nAdult (13-64 years old): 1 x 23.00€ = 23.00€\nRetired (65+ years old): 0 x 18.00€ = 0.00€"
    assert not actual_invoice_desc == expected_invoice_desc, "Strings do not match"