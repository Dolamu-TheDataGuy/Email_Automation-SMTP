from datetime import datetime
import time

start_time = datetime(2023, 1, 27, 10, 37, 0)

while datetime.now() < start_time:
    time.sleep(1)

print("Program now starting on Halloween 2029")

