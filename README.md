# WaterMonitor_IoT_PWA
Water Monitor using PWA and the IoT. This project is inteded to provide a cheap simple IoT device using commodity components to monitor water levels in wells.
 
## Whats The Problem
In parts of Africa small villages walk many miles to local water wells. There is no way for that person to know:
* The state of the well
* Water level
* Quality of the water

From a local coummunity, local area, country or global view there is no data from those wells. 

## The Proposal
The idea is to:
* get access to the data in an easy way.
* store, compare and analyse over time.
* make a device that can record this, but has to be cheap, easy to use and setup and low power so that it can run on solar power.

## Raspberry Pi Setup

### Hardware Used
The hardware used for this sensor:
* Raspberry Pi Zero W
* Float switch (https://www.cynergy3.com/blog/category/float-switches)

### Software Setup
The detector is connected to the Raspberry Pi Zero W. To get this Pi up and running you need to install the following software:

* Use Raspberry Pi Debian Stretch 2018/4/18 OS. (https://www.raspberrypi.org/downloads/raspbian/)
* Update the basic machine with the following packages

    /> sudo apt update
    /> sudo apt install python3-gpiozero
    /> sudo apt-get install python-bluez
    /> sudo apt-get install bluez
    /> sudo  apt-get install bluetooth
    /> sudo pip install arrow

