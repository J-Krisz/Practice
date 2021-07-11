##############
# Run timing #
##############

# Write a function run_timing() that asks how long it took for you to run
# 10km. The function continues to ask how lon (in miutes) it took for additional
# runs, until the user presses Enter. At that point, the function exits -- but
# only after calculateing and displaying the average time the 10km runs took.

# Note that the numeric inputss and outputs should all be floating point values.
# This exercise is meant to help you converting inputs into apropriate types,
# along with tracking information overtime

def run_timing():

    no_of_runs = 0
    total_time = 0

    while True:
        
        one_run = input("10k run time : ")

        if not one_run:
            break

        no_of_runs += 1
        total_time += float(one_run)

    avg_time = total_time / no_of_runs

    return f"Your average time for {no_of_runs} 10km runs is {avg_time} minutes"

print(run_timing())
