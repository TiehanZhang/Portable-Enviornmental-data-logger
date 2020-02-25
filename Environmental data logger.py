# Write your code here :-)
import microbit as mt

with open('data_logger.csv', "w") as tiehan_file:
    my_file.write("")
mt.compass.calibrate()

while True:
    with open('data_logger.csv') as tiehan_file:
        content = my_file.read()
    content = content + str(mt.temperature()) + ", " + str(mt.compass.heading()) + "\n"
    with open('data_logger.csv', "w") as tiehan_file:
        my_file.write(content)
    sleep(5000)
