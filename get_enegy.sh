#/usr/bin/bash

for i in `seq 1 6`; do grep "total energy:" vol$i/nohup.out | tail -1 ; done
