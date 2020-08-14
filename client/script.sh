#!/bin/bash

echo "Running netcat"
nc -zv ${DASK_SCHEDULER_HOST} ${DASK_SCHEDULER_PORT}

echo "Running client py script"
python script.py
