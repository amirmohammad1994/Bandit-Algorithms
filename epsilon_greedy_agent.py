from agent import Agent 
from util import *
import numpy as np

class EpsilonGreedy(Agent):
    best_arm = 0
    #
    def __init__(self,time_horizon,number_of_arms,epsilons):
        self.time_horizon = time_horizon
        self.number_of_arms = number_of_arms
        self.epsilons = epsilons
        self.reset()
        self.name = "epsilon-greedy"
    #
    def reset(self):
        self.mu_estimators = [0]*self.number_of_arms
        self.best_arm = 0
        self.arms_visited = [0]*self.number_of_arms
        print('epsilon-greedy agent started to decide.')

    #
    def decide(self,time,time_horizon,number_of_arms):
        coin = np.random.random_sample()
        #explore
        if coin < self.epsilons[time]:
            arm = np.random.randint(number_of_arms)
        #exploit
        else:
            self.best_arm = np.argmax(self.mu_estimators)
            arm = self.best_arm

        self.arms_visited[arm] += 1
        return arm
         
    #
    def observe(self,time,arm,reward):
        self.mu_estimators[arm] = incrementalAvg(self.arms_visited[arm],self.mu_estimators[arm],reward)