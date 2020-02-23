################################
###                          ###
###  کد روزی که ارائه دادیم  ###
###                          ###
################################


import numpy as np
import math
import matplotlib.pyplot as plt



def Algorithm(K,T,N,mu_array,kind):
    reward = 0
    regret = 0
    regret_series = []
    #finding best arm
    best_mu = max(mu_array)
    #uniform algorithm
    mu_estimator = [0]*K
    
    #exploration
    n_count = 1
    a = 0
    if(kind=="uniform"):
        for i in range(min(K*N,T)):
            r = np.random.random_sample() + mu_array[a]-1/2
            #update mean
            mu_estimator[a] *= n_count - 1
            mu_estimator[a] += r 
            mu_estimator[a] /= n_count
            #
            n_count += 1
            if (n_count == N+1):
                n_count = 1
                a += 1
            #
            reward += r        
            regret += (best_mu-r)
            regret_series.append(regret)

        #best estimated arm
        a = np.argmax(mu_estimator)

        #exploitation
        for i in range(max(0,T-K*N)):
            #a = algorithm(params)
            r = np.random.random_sample()+mu_array[a]-1/2
            reward += r        
            regret += (best_mu-r)
            regret_series.append(regret)
            
    if(kind=='greedy'):
        for i in range(T):
            e_t = math.pow(i*K*math.log(i+1),1/3) 
            rand = np.random.random_sample()
            if(rand > e_t):
                #explore
                a = math.floor(np.random.random_sample()*K)
                r = np.random.random_sample()+mu_array[a]-1/2
                mu_estimator[a] = (mu_estimator[a]+r)/2
            else:
                #exploit
                a = np.argmax(mu_estimator)
                r = np.random.random_sample()+mu_array[a]-1/2
            reward += r        
            regret += (best_mu-r)
            regret_series.append(regret)
        #
    retDict = {
                "regret":regret,
                "regret_series":regret_series,
                "reward":reward,
                "K":K,
                "T":T
    }
    return retDict

def Simulate(alg,n_sim,K=10,T=1000,N=20):
    regrets = []
    regret_series_plot = []
    for i in range(n_sim):
        mu = np.random.random_sample(K)*10
        ret = Algorithm(K,T,N,mu,alg)
        regrets.append(ret['regret'])
        if(i == 0):
            regret_series_plot = ret['regret_series']
    #
    t = np.arange(0,n_sim,1)
    t_series = np.arange(0,T,1)
    
    #plotting
    theory_formula = []
    theory_formula_series = []
    mean_of_regrets = [np.mean(regrets)]*n_sim

    for i in range(n_sim):
        theory_formula.append(math.sqrt(T*T*math.log(T)*K)**(1/3))
    for i in range(T):    
        theory_formula_series.append(math.sqrt((i+1)*(i+1)*math.log(i+1)*K)**(1/3))

    plt.plot(t,theory_formula,'g',t,regrets,'b',t,mean_of_regrets,'r')
    plt.suptitle('Regret')
    plt.show()
    plt.plot(t_series,theory_formula_series,'g',t_series,regret_series_plot,'b')
    plt.suptitle('Regret Series')
    plt.show()

    