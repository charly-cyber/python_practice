import datetime
import time
alarm_time_str = input("Set the alarm time (HH:MM:SS): ")
try:
    alarm_time = datetime.datetime.strptime(alarm_time_str, "%H:%M:%S").time()
    print(f"Alarm set for {alarm_time_str}.")
    while True:
        current_time = datetime.datetime.now().time()
        print(f"Current time: {current_time.strftime('%H:%M:%S')}", end='\r')
        if current_time >= alarm_time:
            print("Alarm! Time to wake up!")
            break
        time.sleep(1)

except ValueError:
    print("Invalid time format. Please use HH:MM:SS.")
    exit() 