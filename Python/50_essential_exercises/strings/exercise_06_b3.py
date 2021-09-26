#####################
#Pig Latin Sentence #
#####################

# Read through an Apache log file. If there is a 404 error -- you can just
# search fot '404', if you want -- display the IP address, which should be the
# first element.

def display_ip(logfile):

    with open(logfile, "r") as file:
        for line in file:
            if "404" in line:
                print(line.split()[0])
