import numpy as np
from bandit import Bandit

class ContextualBandit(Bandit):
    #
    contexts = []
    arm_context[]
    #
    def __init__(self,time_horizon,number_of_arms,agent):
      super().__init__()
    #
    def initEnviroment(self):
      super().initEnviroment()
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
    def contextReveal(self):
        return 0
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

