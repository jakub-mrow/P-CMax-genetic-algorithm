# Solution to P||CMax problem using genetic algorithm metaheuristic

# Structure of repository
- `data` - folder in which there are hard to solve instances given by the professor
- `random` - randomly generated instances
- `src` - source code

# How to run the program
- clone the repository
- run `geneticAlgorithm.py` script which you can find in `src` folder with 2 or 3parameters
    - first - folder in which there is a example that you want to run
    - second - name of the test
    - third (optional) - number of inviduals per generation (if not given the default) - for the best results choose number between 1000-5000
- example `python geneticAlgorithm.py data m25.txt 2000`

# How to choose the input data?
In folder named `data` there are number of examples provided by professor 

# What is the P||CMax problem in computer science
In the P || Cmax problem, the task is to arrange 𝑛 tasks on 𝑚 processors in such a way that the completion time of all tasks on all processors is as short as possible.

# What is a genetic algorithm?
A genetic algorithm is a search heuristic that is inspired by Charles Darwin’s theory of natural evolution. This algorithm reflects the process of natural selection where the fittest individuals are selected for reproduction in order to produce offspring of the next generation.

So in our case, we take the input data, shuffle it `x` times and solve these instances with greedy algorithm. This is our population of individuals. After that our genetic algorithm starts by creating another population which should be better than the previous one, by using technics like selection, mutations and crossovers. We repeat this process as much as we want to improve our final solution of the problem.

More on that topic you can read in documentation (written in Polish) present in this repository. It is a lab report that I did for my Combinatorial Optimization class.