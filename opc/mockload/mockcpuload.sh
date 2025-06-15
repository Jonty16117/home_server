#!/bin/bash

### CONFIGURATION ###
CPU_LOAD_PERCENT=70      # % of total CPU cores to use
#######################

cpu_load() {
  while :; do :; done
}

export -f cpu_load

total_cores=$(nproc)
hog_cores=$((total_cores * CPU_LOAD_PERCENT / 100))
[ "$hog_cores" -lt 1 ] && hog_cores=1

seq "$hog_cores" | xargs -n1 -P"$hog_cores" bash -c 'cpu_load'
