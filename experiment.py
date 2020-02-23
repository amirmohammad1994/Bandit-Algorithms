import numpy as np
import math
import matplotlib.pyplot as plt
from bandit import Bandit
from explore_then_exploit_agent import ExploreThenExploit
from MC_simulator import *
from epsilon_greedy_agent import EpsilonGreedy
from ubc1_agent import UBC1Agent
from report import plot

def createBanditInstancesAndSimulate(params,n_mc_sim):
    n_sim = n_mc_sim
    for i in range(len(params)):
        results = []
        time_horizon = params[i]['time_horizon']
        number_of_arms = params[i]['number_of_arms']
        number_of_exploration_per_arm = params[i]['number_of_exploration_per_arm']

        exp_agent = ExploreThenExploit(time_horizon,number_of_arms,number_of_exploration_per_arm)
        epsilon_greedy_constant_half_epsilonAgent = EpsilonGreedy(time_horizon,number_of_arms,[1/2]*time_horizon)
        epsilon_greedy_constant_epsilonAgent = EpsilonGreedy(time_horizon,number_of_arms,[number_of_exploration_per_arm*number_of_arms/time_horizon]*time_horizon)
        ubc_agent = UBC1Agent(time_horizon,number_of_arms)

        bandit = Bandit(time_horizon,number_of_arms,exp_agent)
        results.append(mc_simulate(n_sim,bandit))

        bandit = Bandit(time_horizon,number_of_arms,epsilon_greedy_constant_epsilonAgent)
        results.append(mc_simulate(n_sim,bandit,"constant-epsilon=rate-of-explore-exploit"))

        bandit = Bandit(time_horizon,number_of_arms,epsilon_greedy_constant_half_epsilonAgent)
        results.append(mc_simulate(n_sim,bandit,"constant-epsilon=0.5"))

        bandit = Bandit(time_horizon,number_of_arms,ubc_agent)
        results.append(mc_simulate(n_sim,bandit))
        
        plot(results,time_horizon,params[i])

        