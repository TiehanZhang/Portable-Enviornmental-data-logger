# Write your code here :-)
from microbit import *
with open('data_logger.csv', "w") as tiehan_file:
    tiehan_file.write("")
microbit.compass.calibrate()
# default initiating for the write mode of my file
while True:
    with open('data_logger.csv') as tiehan_file:
        content = tiehan_file.read()
    content = content + str(temperature()) + ", " + str(compass.heading()) + "\n"
    with open('data_logger.csv', "w") as tiehan_file:
        tiehan_file.write(content)
    sleep(10000)
