import numpy

class ACO:
    def __init__(self, distance_matrix, inversed_distance_matrix, pheromone_matrix, number_of_ant, number_of_iter, decay, alpha, beta, q):
        """
        Parameters:
            distance_matrix (2D numpy.array)
                Distance matrix.
            inversed_distance_matrix (2D numpy.array)
                Distance matrix whose elements are multiplicatively inversed.
            pheromone_matrix (2D numpy.array)
                Pheromone matrix.
            number_of_ant (int)
                Number of ant.
                Default: Equals to number of city.
            number_of_iter (int)
                Number of iteration (1 <= number_of_iter).
                Default: 1000.
            decay (float)
                Pheromone decay rate (0 <= decay < 1).
                The higher decay rate, the faster pheromone decay.
                Default: 0.5.
            alpha (float)
                Weight of pheromone (0 <= alpha).
                Default: 1.
            beta (float)
                Weight of distance (0 <= beta).
                Default: 1.
            q (int)
                Dividend for updating pheromone (0 < q).
                Default: 100.
            all_move (range)
                All index representing move between 2 cities.
        """
        self.distance_matrix = distance_matrix
        self.inversed_distance_matrix = inversed_distance_matrix
        self.pheromone_matrix = pheromone_matrix
        self.number_of_ant = number_of_ant
        self.number_of_iter = number_of_iter
        self.decay = decay
        self.alpha = alpha
        self.beta = beta
        self.q = q
        self.all_move = range(len(distance_matrix))

    def calculate_shortest_path(self):
        """
        Calculate and return shortest path using ACO algorithm.
        """
        shortest_path = None
        shortest_shortest_path = ("placeholder", numpy.inf)
        for i in range(self.number_of_iter):
            all_path = self.generate_all_path()
            self.update_pheromone(all_path)
            shortest_path = min(all_path, key = lambda x: x[1])
            print("Iteration " + str(i))
            print(shortest_path)
            print()
            if(shortest_path[1] < shortest_shortest_path[1]):
                shortest_shortest_path = shortest_path
        return shortest_shortest_path
    
    def generate_all_path(self):
        """
        Generate and return all path (array of sets).
        """
        all_path = []
        for i in range(self.number_of_ant):
            path = self.generate_path(i)
            all_path.append((path, self.calculate_path_distance(path)))
        return all_path

    def generate_path(self, start_city):
        """
        Generate and return path (array of sets).
        """
        path = []
        city_visited = set()
        city_visited.add(start_city)
        current_city = start_city
        for i in range(len(self.distance_matrix) - 1):
            next_city = self.select_next_city(self.pheromone_matrix[current_city], self.inversed_distance_matrix[current_city], city_visited)
            path.append((current_city, next_city))
            current_city = next_city
            city_visited.add(next_city)
        path.append((current_city, start_city))
        return path

    def select_next_city(self, pheromone, inversed_distance, city_visited):
        """
        Select and return next move based on probability (int).
        """
        pheromone = numpy.copy(pheromone)
        pheromone[list(city_visited)] = 0

        move_probability = (pheromone ** self.alpha) * (inversed_distance ** self.beta)
        move_probability = move_probability / move_probability.sum()

        next_city = numpy.random.choice(self.all_move, 1, p = move_probability)[0]
        return next_city

    def calculate_path_distance(self, path):
        """
        Calculate and return distance of a path (int).
        """
        distance = 0
        for city in path:
            distance += self.distance_matrix[city]
        return distance

    def update_pheromone(self, all_path):
        """
        Update pheromone based on decay and move.
        """
        sorted_path = sorted(all_path, key = lambda x: x[1])
        self.pheromone_matrix = (1 - self.decay) * self.pheromone_matrix
        for path, _ in sorted_path:
            for move in path:
                self.pheromone_matrix[move] += self.q / self.distance_matrix[move]
        