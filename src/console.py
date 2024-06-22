import datetime
import time
from temp import read_temp


def console():
    with open("./temperatures.txt", "w") as f:
        while True:
            temp_f = read_temp()
            current_time = datetime.datetime.now()
            temperature = f"{current_time} - {temp_f}\n"
            f.write(temperature)
            print(temperature)
            f.flush()
            time.sleep(60)


console()
