#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

from epsilon_greedy_algorithm import EpsilonGreedy
from thompson_sampling_algorithm import ThompsonSampling
from plots import Visualization


# In[2]:


bandit_means = [1, 2, 3, 4]


# In[3]:


#Initializing the algorithm here.

epsilon_bandit = EpsilonGreedy(bandit_means)
thompson_bandit = ThompsonSampling(bandit_means)


# In[4]:


#Running the experiments here.

results_epsilon = epsilon_bandit.experiment()
results_thompson = thompson_bandit.experiment()


# In[5]:


epsilon_bandit.report()
thompson_bandit.report()


# In[6]:


plotting = Visualization(results_epsilon,results_thompson)


# In[7]:


plotting.plot1()
plotting.plot2()


# In[8]:


final_outputs = pd.concat([results_epsilon, 
                           results_thompson],
                          axis=0)

final_outputs.to_csv("outputs.csv", index=False)

final_outputs.head()


# **Findings**
# 
# In this assignment, we designed and tested two bandit algorithms, the Epsilon-Greedy algorithm and the Thompson Sampling algorithm on a 4-arm problem with true arm means being 1,2,3 and 4. We had 20000 trials for each.
# When we ran the two algorithms here, the Epsilon-Greedy algorithm displayed an average reward of 4.0013 and 
# a total regret of 21. After this, when we ran the Thompson Sampling algorithm, it gave an average reward of 3.9284
# and a total regret of 0.0716.
# 
# When we look at the plot of the learning curve that we visualized above, we can compare how quickly each of the 
# algorithms learn and choose the best arm.
# First of all, we see that The Epsilon-Greedy curve starts lower because it explores all arms right from the start, but then it quickly rises and stabilizes around 4, which is the true mean of the best arm. Once it finds the best option, it doesn't switch or fluctuate and the curve starts becoming flat at the top. Meanwhile, the Thompson Sampling curve starts similarly to the Epsilon-Greedy curve,but grows slower. In the beginning, it keeps exploring more due to its probabilistic sampling, so it sometimes picks suboptimal arms. The curve still rises over time but takes longer to reach the peak. It eventually approaches 4, which means that it chooses the best arm too but more gradually.
# Overall, the learning curve shows that Epsilon-Greedy learns faster, while Thompson Sampling learns steadier.
# 
# When we look at the second plot, we see that it tracks how much total reward each algorithm has earned over all trials.
# Both lines increase almost linearly because both algorithms are collecting rewards almost every trial.
# The Epsilon-Greedy line is slightly above the Thompson Sampling line the whole time, which means it earns more total reward overall. This is because it found the best arm faster and spent more time exploiting it.
# The two lines become nearly parallel after a while, which means that once both algorithms learned enough, they performed similarly.
# 
# Finally, when we look at the last plot, we see how much total reward each algorithm lost by not always picking the most optimal arm. Here, the Epsilon-Greedy algorithm shows a sharp increase in regret at the beginning, then it rises quickly around 21. That means after its early exploration, it almost always chose the most optimal arm and made very few mistakes. In comparison, the Thompson Sampling algorithm starts with a steeper curve making more mistakes from the start and the line keeps rising for longer. Eventually, it flattens as it eventually learns the most optimal arm.
# 
# 

# In[ ]:




