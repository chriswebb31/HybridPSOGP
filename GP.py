import random
import numpy as np

class GeneticProgrammingOptimisation:
    def __init__(self, problem, pso_solution):
        self.problem = problem
        self.problem_size = len(problem.values[0])
        self.problem_targets = problem.targets
        self.problem_values = problem.values
        self.num_weights = 13
        self.solutions_per_population = 8
        self.num_mating_parents = 4
        self.population_size = (self.solutions_per_population, self.num_weights)
        self.num_generations = 500
        self.pso_solution = pso_solution

    def optimise(self):
        try:
            if self.pso_solution == None:
                self.population = self.createNewPopulation()
        except:
            self.population = self.createPSOPopulation()
        for generation in range(self.num_generations):

            # Measing the fitness of each chromosome in the population.
            fitness = self.calcPopulationFitness()

            # Selecting the best parents in the population for mating.
            parents = self.selectMatingPool(fitness)

            # Generating next generation using crossover.
            offspring_crossover = self.crossover(parents,
                                               offspring_size=(self.population_size[0]-parents.shape[0], self.num_weights))

            # Adding some variations to the offsrping using mutation.
            offspring_mutation = self.mutation(offspring_crossover)

            # Creating the new population based on the parents and offspring.
            self.population[0:parents.shape[0], :] = parents
            self.population[parents.shape[0]:, :] = offspring_mutation

            # The best result in the current iteration.
            # print("Best result : ", self.calcPopulationFitness())

        # Getting the best solution after iterating finishing all generations.
        #At first, the fitness is calculated for each solution in the final generation.
        fitness = self.calcPopulationFitness()
        # Then return the index of that solution corresponding to the best fitness.
        best_match_idx = np.where(fitness == np.min(abs(fitness)))
        sol = self.population[best_match_idx, :][0][0]
        return sol

    def createNewPopulation(self):
        return np.random.uniform(low=-1, high=1, size=self.population_size)

    def createPSOPopulation(self):
        population = np.empty(self.population_size)
        for i in range(self.solutions_per_population):
            for j in range(len(self.pso_solution)):
                point = self.pso_solution[j]
                variation = point/10
                population[i][j] = random.uniform(point-variation, point+variation)
        return population


    def calcPopulationFitness(self):
        # Calculating the fitness value of each solution in the current population.
        # The fitness function calculates the sum of products between each input and its corresponding weight.

        all_fitness = []
        for i in range(len(self.problem_values)):
            values = np.sum(self.population*self.problem_values[i], axis = 1)
            fitness = np.absolute(np.subtract(values, self.problem_targets[i]))
            all_fitness.append(fitness)
        sum_of_fitness = [sum(i) for i in zip(*all_fitness)]
        average_fitness = np.divide(sum_of_fitness, len(self.problem_targets))
        return average_fitness

    def selectMatingPool(self, fitness):
        # Selecting the best individuals in the current generation as parents for producing the offspring of the next generation.
        parents = np.empty((self.num_mating_parents, self.population.shape[1]))
        for parent_num in range(self.num_mating_parents):
            max_fitness_idx = np.where(fitness == np.min(abs(fitness)))

            max_fitness_idx = max_fitness_idx[0][0]
            parents[parent_num, :] = self.population[max_fitness_idx, :]
            fitness[max_fitness_idx] = -99999999999
        return parents

    def crossover(self, parents, offspring_size):
        offspring = np.empty(offspring_size)
        # The point at which crossover takes place between two parents. Usually it is at the center.
        crossover_point = np.uint8(offspring_size[1]/2)

        for k in range(offspring_size[0]):
            # Index of the first parent to mate.
            parent1_idx = k%parents.shape[0]
            # Index of the second parent to mate.
            parent2_idx = (k+1)%parents.shape[0]
            # The new offspring will have its first half of its genes taken from the first parent.
            offspring[k, 0:crossover_point] = parents[parent1_idx, 0:crossover_point]
            # The new offspring will have its second half of its genes taken from the second parent.
            offspring[k, crossover_point:] = parents[parent2_idx, crossover_point:]
        return offspring

    def mutation(self, offspring_crossover):
        # Mutation changes a single gene in each offspring randomly.
        for idx in range(offspring_crossover.shape[0]):
            # The random value to be added to the gene.
            random_value = np.random.uniform(-1.0, 1.0, 1)
            offspring_crossover[idx, 4] = offspring_crossover[idx, 4] + random_value
        return offspring_crossover
