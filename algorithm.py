def find_min_schedule(streets_list, cars_list, sim_dur, num_inter, score_per_car):

    intersections = [{} for i in range(num_inter)]

    for car in cars_list:
        for street in car.streets_lst:

            end_inter = intersections[street.end]

            end_inter[street.name] = end_inter.setdefault(street.name, 0) + 1

    return intersections
