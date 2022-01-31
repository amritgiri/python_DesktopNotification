import time
import plyer

if __name__ == '__main__':
    while True:
        plyer.notification.notify(
            title = "Time To Drink Water!!",
            message = "Drinking water stabilizing the heartbeat and maintain blood pressure",

            timeout = 12
        )
        time.sleep(60*60) #sleep upto 1 hours and then notification pops up again
