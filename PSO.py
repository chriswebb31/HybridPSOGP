import math
import random
import numpy as np
from Particle import Particle

class ParticleSwarmOptimisation:
    def __init__(self, problem):
        self.problem = problem
        self.problem_size = len(problem.values[0])
        self.problem_targets = problem.targets
        self.problem_values = problem.values
#         self.problem_size = len(problem)

    def randomPoint(self, bound, variation):
        low = bound - variation
        high = bound + variation
        new_point = random.uniform(low, high)
#         new_point = np.random.uniform(low=low, high=high, size=self.problem_size)
        return new_point

    def randomPosition(self, problem):
        new_position = []
        for point in problem:
            new_position.append(randomPoint(point, point/10))
        return new_position

    def randomPosition(self):
        return np.random.uniform(low=-1, high=1, size=self.problem_size)


    def initialiseSwarmPostGP(self, best_sol):
        swarm_size = int(20 + math.sqrt(self.problem_size))
        self.swarm = []
        average = np.average(best_sol)
        variation = average / 10
        for i in range(swarm_size):
            self.swarm.append(Particle(best_sol, self.randomPoint(average, variation)))

    def initialiseSwarmPreGP(self):
        swarm_size = int(20 + math.sqrt(self.problem_size))
        self.swarm = []
        for i in range(swarm_size):
            self.swarm.append(Particle(self.randomPosition(), self.randomPosition()))

    def optimise(self):
        best = 0
        for i in range(1000):
            best = self.globalBest()
            for particle in self.swarm:
                particle.updateVelocity(best)
                particle.updatePosition()
                particle.updateLocalBest()
#         for i in range(len(best)):
        # print("Best = ", best)
        # print("\n\n\n\n\n\n")
        #
        # quick_test = [64.5,164.75, 30.75 ,21.5,0,122.75,42.5,0,0,0,0,1,0]
        # print(np.sum(np.multiply(best,quick_test)))


        return best

    def evaluate(self, particle):
        new_vals = []
        for i in range(len(self.problem_values)):
            temp = np.sum(np.multiply(self.problem_values[i], particle))
            new_vals.append(abs(temp - self.problem_targets[i]))
        fitness = np.sum(new_vals) / self.problem_size
        return fitness

    def globalBest(self):
#         self.problem.evaluatePSO(particle)
        best_particle = self.swarm[0].best
#         best_fitness = self.problem.evaluatePSO(best_particle)
        for particle in self.swarm[1:]:
            best_fitness = self.evaluate(best_particle)
            temp = self.evaluate(particle.best)
            if best_fitness > temp:
                best_particle = particle.best
        return best_particle
#         for i in swarm[1:]:
#             if
