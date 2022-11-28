#!/bin/bash

pushd /home/simon/Code/todo-list || exit

while :
  do
    # Holds the terminal until action is chosen
    python3 main.py

    # Waits for miniscule amount of time
    sleep 2

    # Resets the terminal
    clear
  done
