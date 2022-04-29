#!/bin/bash

# SPECIFY THE SAME NUMBER OF ITERATIONS FOR ALL RUNS
ITERATIONS=1e5

# Run the Python3 script
echo '% --------------------------------- %'
echo '% ------- RUNNING PYTHON ---------- %'
python3 mc_pi.py $ITERATIONS
echo '% --------------------------------- %'

# Compile and run the C++ script
echo '% --------- RUNNING C++ ----------- %'
g++ -o mc_pi_cpp.out -ftime-report mc_pi.cpp
./mc_pi_cpp.out $ITERATIONS
echo '% --------------------------------- %'
