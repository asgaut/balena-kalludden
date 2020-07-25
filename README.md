# Källudden Control and Monitoring

This is my [balenaCloud](https://www.balena.io/cloud) project to set up a Raspberry Pi to read data from a Cotech 36-6726 weather station and control a relay for starting/stopping the electrical heating unit.

## Service containers

### rtl433

This service uses RTL_433 to receive Cotech 36-6726 and other sensors transmissions using an RTL-SDR USB stick.
The decoded data is sent to a MQTT server by setting the output to `-F mqtt://server:1883`

Documentation and list of supported devices is at https://github.com/merbanan/rtl_433

#### Device service variables

- RTL_433_INPUT: `-R 18 -R 19 -R 153 -C si -M level -M utc`
- RTL_433_OUTPUT: `-F mqtt://mqtt_server_ip:1883,devices=/dev[/model][/id][/channel],events=/events,states=/states`

When testing under Windows: use numeric IP address for the MQTT server as the DNS lookup in rtl_433 does not work
under Windows OS.

#### Description

- -R 18: Enable Fineoffset-WH2 (Telldus) temperature/humidity sensor
- -R 19: Enable Nexus (Clas Ohlson Cotech 36-6726) temperature/humidity sensor
- -R 153: Enable Clas Ohlson Cotech 36-7959 weather station
- -M level -M utc -C si: Various output control parameteres

### heatercontrol

This service listens for commands on a MQTT topic and controls a relay connected to a GPIO output on the Raspberry Pi.

## Testing

- Install MQTT client tools using `sudo apt install mosquitto-clients`
- Listen for all published messages using: `mosquitto_sub -t "/#" -h mqtt_server_ip -v`

## Required hardware

- Raspberry Pi 3B
- 16 GB Micro-SD Card (Balena recommend Sandisk Extreme Pro SD cards)
- Micro-USB cable
- Power supply
- Case (optional)
- RTL-SDR USB stick

## Sample MQTT data from RTL_433

```text
/events {"time":"2020-07-05 21:04:23","model":"Nexus-TH","id":173,"channel":1,"battery_ok":1,"temperature_C":22.7,"humidity":49,"mod":"ASK","freq":433.98397,"rssi":-0.111965,"snr":35.04253,"noise":-35.1545}
/dev/Nexus-TH/173/1/time 2020-07-05 21:04:23
/dev/Nexus-TH/173/1/id 173
/dev/Nexus-TH/173/1/channel 1
/dev/Nexus-TH/173/1/battery_ok 1
/dev/Nexus-TH/173/1/temperature_C 22.7
/dev/Nexus-TH/173/1/humidity 49
/dev/Nexus-TH/173/1/mod ASK
/dev/Nexus-TH/173/1/freq 433.98397
/dev/Nexus-TH/173/1/rssi -0.111965
/dev/Nexus-TH/173/1/snr 35.04253
/dev/Nexus-TH/173/1/noise -35.1545
/events {"time":"2020-07-05 21:04:31","model":"Fineoffset-WH2","id":135,"temperature_C":18.5,"humidity":61,"mic":"CRC","mod":"ASK","freq":434.24208,"rssi":-0.124493,"snr":14.1239,"noise":-14.2484}
/dev/Fineoffset-WH2/135/time 2020-07-05 21:04:31
/dev/Fineoffset-WH2/135/id 135
/dev/Fineoffset-WH2/135/temperature_C 18.5
/dev/Fineoffset-WH2/135/humidity 61
/dev/Fineoffset-WH2/135/mic CRC
/dev/Fineoffset-WH2/135/mod ASK
/dev/Fineoffset-WH2/135/freq 434.24208
/dev/Fineoffset-WH2/135/rssi -0.124493
/dev/Fineoffset-WH2/135/snr 14.1239
/dev/Fineoffset-WH2/135/noise -14.2484
/events {"time":"2020-07-05 21:04:35","model":"Fineoffset-WH2","id":151,"temperature_C":18.1,"humidity":64,"mic":"CRC","mod":"ASK","freq":434.16739,"rssi":-0.123405,"snr":14.72105,"noise":-14.8445}
/dev/Fineoffset-WH2/151/time 2020-07-05 21:04:35
/dev/Fineoffset-WH2/151/id 151
/dev/Fineoffset-WH2/151/temperature_C 18.1
/dev/Fineoffset-WH2/151/humidity 64
/dev/Fineoffset-WH2/151/mic CRC
/dev/Fineoffset-WH2/151/mod ASK
/dev/Fineoffset-WH2/151/freq 434.16739
/dev/Fineoffset-WH2/151/rssi -0.123405
/dev/Fineoffset-WH2/151/snr 14.72105
/dev/Fineoffset-WH2/151/noise -14.8445
/events {"time":"2020-07-05 21:04:56","model":"Cotech-367959","id":15,"battery_ok":1,"temperature_C":14.94445,"humidity":61,"rain_mm":25.5,"wind_dir_deg":3,"wind_avg_m_s":0.8,"wind_max_m_s":1.0,"mic":"CRC","mod":"ASK","freq":433.92234,"rssi":-12.1442,"snr":19.58607,"noise":-31.7303}
/dev/Cotech-367959/15/time 2020-07-05 21:04:56
/dev/Cotech-367959/15/id 15
/dev/Cotech-367959/15/battery_ok 1
/dev/Cotech-367959/15/temperature_C 14.94445
/dev/Cotech-367959/15/humidity 61
/dev/Cotech-367959/15/rain_mm 25.5
/dev/Cotech-367959/15/wind_dir_deg 3
/dev/Cotech-367959/15/wind_avg_m_s 0.8
/dev/Cotech-367959/15/wind_max_m_s 1.0
/dev/Cotech-367959/15/mic CRC
/dev/Cotech-367959/15/mod ASK
/dev/Cotech-367959/15/freq 433.92234
/dev/Cotech-367959/15/rssi -12.1442
/dev/Cotech-367959/15/snr 19.58607
/dev/Cotech-367959/15/noise -31.7303
```
