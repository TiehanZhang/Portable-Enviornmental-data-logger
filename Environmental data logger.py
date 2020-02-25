from microbit import *
with open('data_logger.csv', "w") as my_file:
    my_file.write("Hello")
compass.calibrate()
turn = 0
# default initiating for the write mode of my file
while True:
    with open('data_logger.csv') as my_file:
        content = my_file.read()
    content = content + str(temperature()) + ", " + str(compass.heading()) + "\n"
    with open('data_logger.csv', "w") as my_file:
        my_file.write(content)
    display.show(turn)
    turn = turn + 1
    # count the turns of uploading the data
    sleep(10000)
