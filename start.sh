#!/bin/bash
echo "RTL_433_INPUT:" $RTL_433_INPUT
echo "RTL_433_OUTPUT:" $RTL_433_OUTPUT
echo "Starting rtl_433..."
rtl_433 $RTL_433_INPUT $RTL_433_OUTPUT
