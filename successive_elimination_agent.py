from agent import Agent 
from util import *
import numpy as np
import math

class SuccessiveEliminationAgent(Agent):
    best_arm = 0
    last_arm = 0
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
        self.last_arm = 0
        self.arms_visited = [0]*self.number_of_arms
        self.ubc = [0]*self.number_of_arms
        self.lbc = [0]*self.number_of_arms
        self.active_arms = np.arange(self.number_of_arms)
        self.active_arms_snapshot = np.arange(self.number_of_arms)
        print('successive-elimination agent started to decide.')
    #
    def decide(self,time,time_horizon,number_of_arms):
        arm = 0
        if self.last_arm == len(self.active_arms_snapshot):
            self.last_arm = 0
            self.active_arms_snapshot = np.copy(self.active_arms)
        arm = self.active_arms_snapshot[self.last_arm]
        self.last_arm += 1

        self.arms_visited[arm] += 1
        return arm         
    #
    def observe(self,time,arm,reward):
        self.mu_estimators[arm] = incrementalAvg(self.arms_visited[arm],self.mu_estimators[arm],reward)
        self.ubc[arm] = self.mu_estimators[arm] + math.sqrt(2*math.log(self.time_horizon)/self.arms_visited[arm])
        self.lbc[arm] = self.mu_estimators[arm] - math.sqrt(2*math.log(self.time_horizon)/self.arms_visited[arm])
        
        updated_actives = np.copy(self.active_arms)

        if len(self.active_arms) > 0:
            for a in self.active_arms:
                if np.max(self.lbc) > self.ubc[a] and self.arms_visited[a] > 0:
                    #print(np.max(self.lbc))
                    #print(self.lbc[a],self.ubc[a])
                    updated_actives = updated_actives[updated_actives != a]
        self.active_arms = updated_actives

            