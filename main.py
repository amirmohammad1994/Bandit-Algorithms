from experiment import *

n_sim = 40
params = [{
"time_horizon" :  1000,
"number_of_arms" : 10,
"number_of_exploration_per_arm" : 10,
},
{
"time_horizon" :  10000,
"number_of_arms" : 100,
"number_of_exploration_per_arm" : 10,
},
{
"time_horizon" :  10000,
"number_of_arms" : 200,
"number_of_exploration_per_arm" : 10,
},
{
"time_horizon" :  1000,
"number_of_arms" : 10,
"number_of_exploration_per_arm" : 100,
},]

createBanditInstancesAndSimulate(params,n_sim)
