from street import Street
from car import Car
from algorithm import find_min_schedule

def solve(input_path, output_path):

    cars_list = []
    streets_dict = {}

    with open(input_path, 'r') as infile:
        sim_dur, num_inter, num_streets, num_cars, score_per_car = map(int, infile.readline().split())

        for _ in range(num_streets):
            start_inter, end_inter, name_street, time_to_cross = infile.readline().split()
            start_inter, end_inter, time_to_cross = map(int, (start_inter, end_inter, time_to_cross))

            streets_dict[name_street] = Street(start_inter, end_inter, name_street, time_to_cross)

        for _ in range(num_cars):
            num_streets_for_car, streets = infile.readline().split(sep=' ', maxsplit=1)
            num_streets_for_car = int(num_streets_for_car)
            streets = [streets_dict[street_name] for street_name in streets.split()]

            cars_list.append(Car(streets))

    intersections_infos = find_min_schedule(streets_dict, cars_list, sim_dur, num_inter, score_per_car)

    with open(output_path, 'w') as outfile:
        num_inter = sum(map(bool, intersections_infos))
        print(num_inter, file=outfile)

        for idx, intersection in enumerate(intersections_infos):
            # TODO: implement output info for a schedule
            if intersection:
                print(idx, file=outfile)
                print(len(intersection), file=outfile)
                for street, num_cars_passed in intersection.items():
                    print(street, num_cars_passed, file=outfile)


if __name__ == "__main__":
    solve("b.txt", 'out_b.txt')
