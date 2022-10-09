from numpy import matrix
from random_utilities import *
def create_schedule(number_of_racers,minimum_number_races):
    """
    This takes a number of total racers and returns a 2D array of 
    nX4 for the race
    
    Parameters:
        number_of_racers: (int) the number of race cars for this schedule
        minimum_number_races_per_racer: (int) the lowest desired total number of races for each racer
    
    Returns:
        2D array representing the generated schedule
    """
    schedule = []
    racer_matrix = []
    
    # fill in empty matrix
    for i in range(number_of_racers):
        temp_arr = []
        for j in range(number_of_racers):
            temp_arr.append(0)
        racer_matrix.append(temp_arr)
    
    while(len(schedule) < minimum_number_races):
        r1 = get_min_diagonal(racer_matrix)
        r2 = get_min_row(racer_matrix, [r1])
        r3 = get_min_row(racer_matrix, [r1,r2])
        r4 = get_min_row(racer_matrix, [r1,r2,r3])
        
        add_racers_to_matrix(r1,r2,r3,r4,racer_matrix)
        schedule.append([r1,r2,r3,r4])
        
    print("---RACER MATRIX---")
    print_matrix(racer_matrix)
    print("---Total Races---")
    print(len(schedule))
        
    # while(not is_diagonal_equal(racer_matrix)):
    #     r1 = get_min_diagonal(racer_matrix)
    #     r2 = get_min_diagonal(racer_matrix,[r1])
    #     r3 = get_min_diagonal(racer_matrix,[r1,r2])
    #     r4 = get_min_diagonal(racer_matrix,[r1,r2,r3])
    #     add_racers_to_matrix(r1,r2,r3,r4,racer_matrix)
    #     schedule.append([r1,r2,r3,r4])
    
    
    while(True):
        racers_with_full_schedule = get_all_max_on_diagonal(racer_matrix)
        r1 = get_min_diagonal(racer_matrix,racers_with_full_schedule)
        racers_with_full_schedule.append(r1)
        if len(racers_with_full_schedule) == len(racer_matrix):
            # TODO: Steal from previous 2 races (3 total races with 3 cars)
            # TODO: add to matrix and schedule
            break
        r2 = get_min_row(racer_matrix, racers_with_full_schedule)
        racers_with_full_schedule.append(r2)
        if len(racers_with_full_schedule) == len(racer_matrix):
            # TODO: Steal from previous 1 race (2 total 3 car races)
            # TODO: add to matrix and schedule
            break
        r3 = get_min_row(racer_matrix, racers_with_full_schedule)
        racers_with_full_schedule.append(r3)
        if len(racers_with_full_schedule) == len(racer_matrix):
            # TODO: add to matrix and schedule
            break
        r4 = get_min_row(racer_matrix, racers_with_full_schedule)
        racers_with_full_schedule.append(r4)
        if len(racers_with_full_schedule) == len(racer_matrix):
            schedule.append([r1,r2,r3,r4])
            add_racers_to_matrix(r1,r2,r3,r4,racer_matrix)
            break
        
        schedule.append([r1,r2,r3,r4])
        add_racers_to_matrix(r1,r2,r3,r4,racer_matrix)
        
        
        
    # print("---CURRENT SCHEDULE---")
    # print_matrix(schedule)
    print("---RACER MATRIX---")
    print_matrix(racer_matrix)
    print("---Total Races---")
    print(len(schedule))
        
    
if __name__=="__main__":
    create_schedule(23,60)