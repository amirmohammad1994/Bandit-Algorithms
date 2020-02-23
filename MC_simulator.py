from bandit import Bandit
from util import *
import numpy as np


def mc_simulate(n,bandit):
    result = {}
    result['totalReward'] = 0
    result['totalRegret'] = 0
    result['regrets'] = [0]*bandit.time_horizon
    result['regrets'] = np.array(result['regrets'])
    result['rewards'] = [0]*bandit.time_horizon
    result['rewards'] = np.array(result['rewards'])

    for i in range(n):
        bandit.reset()
        bandit.simulate()
        result['totalReward'] = incrementalAvg(i+1,result['totalReward'],bandit.totalReward)        
        result['totalRegret'] = incrementalAvg(i+1,result['totalRegret'],bandit.totalRegret)        
        result['regrets'] = (result['regrets']*(i) + np.array(bandit.regrets)) / (i+1)        
        result['rewards'] = (result['rewards']*(i) + np.array(bandit.rewards)) / (i+1)        
    
    return result            