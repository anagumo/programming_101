import zoo

def test_calculate_ticket():
    ticket_free = zoo.calculate_ticket(-2)
    ticket_adult = zoo.calculate_ticket(90)

    assert ticket_free == (zoo.Ticket.FREE, 0)
    assert ticket_adult == (zoo.Ticket.RETIRED, 18)

def test_input():
    assert zoo.is_integer(90)
    assert zoo.is_integer("4")
    assert not zoo.is_integer("zsh")

def test_total_price():
    assert zoo.calculate_total_price([
        (zoo.Ticket.RETIRED, 18),
        (zoo.Ticket.CHILD, 14)]) == (32,[0,1,0,1],[0,14,0,18])
    
    assert zoo.calculate_total_price([
        (zoo.Ticket.FREE, 0),
        (zoo.Ticket.CHILD, 14),
        (zoo.Ticket.CHILD, 14),
        (zoo.Ticket.ADULT, 23,)]) == (51,[1,2,1,0],[0,28,23,0])