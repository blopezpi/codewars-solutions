def number(bus_stops):
    persons = 0
    for stop in bus_stops:
        persons += stop[0]
        persons -= stop[1]
    return persons
