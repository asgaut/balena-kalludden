# Källudden Control and Monitoring

This is my [balenaCloud](https://www.balena.io/cloud) project to set up a Raspberry Pi to read data from a WH1080 weather station and control a relay for starting/stopping the electrical heating unit.

## Service containers

### rtl433

This service uses RTL_433 to receive WH1080 RF transmissions using an RTL-SDR USB stick.
The decoded data can be sent to a MQTT server by setting the output to `-F mqtt://server:1883`

Documentation and list of supported devices is at https://github.com/merbanan/rtl_433

#### Device service variables

* RTL_433_INPUT: -H 60 -R 32 -R 18 -f 868.38M -f 433.92M -M newmodel -M level -M utc
* RTL_433_OUTPUT: -F mqtt://mqtt_server_ip:1883,devices=/dev/wh1080,events=/events,states=/states

When testing under Windows: use numeric IP address for the MQTT server as the DNS lookup in rtl_433 does not work
under Windows OS.

#### Description

* -H 60 -f 868.38M -f 433.92M: Hop every 60 s between these frequencies
* -R 32: Enable WH1080 weather station
* -R 18: Enable Fineoffset-WH2 (Telldus) temperature/humidity sensor
* -M newmodel -M level -M utc -C si: Various output control parameteres

### heatercontrol

This service listens for commands on a MQTT topic and controls a relay connected to a GPIO output on the Raspberry Pi.

## Required hardware

* Raspberry Pi 3B
* 16 GB Micro-SD Card (Balena recommend Sandisk Extreme Pro SD cards)
* Micro-USB cable
* Power supply
* Case (optional)
* RTL-SDR USB stick
