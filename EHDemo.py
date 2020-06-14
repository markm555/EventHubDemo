
# Author: Mark Moore
# Created: 6/10/2020
# Last updated: 6/11/2020
# Simulate a sine wave to send to an event hub and plot in real time.
# Reference: https://en.wikipedia.org/wiki/Sine_wave to get the math to plot a sine wave

import time                                                                   # get time for the delay
from math import *                                                            # get math for the sine function
from azure.eventhub import EventHubClient, Sender, EventData                  # get eventhub functions

Frequency=80                                                                  # Frequency is the number of cycles over time.
Frequencydelay = .1                                                           # Frequencydelay is a delay of time clock time for each loop to smooth the plot in PowerBI.  
pi=3.1415926535897932384626433832795028841971693993751057                     # The value of pi

ADDRESS = "amqps://yournamespace.servicebus.windows.net/youehname"            # Event hub and namespace
Policy = "YourPolicyName"                                                     # Event hub Username
KEY = "YourPolicyKey"                          # Event hub Key
client = EventHubClient(ADDRESS, debug=False, username=Policy, password=KEY)  # Create the client object
sender = client.add_sender(partition="0")                                     # Create the sender object
client.run()                                                                  # Start the client

while True:                                                                   # Infinite loop
   for n in range(Frequency):                                                 # inner loop that repeats 'Frequency' times
      p=sin(2*pi*n/Frequency)                                                 # fudged sine wave math since this is plotted in PowerBI in real time not on a graph where time is plotted as static.
      p=p*100                                                                 # Increase the value of p. Left alone, p will be between 1 and -1 and will plot as 0 for all points.  
      msg = '{"p":%i}' % (p)                                                  # construct json message with plot point to send to event hub
      sender.send(EventData(msg))                                             # send json to event hub
      time.sleep(Frequencydelay)                                              # Added to smooth out plot.  Increse to have fewer cycle per second decrease to have more
