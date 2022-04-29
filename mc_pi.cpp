/* C++ program for estimation of Pi using Monte
   Carlo Simulation */
#include <bits/stdc++.h>
#include <random>
#include <cmath>
#include <chrono>

using namespace std::chrono;

int main(int argc,char* argv[])
{
    int i;
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
    if (argc > 1) interval =  atof(argv[1]);

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

        // estimated pi after this iteration
        pi = double(4 * circle_points) / square_points;
    }

    // END TIME OF ROUTINE AND DURATION
    auto end = high_resolution_clock::now();
    duration<double> elapsed = end - start;

    // Final Estimated Value
    printf("\nAfter %.0e Iterations\n", interval);
    printf("\nEstimation of PI:\t PI = %f", pi);
    printf("\nCompare to CMATH:\t PI = %f\n", M_PI);
    std::cout << "\nExecution time was " <<
              elapsed.count() << "s.\n";

    return 0;
}