def solve(input_path, output_path):

    cars_list = []
    streets_list = []

    with open(input_path, 'r') as infile:
        sim_dur, num_inter, num_streets, num_cars, score = map(int, infile.readline().split())

        for _ in range(num_streets):
            start_inter, end_inter, name_street, time_to_cross = infile.readline().split()
            start_inter, end_inter, time_to_cross = map(int, (start_inter, end_inter, time_to_cross))

            streets_list.append(Street(start_inter, end_inter, name_street, time_to_cross))

        for _ in range(num_cars):
            num_streets_for_car, streets = infile.readline().split(maxsplit=1)
            num_streets_for_car = int(num_streets_for_car)
            streets = list(streets)

            cars_list.append(num_streets_for_car, streets)

    num_inter, intersections_infos = algorithm(streets_list, cars_list)

    with open(output_path, 'w') as outfile:
        print(num_inter, file=outfile)

        for intersection_info in intersections_infos:
            # TODO: implement output info for a schedule
            pass
    