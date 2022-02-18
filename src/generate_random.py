import random

SIZES = [100, 200, 300, 400, 500]
PROCESSORS = [10, 20, 50]

for processor in PROCESSORS:
    for size in SIZES:
        name = "random/random" + str(processor)  + "_" + str(size)
        with open(name, "a") as file:
            file.write(str(processor) + "\n")
            file.write(str(size) + "\n")
            for num in range(size):
                randomNum = random.randint(1, size)    
                file.write(str(randomNum) + "\n")
