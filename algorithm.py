def find_min_schedule(streets_list, cars_list, sim_dur, num_inter, score_per_car):

    intersections = [{} for i in range(num_inter)]

    for car in cars_list:
        for street in car.streets_lst:

            end_inter = intersections[street.end]

            end_inter[street.name] = end_inter.setdefault(street.name, 0) + 1

    intersections = mapping(intersections)

    return intersections



def mapping(intersections):
    for intersection in intersections:
        for idx in intersection:
            intersection[idx] = int(intersection[idx]**0.3)

    return intersections


# def calc_state_of_trafic_lights(T, sec_start, cycle_time, duration) -> bool:
#     if sec_start <= ((T % cycle_time) - sec_start) <= duration:
#         return True

#     return False


# def calc_score(intersections, sim_dur, score_per_car):
#     total = 0

#     for T in range(sim_dur):
#         pass
