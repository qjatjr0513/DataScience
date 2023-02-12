import schedule
import time

i = 0

def job():
    global i
    print("i'm working...")
    print("variable")
    print(i)
    i = i + 1

schedule.every(5).seconds.do(job)

while True:

    schedule.run_pending()
    time.sleep(1)
    if i ==5:
        break