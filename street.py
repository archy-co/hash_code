class Street:
    def __init__(self, start, end, name, time_to_cross, queue=None):
        self.start = start
        self.end = end
        self.name = name
        self.time_to_cross = time_to_cross
        self.queue = queue



def get_perfect_time(streets):
    perfect_time = 0
    for street in streets[1:]:
        perfect_time += street.time_to_cross

    return perfect_time

