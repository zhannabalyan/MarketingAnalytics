#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
from loguru import logger


class Visualization:
    """
    Handles visualization of multi-armed bandit experiment results.

    Class Attributes:
        eg_results(pd.DataFrame): Results from Epsilon-Greedy algorithm.
        ts_results(pd.DataFrame): Results from Thompson Sampling algorithm.
    """

    def __init__(self, eg_results, ts_results):
        """
        Stores the experiment results.

        Args:
            eg_results(pd.DataFrame): Results of 'Reward' and 'Regret' columns of Epsilon-Greedy algorithm.
            ts_results(pd.DataFrame): Results of 'Reward' and 'Regret' columns of Thompson Sampling algorithm.
        """
        self.eg_results = eg_results
        self.ts_results = ts_results

    def plot1(self):
        """
        Displays the learning progress of both algorithms as a smoothed reward curve.
        """
        logger.info("Plotting learning progress for both algorithms")

        plt.figure(figsize=(10,5))
        eg_mean = self.eg_results['Reward'].rolling(window=200).mean()
        ts_mean = self.ts_results['Reward'].rolling(window=200).mean()
        
        plt.plot(eg_mean, color='hotpink', label='Epsilon-Greedy')
        plt.plot(ts_mean, color='purple', label='Thompson Sampling')
        plt.title("Learning Curve")
        plt.xlabel("Trial")
        plt.ylabel("Average Reward")
        plt.legend()
        plt.show()

    def plot2(self):
        """
        Visualizes cumulative rewards and cumulative regrets for both algorithms.
        """
        logger.info("Plotting cumulative rewards and cumulative regrets")

        
        plt.figure(figsize=(10,5))
        plt.plot(self.eg_results['Reward'].cumsum(), color='hotpink', label='Epsilon-Greedy')
        plt.plot(self.ts_results['Reward'].cumsum(), color='purple', label='Thompson Sampling')
        plt.title("Cumulative Rewards Comparison")
        plt.xlabel("Trial")
        plt.ylabel("Cumulative Reward")
        plt.legend()
        plt.show()

        
        plt.figure(figsize=(10,5))
        plt.plot(self.eg_results['Regret'].cumsum(), color='hotpink', label='Epsilon-Greedy')
        plt.plot(self.ts_results['Regret'].cumsum(), color='purple', label='Thompson Sampling')
        plt.title("Cumulative Regret Comparison")
        plt.xlabel("Trial")
        plt.ylabel("Cumulative Regret")
        plt.legend()
        plt.show()


# In[ ]:




