# Källudden Control and Monitoring

This is my [balenaCloud](https://www.balena.io/cloud) project to set up a Raspberry Pi to read data from a WH1080 weather station and control a relay for starting/stopping the electrical heating unit.

## Service containers

### rtl422

This service uses RTL_422 to receive WH1080 RF transmissions using an RTL-SDR USB stick.
The decoded data can be sent to a MQTT server by setting the output to `-F mqtt://server:1883`

### heatercontrol

This service listens for commands on a MQTT topic and controls a relay connected to a GPIO output on the Raspberry Pi.

## Required hardware

* Raspberry Pi 3B
* 16 GB Micro-SD Card (Balena recommend Sandisk Extreme Pro SD cards)
* Micro-USB cable
* Power supply
* Case (optional)
* RTL-SDR USB stick
