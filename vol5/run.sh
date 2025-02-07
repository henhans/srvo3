#/usr/bin/bash

nohup mpirun --bind-to numa -np 1 python3 main.py grisb_config.toml &
