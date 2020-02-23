from epsilon_greedy_agent import EpsilonGreedy
from ubc1_agent import UBC1Agent
from report import plot
from successive_elimination_agent import SuccessiveEliminationAgent
from agent import Agent
from explore_then_exploit_agent import ExploreThenExploit


def agentFactory(name,time_horizon,number_of_arms,parameter="foo"):
    if name == "epsilon-greedy":
        return EpsilonGreedy(time_horizon,number_of_arms,parameter)
    elif name == "explore-then-exploit":
        return ExploreThenExploit(time_horizon,number_of_arms,parameter)
    elif name == "ucb1":
        return UBC1Agent(time_horizon,number_of_arms)
    elif name == "successive-elimination":
        return SuccessiveEliminationAgent(time_horizon,number_of_arms)
    elif name == "random": 
        return Agent()
