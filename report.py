import matplotlib.pyplot as plt
import numpy as np

def plot(results,time_horizon,params):
    plt.rcParams["figure.figsize"] = (20,12)

    t_axis = np.arange(0,time_horizon,1)
    plt.suptitle(params)

    plt.subplot(2, 1, 1)
    for result in results:
        plt.plot(t_axis,result['regrets'],label=result['name'])     
    plt.title('Regret')
    plt.legend(loc='upper left',prop={'size': 10})
    
    plt.subplot(2, 1, 2)
    for result in results:
        plt.plot(t_axis,result['rewards'],label=result['name'])     
    plt.title('Reward')
    plt.legend(loc='upper left',prop={'size': 10})
    plt.show()
