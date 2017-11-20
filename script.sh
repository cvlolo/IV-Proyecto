#!/bin/bash

# Start the first process
gunicorn --config=config_gunicorn.py web:app -D
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start my_first_process: $status"
  exit $status
fi

# Start the second process
python ATPBot/ATPbot.py -D
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start my_second_process: $status"
  exit $status
fi




