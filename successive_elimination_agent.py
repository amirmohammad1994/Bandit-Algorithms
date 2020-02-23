from agent import Agent 
from util import *
import numpy as np
import math

class SuccessiveEliminationAgent(Agent):
    best_arm = 0
    #
    def __init__(self,time_horizon,number_of_arms):
        self.time_horizon = time_horizon
        self.number_of_arms = number_of_arms
        self.reset()
        self.name = "successive-elimination"
    #
    def reset(self):
        self.mu_estimators = [0]*self.number_of_arms
        self.best_arm = 0
        self.arms_visited = [0]*self.number_of_arms
        self.ubc = [0]*self.number_of_arms
        self.lbc = [0]*self.number_of_arms

    #
    def decide(self,time,time_horizon,number_of_arms):
        arm = 0

        #explore
        if time<number_of_arms:
            arm = time
        #exploit
        else :
            arm = np.argmax(self.ubc)

        self.arms_visited[arm] += 1
        return arm         
    #
    def observe(self,time,arm,reward):
        self.mu_estimators[arm] = incrementalAvg(self.arms_visited[arm],self.mu_estimators[arm],reward)
        self.ubc[arm] = self.mu_estimators[arm] + math.sqrt(2*math.log(self.time_horizon)/self.arms_visited[arm])
        self.lbc[arm] = self.mu_estimators[arm] - math.sqrt(2*math.log(self.time_horizon)/self.arms_visited[arm])