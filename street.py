class Street:
    def __init__(self, start, end, name, time_to_cross, queue_length=0):
        self.start = start
        self.end = end
        self.name = name
        self.time_to_cross = time_to_cross
        self.queue_length = queue_length

            


def get_perfect_time(streets):
    perfect_time = 0
    for street in streets[1:]:
        perfect_time += street.time_to_cross

    return perfect_time

