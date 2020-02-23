import numpy as np
from bandit import Bandit

class ContextualBandit(Bandit):
    #
    arms_mu = []
    totalReward = 0
    totalRegret = 0
    time = 0
    best_mu = 0
    rewards = []
    regrets = []
    #
    def __init__(self,time_horizon,number_of_arms,agent):
        self.time_horizon = time_horizon
        self.number_of_arms = number_of_arms
        self.agent = agent
        self.initEnviroment()
    #
    def initEnviroment(self):
        for i in range(self.number_of_arms):
            self.arms_mu.append(i+1)
        self.best_mu = self.number_of_arms
    #
    def reset(self):
        self.totalReward = 0
        self.totalRegret = 0
        self.time = 0
        self.rewards = []
        self.regrets = []    
        self.agent.reset()
    # 
    def createArm(self,sample_name,mu):
        return
    #
    def step(self):
        choosed_arm = self.agent.decide(self.time,self.time_horizon,self.number_of_arms)

        reward = np.random.normal(self.arms_mu[choosed_arm],1)        
        self.agent.observe(self.time,choosed_arm,reward)
        self.rewards.append(reward+self.totalReward)
        self.totalReward += reward

        regret = self.best_mu - reward
        self.regrets.append(regret+self.totalRegret)
        self.totalRegret += regret
    #
    def simulate(self):
        for t in range(self.time_horizon):
            self.time = t 
            self.step()

