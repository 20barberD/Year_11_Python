def ticketPrice(childTickets, adultTickets):
    return (childTickets * 8.99) + (adultTickets * 19.99) + 2.50

print(round(ticketPrice(15, 2), 2))