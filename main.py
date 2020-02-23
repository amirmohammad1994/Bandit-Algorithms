import numpy as np
import math
import matplotlib.pyplot as plt
from bandit import Bandit
from explore_then_exploit_agent import ExploreThenExploit
from MC_simulator import *
from epsilon_greedy_agent import EpsilonGreedy
#
time_horizon = 1000
number_of_arms = 10
number_of_exploration_per_arm = 10
n_sim = 40

exp_Agent = ExploreThenExploit(time_horizon,number_of_arms,number_of_exploration_per_arm)
epsilon_greedy_constant_half_epsilonAgent = EpsilonGreedy(time_horizon,number_of_arms,[1/2]*time_horizon)
epsilon_greedy_constant_epsilonAgent = EpsilonGreedy(time_horizon,number_of_arms,[number_of_exploration_per_arm*number_of_arms/time_horizon]*time_horizon)

bandit = Bandit(time_horizon,number_of_arms,exp_Agent)
result = mc_simulate(n_sim,bandit)

bandit = Bandit(time_horizon,number_of_arms,epsilon_greedy_constant_epsilonAgent)
result2 = mc_simulate(n_sim,bandit)

bandit = Bandit(time_horizon,number_of_arms,epsilon_greedy_constant_half_epsilonAgent)
result3 = mc_simulate(n_sim,bandit)
#
t_axis = np.arange(0,time_horizon,1)

plt.plot(t_axis,result['regrets'],t_axis,result2['regrets'],t_axis,result3['regrets'])
plt.suptitle('Regret')
plt.show()
plt.plot(t_axis,result['rewards'],t_axis,result2['rewards'],t_axis,result3['rewards'])
plt.suptitle('Reward')
plt.show()


