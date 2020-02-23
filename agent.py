import numpy as np

class Agent:
    name = 'random'
    def __init__(self):
        return
    def reset(self):
        return
    def decide(self,time,time_horizon,number_of_arms):
         return np.random.randint(number_of_arms)
    def observe(self,time,arm,reward):
        return