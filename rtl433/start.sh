#!/bin/bash
echo "RTL_433_INPUT:" $RTL_433_INPUT
echo "RTL_433_OUTPUT:" $RTL_433_OUTPUT
echo "Removing RTL-SDR kernel module"
rmmod dvb_usb_rtl28xxu
echo "Starting rtl_433..."
rtl_433 $RTL_433_INPUT $RTL_433_OUTPUT
echo "rtl_433 exited..."
