from temp import read_temp
import time
import datetime


def main():
    with open("./temperatures.txt", "w") as f:
        while True:
            temp_f = read_temp()
            current_time = datetime.datetime.now()
            temperature = f"{current_time} - {temp_f}\n"
            f.write(temperature)
            print(temperature)

            f.flush()
            time.sleep(1)


main()
