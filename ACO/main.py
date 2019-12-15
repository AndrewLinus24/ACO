from source import ACO
import numpy

MINIMUM_DISTANCE = {
    "10kota": 48,
    "eil51": 426,
    "berlin52": 7544,
}

NUMBER_OF_CITY = {
    "10kota": 10,
    "eil51": 51,
    "berlin52": 52,
}

def load_dataset(filename):
    """
    Load dataset from .txt and save it into array.
    Dataset format: (city_x_coordinate)\t(city_y_coordinate)\n
    """
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

def set_distance_matrix(dataset, inversed = False):
    """
    Set distance matrix (2D numpy.array) based on array of dataset.
    Distance is calculated using Euclidean Distance equation:
        numpy.linalg.norm(numpy.array(start_city) - numpy.array(end_city))
    Diagonal element is set to zero.
    If inversed = True, distance matrix elements are multiplicatively inversed:
        5 becomes 1/5
        0 remains 0
    """
    array = []
    for start_city in dataset:
        array_row = []
        for end_city in dataset:
            if(start_city != end_city):
                if(inversed):
                    array_row.append(1 / numpy.linalg.norm(numpy.array(start_city) - numpy.array(end_city)))
                else:
                    array_row.append(numpy.linalg.norm(numpy.array(start_city) - numpy.array(end_city)))
            else:
                array_row.append(0)
        array.append(array_row)
    return numpy.array(array)

def set_pheromone_matrix(dataset):
    """
    Set pheromone matrix (2D numpy.array) based on array of dataset.
    Pheromone is calculated using this equation:
        1 / MINIMUM_DISTANCE
    Diagonal element is set to zero.
    """
    array = []
    for start_city in dataset:
        array_row = []
        for end_city in dataset:
            if(start_city != end_city):
                if(len(dataset) == NUMBER_OF_CITY["10kota"]):
                    array_row.append(1 / MINIMUM_DISTANCE["10kota"])
                elif(len(dataset) == NUMBER_OF_CITY["eil51"]):
                    array_row.append(1 / MINIMUM_DISTANCE["eil51"])
                elif(len(dataset) == NUMBER_OF_CITY["berlin52"]):
                    array_row.append(1 / MINIMUM_DISTANCE["berlin52"])
            else:
                array_row.append(0)
        array.append(array_row)
    return numpy.array(array)

def run_aco(dataset_name, default_parameter):
    """
    Run ACO algorithm for calculating shortest path.
    Parameters:
        dataset_name (string)
            Name of dataset that is being used.
            Choices: "10kota", "eil51", "berlin52".
        default_parameter (boolean)
            True: Using default parameter.
            False: Using custom parameter.
    """
    dataset = load_dataset(dataset_name + ".txt")
    print("Dataset " + dataset_name)
    print(dataset)
    print()

    distance_matrix = set_distance_matrix(dataset)
    print("Distance Matrix")
    print(distance_matrix)
    print()

    inversed_distance_matrix = set_distance_matrix(dataset, inversed = True)
    print("Distance Matrix (Inversed Element)")
    print(inversed_distance_matrix)
    print()

    pheromone_matrix = set_pheromone_matrix(dataset)
    print("Pheromone Matrix")
    print(pheromone_matrix)
    print()

    number_of_ant = NUMBER_OF_CITY[dataset_name]
    number_of_iter = 1000
    decay = 0.5
    alpha = 1
    beta = 1
    q = 100

    if(not default_parameter):
        number_of_ant = 0
        while(number_of_ant < 1):
            number_of_ant = input("Input number of ant [> 0] [default = number of city]: ")
            try:
                number_of_ant = int(number_of_ant)
            except:
                number_of_ant = 0
                print("Input must be integer!")
                pass
        
        number_of_iter = 0
        while(number_of_iter < 1):
            number_of_iter = input("Input number of iteration [> 0] [default = 1000]: ")
            try:
                number_of_iter = int(number_of_iter)
            except:
                number_of_iter = 0
                print("Input must be integer!")
                pass

        decay = -1
        while(decay < 0 or decay >= 1):
            decay = input("Input pheromone decay rate [>= 0.00] [< 1.00] [default = 0.5]: ")
            try:
                decay = float(decay)
            except:
                decay = -1
                print("Input must be integer or decimal number!")
                pass

        alpha = -1
        while(alpha < 0):
            alpha = input("Input alpha (weight of pheromone) [>= 0.00] [default = 1.00]: ")
            try:
                alpha = float(alpha)
            except:
                alpha = -1
                print("Input must be integer or decimal number!")
                pass

        beta = -1
        while(beta < 0):
            beta = input("Input beta (weight of distance) [>= 0.00] [default = 1.00]: ")
            try:
                beta = float(beta)
            except:
                beta = -1
                print("Input must be integer or decimal number!")
                pass

        q = 0
        while(q < 1):
            q = input("Input q (dividend for updating pheromone) [>= 1.00] [default = 100]: ")
            try:
                q = float(q)
            except:
                q = 0
                print("Input must be integer or decimal number!")
                pass
        
    aco = ACO(distance_matrix, inversed_distance_matrix, pheromone_matrix, number_of_ant, number_of_iter, decay, alpha, beta, q)
    result = aco.calculate_shortest_path()
    print()
    print("Shortest Path: {}".format(result[0]))
    print("Shortest Distance: {}".format(result[1]))

def print_developer():
    """
    Print developer information.
    """
    print("This application was developed by:")
    print("2201916956 - David William")
    print("2201917095 - Adithya Nugraha Tjokrosetio")
    print("2201917126 - Andrew")

def main():
    """
    Main function.
    """
    index = 0
    while(index != 8):
        for i in range (0, 25):
            print()
        index = 0
        print("Default Parameter")
        print("=================")
        print("Number of ant = Number of city")
        print("Number of iteration = 1000")
        print("Pheromone decay rate = 0.5")
        print("Alpha (weight of pheromone) = 1")
        print("Beta (weight of distance) = 1")
        print("Q (dividend for updating pheromone) = 100")
        print()
        print("Ant Colony Optimization (ACO)")
        print("=============================")
        print("1. 10kota - Default Parameter")
        print("2. 10kota - Custom Parameter")
        print("3. eil51 - Default Parameter")
        print("4. eil51 - Custom Parameter")
        print("5. berlin52 - Default Parameter")
        print("6. berlin52 - Custom Parameter")
        print("7. About Developer")
        print("8. Exit")
        while(index < 1 or index > 8):
            index = input("Input [1-8]: ")
            try:
                index = int(index)
            except:
                index = 0
                print("Input must be numeric!")
                pass
        print()
        if(index == 1):
            run_aco(dataset_name = "10kota", default_parameter = True)
        elif(index == 2):
            run_aco(dataset_name = "10kota", default_parameter = False)
        elif(index == 3):
            run_aco(dataset_name = "eil51", default_parameter = True)
        elif(index == 4):
            run_aco(dataset_name = "eil51", default_parameter = False)
        elif(index == 5):
            run_aco(dataset_name = "berlin52", default_parameter = True)
        elif(index == 6):
            run_aco(dataset_name = "berlin52", default_parameter = False)
        elif(index == 7):
            print_developer()
        if(index != 8):
            print()
            print("Press ENTER to continue...")
            print()
            input()

main()