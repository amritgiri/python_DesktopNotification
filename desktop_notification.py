import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title = "Time To Drink Water!!",
            message = "Drinking water stabilizing the heartbeat and maintain blood pressure",

            timeout = 12
        )
        time.sleep(60*60) #sleep upto 1 hours and then notification pops up again