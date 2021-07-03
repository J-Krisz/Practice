# Write a function ( run_timing ) that asks how long it took for you to run 10 km.
# The function continues to ask how long (in minutes) it took for additional runs, until
# the user presses Enter. At that point, the function exits—but only after calculating and
# displaying the average time that the 10 km runs took.


def run_timing():
    runs = 0
    total_t = 0

    while True:
        one_run = input("How long did it take to finish your 10km (in minutes)? :")

        if not one_run:
            break

        runs += 1
        total_t += float(one_run)

    avg_time = total_t / runs

    return f"Your average time is {avg_time} over {runs} runs"


print(run_timing())
