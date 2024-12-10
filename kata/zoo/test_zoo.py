import zoo

def test_calculate_ticket():
    ticket = zoo.calculate_ticket(90)

    assert ticket == (zoo.Ticket.RETIRED, 18)
