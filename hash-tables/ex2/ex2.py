def reconstruct_trip(tickets):
    d = {}
    flight = []

    for ticket in tickets:
        d[ticket[0]] = ticket[1]
    flight.append(d[None])

    current = d[None]

    while current is not None:
      if current in d:
        current = d[current]
        if current is not None:
          flight.append(current)
      else:
        return []
    return flight



if __name__ == '__main__':
    # You can write code here to test your implementation using the Python repl
    pass
