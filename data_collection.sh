#!/bin/bash

# MOVE INTO THE CODE FOLDER
cd code

# SET THE NUMBER OF ITERATIONS
BASEARRAY=( 1 2 4 8 )
MAGARRAY=( 1 2 3 4 5 6 )
ITERATIONS=(  )

# create Iterations array
for mag in "${MAGARRAY[@]}"
	do
	for base in "${BASEARRAY[@]}"
	do
	ITERATIONS=(${ITERATIONS[@]} $(( $base * 10 ** $mag )))
	done
done
# append the next power of 10
ITERATIONS=(${ITERATIONS[@]} $(( 10 ** ${MAGARRAY[-1]} * 10 )))

# SET CORRECT PRINT FLAG
PF=2

# COMPILE C AND C++ CODE
gcc -o mc_pi_c.out mc_pi.c
g++ -o mc_pi_cpp.out mc_pi.cpp

# CREATE A DATA FILE HEADER
# (use '>' to start new file)
printf "NumIt\t Py (ser) [s]\t Py (P4) [s]\t C++ [s]\t C [s]\n" > TimeComparison.dat

# FILL THE DATA FILE
for IT in "${ITERATIONS[@]}"
do
	printf "Processing $IT Iterations\n"
	printf "$IT\t `python3 mc_pi.py $IT $PF`\t `python3 mc_pi_pool.py $IT $PF`\t `./mc_pi_cpp.out $IT $PF`\t `./mc_pi_c.out $IT $PF`\n" >> TimeComparison.dat
done

# CLEAN UP (REMOVE EXECUTABLES)
rm *.out

# PLACE RESULTS IN MAIN DIRECTORY
mv TimeComparison.dat ../

