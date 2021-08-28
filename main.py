#check the current time
import datetime
#time to repat the notification
import time 
#getting custom notification in our windows
from plyer import notification
#for threading
from threading import Thread

class WaterReminder (Thread):
    def run(self):
        while(True):
            print("start")
            notification.notify(
                #title of the notification,
                title = "Drink Water",
                #the body of the notification
                message = "Take a sip of water",
                #make sure the icon is in ico format when it is downloaded 
                app_icon = "drink-water.ico",
                # the notification stays for 20sec
                timeout  = 20
            )
            #sleep for 30 minutes (30mins * 60 seconds = 1800)
            #notification repeats after every 30 minutes
            time.sleep(30*60)

class PostureReminder (Thread):
    def run(self):
        while(True):
            notification.notify(
                #title of the notification,
                title = "Maintain proper posture",
                #the body of the notification
                message = "Sit Straight",
                #make sure the icon is in ico format when it is downloaded 
                app_icon = "posture.ico",
                # the notification stays for 20sec
                timeout  = 20
            )
            #sleep for 1 hr minutes (60mins * 60 seconds = 3600)
            #notification repeats after every 60 minutes
            time.sleep(60*60)

#calculate the time left for the closest hour 
delta = datetime.timedelta(hours=1) 
now = datetime.datetime.now()
nextHour = (now + delta).replace(microsecond=0, second=0, minute=0)  
waitSeconds = (nextHour - now).seconds   

#sleep till the closest hour 
time.sleep(waitSeconds)

#run when the closest hour begins
water = WaterReminder()
posture = PostureReminder ()
water.start()
posture.start()

