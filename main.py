def solve(input_path, output_path):
    with open(input_path, 'w') as infile:
        sim_dur, num_inter, num_streets, num_cars, score = map(int, infile.readline().split())
    
        for _ in range(num_streets):
            start_inter, end_inter, name_street, time_to_cross = infile.readline().split()
            start_inter, end_inter, time_to_cross = map(int, (start_inter, end_inter, time_to_cross))

        for _ in range(num_cars):
            num_streets_for_car, streets = infile.readline().split(maxsplit=1)
