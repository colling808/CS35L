R. Collin Guieb
104416194
HW 8: Multithreading Performance

Running make check clean resulted in a much better performance for larger numbers of threads.

For threads 1, 2, 4, and 8, the real time decreased by a factor of 1/2 each time.
This makes sense mathematically given that they are dividing the work into two more parts each time.

for 1 thread:
    real 0m46.402s
    user 0m46.413s
    sys  0m0.003s

for 2 threads:
    real 0m24.003s
    user 0m47.519s
    sys  0m0.001s

for 4 threads:
    real 0m12.425s
    user 0m47.754s
    sys  0m0.003s

for 8 threads:
    real 0m6.315s
    user 0m49.280s
    sys  0m0.004s

At first, I had no idea where to start. I had to carefully analyze the code and see what each part did.

I had trouble with the output, but I found the idea of turning the scaled_color into a 2-dimensional array.
This made sense because we had two variables, x and y, with one color. Implementing this was fairly simple,
just involved changing the variable wherever it occurred.

Other than this, the project was fairly straightforward. I just had to move the main part of the function into
the thread function. I did have trouble with making it only because I forgot to link -lpthread in the Makefile...whoops!

