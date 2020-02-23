import numpy as np
import math
import matplotlib.pyplot as plt
from bandit import Bandit
from explore_then_exploit_agent import ExploreThenExploit
from MC_simulator import *
from epsilon_greedy_agent import EpsilonGreedy
from ubc1_agent import UBC1Agent
from report import plot
from successive_elimination_agent import SuccessiveEliminationAgent
from agent import Agent
from agent_factory import agentFactory

n_sim = 40

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
        se_agent = SuccessiveEliminationAgent(time_horizon,number_of_arms) 
        random_agent = Agent()
        
        bandit = Bandit(time_horizon,number_of_arms,random_agent)
        results.append(mc_simulate(n_sim,bandit))

        bandit = Bandit(time_horizon,number_of_arms,exp_agent)
        results.append(mc_simulate(n_sim,bandit))

        bandit = Bandit(time_horizon,number_of_arms,epsilon_greedy_constant_epsilonAgent)
        results.append(mc_simulate(n_sim,bandit,"constant-epsilon=rate-of-explore-exploit"))

        bandit = Bandit(time_horizon,number_of_arms,epsilon_greedy_constant_half_epsilonAgent)
        results.append(mc_simulate(n_sim,bandit,"constant-epsilon=0.5"))

        bandit = Bandit(time_horizon,number_of_arms,ubc_agent)
        results.append(mc_simulate(n_sim,bandit))

        bandit = Bandit(time_horizon,number_of_arms,se_agent)
        results.append(mc_simulate(n_sim,bandit))

        plot(results,time_horizon,params[i])


def experiment1():
    params = [{
        "time_horizon" : 1000,
        "number_of_arms" : 5
    },
    {
        "time_horizon" : 10000,
        "number_of_arms" : 5
    },
    {
        "time_horizon" : 1000,
        "number_of_arms" : 10
    },
    {
        "time_horizon" : 10000,
        "number_of_arms" : 10
    },
    {
        "time_horizon" : 1000,
        "number_of_arms" : 20
    },
    {
        "time_horizon" : 10000,
        "number_of_arms" : 20
    },
    ]
    
    for i in range(len(params)):
        results = []
        time_horizon = params[i]["time_horizon"]
        number_of_arms = params[i]["number_of_arms"]
        agent1 = agentFactory("explore-then-exploit",time_horizon,number_of_arms,5)
        agent2 = agentFactory("explore-then-exploit",time_horizon,number_of_arms,time_horizon/10)
        agent3 = agentFactory("explore-then-exploit",time_horizon,number_of_arms,time_horizon/100)
        
        bandit = Bandit(time_horizon,number_of_arms,agent1)
        results.append(mc_simulate(n_sim,bandit,"N=5"))
 
        bandit = Bandit(time_horizon,number_of_arms,agent2)
        results.append(mc_simulate(n_sim,bandit,"N=T/10"))
        
        bandit = Bandit(time_horizon,number_of_arms,agent3)
        results.append(mc_simulate(n_sim,bandit,"N=T/100"))

        plot(results,time_horizon,params[i])


def experiment1():
    params = [{
        "time_horizon" : 1000,
        "number_of_arms" : 5
    },
    {
        "time_horizon" : 10000,
        "number_of_arms" : 5
    },
    {
        "time_horizon" : 1000,
        "number_of_arms" : 10
    },
    {
        "time_horizon" : 10000,
        "number_of_arms" : 10
    },
    {
        "time_horizon" : 1000,
        "number_of_arms" : 20
    },
    {
        "time_horizon" : 10000,
        "number_of_arms" : 20
    },
    ]
    
    for i in range(len(params)):
        results = []
        time_horizon = params[i]["time_horizon"]
        number_of_arms = params[i]["number_of_arms"]
        agent1 = agentFactory("explore-then-exploit",time_horizon,number_of_arms,5)
        agent2 = agentFactory("explore-then-exploit",time_horizon,number_of_arms,time_horizon/10)
        agent3 = agentFactory("explore-then-exploit",time_horizon,number_of_arms,time_horizon/100)
        
        bandit = Bandit(time_horizon,number_of_arms,agent1)
        results.append(mc_simulate(n_sim,bandit,"N=5"))
 
        bandit = Bandit(time_horizon,number_of_arms,agent2)
        results.append(mc_simulate(n_sim,bandit,"N=T/10"))
        
        bandit = Bandit(time_horizon,number_of_arms,agent3)
        results.append(mc_simulate(n_sim,bandit,"N=T/100"))

        plot(results,time_horizon,params[i])


def experiment2():
    params = [{
        "time_horizon" : 500,
        "number_of_arms" : 5
    },
    {
        "time_horizon" : 5000,
        "number_of_arms" : 5
    },
    {
        "time_horizon" : 500,
        "number_of_arms" : 10
    },
    {
        "time_horizon" : 5000,
        "number_of_arms" : 10
    },
    {
        "time_horizon" : 500,
        "number_of_arms" : 20
    },
    {
        "time_horizon" : 5000,
        "number_of_arms" : 20
    },
    ]
    
    for i in range(len(params)):
        results = []
        time_horizon = params[i]["time_horizon"]
        number_of_arms = params[i]["number_of_arms"]
        agent1 = agentFactory("random",time_horizon,number_of_arms)
        
        epsilons = []
        for j in range(time_horizon):
            epsilons.append(math.pow((j+1)*number_of_arms*math.log(j+1),1/3))
        
        agent2 = agentFactory("epsilon-greedy",time_horizon,number_of_arms,epsilons)
        agent3 = agentFactory("explore-then-exploit",time_horizon,number_of_arms,time_horizon/100)
        agent4 = agentFactory("ucb1",time_horizon,number_of_arms)
        agent5 = agentFactory("successive-elimination",time_horizon,number_of_arms)

        bandit = Bandit(time_horizon,number_of_arms,agent1)
        results.append(mc_simulate(n_sim,bandit))
 
        bandit = Bandit(time_horizon,number_of_arms,agent2)
        results.append(mc_simulate(n_sim,bandit))
        
        bandit = Bandit(time_horizon,number_of_arms,agent3)
        results.append(mc_simulate(n_sim,bandit,"N=T/100"))

        bandit = Bandit(time_horizon,number_of_arms,agent4)
        results.append(mc_simulate(n_sim,bandit))
        
        bandit = Bandit(time_horizon,number_of_arms,agent5)
        results.append(mc_simulate(n_sim,bandit))

        plot(results,time_horizon,params[i])
