#!/bin/bash

ps aux | grep false | grep -v grep > /dev/nul
found_zombie=$?
while [ $found_zombie ] ; do
  ps aux | grep false | grep -v grep > /dev/nul
  found_zombie=$?
  sleep 1
done

echo zombie was killed. Time is:
time
