#!/bin/bash

# MOVE INTO THE CODE FOLDER
cd code

# SPECIFY THE SAME NUMBER OF ITERATIONS FOR ALL RUNS
ITERATIONS=1e5
PRINTFLAG=1

# COMMAND LINE ARGUMENTS CAN BE USED
if [ $# == 1 ]; then
	ITERATIONS=$1
fi

echo '% --------------------------------- %'


# Run the Python3 script
echo '% ------- RUNNING PYTHON ---------- %'
python3 mc_pi.py $ITERATIONS $PRINTFLAG
echo '% --------------------------------- %'


# Run the Python3 script, parallelised
echo '% ---- RUNNING PYTHON (Pool4) ----- %'
python3 mc_pi_pool.py $ITERATIONS $PRINTFLAG
echo '% --------------------------------- %'


# Compile and run the C++ script
echo '% -------- RUNNING C++ ------------ %'
g++ -o mc_pi_cpp.out mc_pi.cpp
./mc_pi_cpp.out $ITERATIONS $PRINTFLAG
rm mc_pi_cpp.out
echo '% --------------------------------- %'


# Compile and run the C script
echo '% -------- RUNNING C -------------- %'
gcc -o mc_pi_c.out mc_pi.c
./mc_pi_c.out $ITERATIONS $PRINTFLAG
rm mc_pi_c.out
echo '% --------------------------------- %'

