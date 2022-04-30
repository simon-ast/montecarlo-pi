/* C++ program for estimation of Pi using Monte
   Carlo Simulation */
#include <bits/stdc++.h>
#include <random>
#include <cmath>
#include <chrono>

using namespace std::chrono;

int main(int argc, char* argv[])
{
    int i, print_flag = 0;
    double rand_x, rand_y, origin_dist, pi;
    double interval = 1e5;
    int circle_points = 0, square_points = 0;

    // START A TIMER FOR EXECUTION
    auto start = high_resolution_clock::now();

    // GENERATOR FOR RANDOM NUMBER UNIFORMLY DISTRIBUTED
    // IN (-1, 1)
    std::default_random_engine generator;
    std::uniform_real_distribution<double> distribution(-1,1);

    // ITERATION NUMBER IS TAKEN AS COMMANDLINE ARGUMENT (ONLY
    // IF PRESENT)
    if (argc > 1) 
    {
    	interval =  atof(argv[1]);
    	print_flag = atoi(argv[2]);
    }

    // LOOP FOR SPECIFIED NUMBER OF ITERATIONS
    for (i = 0; i <= interval; i++) {
        // Randomly generated x and y values
        rand_x = distribution(generator);
        rand_y = distribution(generator);

        // Distance between (x, y) from the origin
        origin_dist = rand_x * rand_x + rand_y * rand_y;

        // Checking if (x, y) lies inside the define
        // circle with R=1
        if (origin_dist <= 1) circle_points++;

        // Total number of points generated
        square_points++;
        
    }
    
    // ESTIMATE PI AFTER END OF ITERATIONS
    pi = double(4 * circle_points) / square_points;

    // END TIME OF ROUTINE AND DURATION
    auto end = high_resolution_clock::now();
    duration<double> elapsed = end - start;

    // Final Estimated Value
    if (print_flag==1) {
        printf("\nAfter %.0e Iterations\n", interval);
        printf("\nEstimation of PI:\t PI = %f", pi);
        printf("\nCompare to CMATH:\t PI = %f", M_PI);
        printf("\nFirst 10 digits:\t PI = 3.141592653\n");
        printf("\nExecution time was %1.5es.\n\n", elapsed.count());
    }
    
    if (print_flag==2)
	{
		printf("%1.5e",elapsed.count());
	}

    return 0;
}
