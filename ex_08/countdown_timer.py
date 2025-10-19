import time

timer = int(input("Enter the countdown time in seconds: "))
while timer:
    mins, secs = divmod(timer, 60)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    print(timeformat, end='\r')
    time.sleep(1)
    timer -= 1
print("Time's up!")