#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#define RMAX ((double)RAND_MAX*(double)RAND_MAX)


int main(int argc, char* argv[])
{
	int i, print_flag = 0;
	double rand_x, rand_y, origin_dist, pi;
	double interval = 1e5;
	double circle_points = 0., square_points = 0.;
	clock_t start, end;
	double elapsed;
	
	// START A TIMER FOR CODE EXECUTION
	start = clock();
	
	// USE COMMAND LINE INPUT AS ITERATION LENGTH
	if (argc > 1) 
	{
		interval =  atof(argv[1]);
		print_flag = atoi(argv[2]);
	}
	
	// LOOP FOR SPECIFIED NUMBER OF ITERATIONS
	for (i = 0; i <= interval; i++)
	{
		// GENERATE A RANDOM NUMBER FROM A UNIFORM DISTRIBUTION
		// BETWEEN (-1, 1).
		rand_x = rand();
		rand_y = rand();
		
		// CALCULATE DISTANCE TO ORIGIN
		origin_dist = rand_x * rand_x + rand_y * rand_y;
		
		// CHECK IF DISTANCE TO THE ORIGIN IS WITHIN THE CIRCLE
		if (origin_dist <= RMAX) circle_points++;
		
		// INCREMENT NUMBER OF POINTS IN SQUARE
		square_points++;
	}
	
	// ESTIMATE PI AFTER END OF ITERATIONS
	pi = (4 * circle_points) / square_points;
	
	// NOTE END TIME OF EXECUTION AND CALCULATE DURATION
	end = clock();
	elapsed = ((double)(end - start)) / CLOCKS_PER_SEC;
	
	// PRINT FINAL VALUES (IF PROMPTED)
	if (print_flag==1) 
	{
		printf("\nAfter %.0e Iterations\n", interval);
		printf("\nEstimation of PI:\t PI = %f", pi);
		printf("\nCompare to MATH:\t PI = %f", M_PI);
		printf("\nFirst 10 digits:\t PI = 3.141592653 ...\n");
		printf("\nExecution time was %1.5es.\n\n", elapsed);
	}
	
	if (print_flag==2)
	{
		printf("%1.5e", elapsed);
	}

    return 0;
}
