import random
import numpy as np

class Particle:
    def __init__(self, pos1, pos2):
        self.position = pos1
        self.velocity = np.divide(np.subtract(pos2, pos1), 2)
        self.best = pos1
        self.eta = np.reciprocal(np.multiply(2, np.log(2)))
        self.phi = np.add(0.5, np.log(2))

    def updateVelocity(self, global_best):
        self.velocity = np.add(np.add(np.multiply(self.eta, self.velocity),
                                 np.multiply(self.phi * random.random(),
                                             np.subtract(self.best, self.position))),
                          np.multiply(self.phi * random.random(),
                                      np.subtract(global_best, self.position)))

    def updateLocalBest(self):
        if abs(np.sum(self.best)) > abs(np.sum(self.position)):
            self.best = self.position


    def updatePosition(self):
        self.position = np.add(self.position, self.velocity)
