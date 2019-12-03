import sys
import time
from Problem import Problem
from GP import GeneticProgrammingOptimisation
from PSO import ParticleSwarmOptimisation
# from HGPPSO import HGPPSO
# from HPSOGP import HPSOGP

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print("Enter the type of optimisation to solve the problem")
        print("(1) - Particle Swarm Optimisation")
        print("(2) - Genetic Programming Optimisation")
        print("(3) - Hybrid PSO GP Optimisation")
        print("(4) - Hybrid GP PSO Optimisation")
    elif sys.argv[1] == "1":
        problem = Problem('cwk_train.csv', 'cwk_test.csv')
        problem.defineProblem()
        epoch = 100
        counter = 0
        best_average_cost = 99999
        start_time = time.time()
        while counter < epoch:
            print("Epoch ", counter)
            pso = ParticleSwarmOptimisation(problem)
            pso.initialiseSwarmPreGP()
            pso_best = pso.optimise()
            if problem.testProblem(pso_best) < best_average_cost:
                best_average_cost = problem.testProblem(pso_best)
                best_solution = pso_best
            counter += 1
        total_time = time.time() - start_time
        print("Time Taken: ", total_time)
        print("Solution: ", best_solution)
        print("Cost: ", best_average_cost)
    elif sys.argv[1] == "2":
        problem = Problem('cwk_train.csv', 'cwk_test.csv')
        problem.defineProblem()
        epoch = 1000
        counter = 0
        best_average_cost = 99999
        start_time = time.time()
        while counter < epoch:
            print("Epoch ", counter)
            gp = GeneticProgrammingOptimisation(problem, None)
            gp_best = gp.optimise()
            if problem.testProblem(gp_best) < best_avergae_cost:
                best_average_cost = problem.testProblem(gp_best)
                best_solution = gp_best
            counter += 1
        total_time = time.time() - start_time
        print("Time Taken: ", total_time)
        print("Solution: ", best_solution)
        print("Cost: ", best_average_cost)
    elif sys.argv[1] == "3":
        problem = Problem('cwk_train.csv', 'cwk_test.csv')
        problem.defineProblem()
        epoch = 1000
        counter = 0
        error_counter = 0
        best_average_cost = 99999
        start_time = time.time()
        while counter < epoch:
            print("Epoch ", counter)
            pso = ParticleSwarmOptimisation(problem)
            pso.initialiseSwarmPreGP()
            pso_best = pso.optimise()
            gp = GeneticProgrammingOptimisation(problem, pso_best)
            gp_best = gp.optimise()
            if problem.testProblem(gp_best) < best_average_cost:
                best_average_cost = problem.testProblem(gp_best)
                best_solution = gp_best
            if problem.testProblem(gp_best) > problem.testProblem(pso_best):
                error_counter += 1
            counter += 1
        total_time = time.time() - start_time
        print("Time Taken: ", total_time)
        print("Error Count: ", error_counter)
        print("Error Percentage: ", error_counter/epoch*100, "%")
        print("Solution: ", best_solution)
        print("Cost: ", best_average_cost)
    elif sys.argv[1] == "4":
        problem = Problem('cwk_train.csv', 'cwk_test.csv')
        problem.defineProblem()
        epoch = 1000
        counter = 0
        error_counter = 0
        best_average_cost = 99999
        start_time = time.time()
        while counter < epoch:
            print("Epoch ", counter)
            gp = GeneticProgrammingOptimisation(problem, None)
            gp_best = gp.optimise()
            pso = ParticleSwarmOptimisation(problem)
            pso.initialiseSwarmPostGP(gp_best)
            pso_best = pso.optimise()
            if problem.testProblem(pso_best) < best_average_cost:
                best_average_cost = problem.testProblem(pso_best)
                best_solution = pso_best
            if problem.testProblem(gp_best) < problem.testProblem(pso_best):
                error_counter += 1
            counter += 1
        total_time = time.time() - start_time
        print("Time Taken: ", total_time)
        print("Error Count: ", error_counter)
        print("Error Percentage: ", error_counter/epoch*100, "%")
        print("Solution: ", best_solution)
        print("Cost: ", best_average_cost)
