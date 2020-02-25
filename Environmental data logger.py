# Write your code here :-)
import microbit as mt

with open('env_data_logger.csv', "w") as my_file:
    my_file.write("")
mt.compass.calibrate()
while True:
    with open('env_data_logger.csv') as my_file:
        content = my_file.read()
    content = content + str(mt.temperature()) + ", " + str(mt.compass.heading()) + "\n"
    with open('env_data_logger.csv', "w") as my_file:
        my_file.write(content)
    sleep(10000)