import datetime
import time

# Get the current time and set wait time
start_time = datetime.datetime.now()
wait_until = (start_time + datetime.timedelta(seconds=2)).second

while datetime.datetime.now().second != wait_until:
    print('Still waiting!')
    time.sleep(0.1)  # Avoid CPU overuse with a short sleep interval

print(f'We are at {wait_until} seconds!')

