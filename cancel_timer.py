# Program to Cancel the Timer 
import threading 
  
def gfg(): 
    print("Website: Accessible\n") #include in the url (unblocker) on this part
  
timer = threading.Timer(3.0, gfg) #have a way to connect the time with the website feature
timer.start() 
print("Cancelling Timer\n") 
timer.cancel() 
print("Timer Cancelled. Website is now accessible.\n") 