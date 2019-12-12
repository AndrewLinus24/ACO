from source import ACO
import numpy

MINIMUM_DISTANCE = {
    "10kota": 50,
    "eil51con": 426,
    "berlin52conv": 1000,
}

def load_dataset(filename):
    file = open(filename, "r")
    iter_file = iter(file)
    next(iter_file)
    array = []
    for line in iter_file:
        city_start, city_end = line.split("\t")
        city_end = city_end.strip("\n")
        array.append([int(city_start), int(city_end)])
    file.close()
    return(array)

def set_distance_matrix(dataset):
    array = []
    for start_city in dataset:
        for end_city in dataset:
            if(start_city != end_city):
                array.append(numpy.linalg.norm(numpy.array(start_city) - numpy.array(end_city)))
            else:
                array.append(0)
    return numpy.array(array)

def set_pheromone_matrix(dataset):
    array = []
    for start_city in dataset:
        for end_city in dataset:
            if(start_city != end_city):
                array.append(1/MINIMUM_DISTANCE["10kota"])
            else:
                array.append(0)
    return numpy.array(array)

def run_10kota():
    dataset = load_dataset("10kota.txt")
    distance_matrix = set_distance_matrix(dataset)
    print("Distance Matrix (Multiplicatively Inversed)")
    print(distance_matrix)
    print()

    pheromone_matrix = set_pheromone_matrix(dataset)
    print("Pheromone Matrix")
    print(pheromone_matrix)
    print()

    print("ACO Shortest Distance: ")
    print()

    print("ACO Shortest Path: ")

def run_eil51con():
    pass

def run_berlin52_conv():
    pass

def print_developer():
    print("This app was developed by:")
    print("Andrew - 2201917126")
    print("Adithya Nugraha Tjokrosetio - 2001551315")
    print("David William - 2001540066")

def clearScreen(x):
    for i in range (0, x):
        print()

def main():
    index = 0
    while(index != 5):
        clearScreen(25)
        index = 0
        print("Ant Colony Optimization (ACO)")
        print("=============================")
        print("1. 10kota")
        print("2. eil51con")
        print("3. berlin52conv")
        print("4. About Developer")
        print("5. Exit")
        while(index < 1 or index > 5):
            index = input("Input [1-5]: ")
            try:
                index = int(index)
            except:
                index = 0
                print("Input must be numeric!")
                pass
        print()
        if(index == 1):
            run_10kota()
        elif(index == 2):
            run_eil51con()
        elif(index == 3):
            run_berlin52_conv()
        elif(index == 4):
            print_developer()
        if(index != 5):
            input()

main()