#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
Epsilon-Greedy Algorithm for Multi-Armed Bandit Problem
Implements exploration-exploitation tradeoff with decaying epsilon.
"""


import numpy as np

import pandas as pd

from loguru import logger

from Bandit import Bandit


class EpsilonGreedy(Bandit):
    
    """
    Epsilon-Greedy strategy implementation.

    Class Attributes:
        true_means(np.ndarray): True reward probabilities of each arm.
        
        n_arms(int): Total number of arms.
        
        epsilon(float): Exploration rate (updated over time).
        
        pulls(np.ndarray): Number of times each arm was pulled.
        
        estimates(np.ndarray): Estimated reward means per arm.
        
        rewards(list): List of obtained rewards.
        
        chosen_arms(list): List of arm indices chosen per trial.
    """

    def __init__(self, true_means, epsilon_start=1.0):
        """
        Initializing the algorithm.

        Args:
            true_means (Sequence[float]): The real average reward values for each arm.
            epsilon_start (float, optional): Starting exploration probability and setting default to 1.0.
        """
        self.true_means = np.array(true_means)
        self.n_arms = len(true_means)
        self.epsilon = epsilon_start
        self.pulls = np.zeros(self.n_arms)
        self.estimates = np.zeros(self.n_arms)
        self.rewards = []
        self.chosen_arms = []

    def __repr__(self):
        return f"<EpsilonGreedy Agent | epsilon={self.epsilon:.3f}, arms={self.n_arms}>"

    def select_arm(self):
        """
        Decide which arm to pull based on epsilon-greedy logic.

        Returns:
            int: Index of chosen arm.
        """
        explore = np.random.rand() < self.epsilon
        if explore:
            arm_index = np.random.randint(self.n_arms)
        else:
            arm_index = np.argmax(self.estimates)
        return arm_index

    def pull(self):
        """
        Pull a selected arm and observe reward.

        Returns:
            tuple: (chosen_arm, observed_reward)
        """
        arm = self.select_arm()
        reward = np.random.normal(self.true_means[arm], 1)
        return arm, reward

    def update(self, arm, reward):
        """
        Update internal reward estimates after each pull.

        Args:
            arm (int): Arm index that was pulled.
            reward (float): Reward obtained.
        """
        self.pulls[arm] += 1
        count = self.pulls[arm]
        current_estimate = self.estimates[arm]
        self.estimates[arm] = current_estimate + (reward - current_estimate) / count

    def experiment(self, n_trials=20000):
        """
        Run the epsilon-greedy experiment.

        Args:
            n_trials (int): Number of iterations to perform.

        Returns:
            pd.DataFrame: Trial-by-trial record of arms, rewards, and regrets.
        """
        logger.info("Starting Epsilon-Greedy simulation")

        best_true_mean = np.max(self.true_means)

        for t in range(1, n_trials + 1):
            self.epsilon = 1 / t
            arm, reward = self.pull()
            self.update(arm, reward)
            self.rewards.append(reward)
            self.chosen_arms.append(arm)

        regrets = best_true_mean - np.array([self.true_means[a] for a in self.chosen_arms])
        results = pd.DataFrame({
            "Trial": np.arange(1, n_trials + 1),
            "Arm": self.chosen_arms,
            "Reward": self.rewards,
            "Regret": regrets,
            "Algorithm": "Epsilon-Greedy"
        })

        logger.success("Epsilon-Greedy simulation complete.")
        return results

    def report(self):
        """
        Summarize and log the experimental performance.
        """
        mean_reward = np.mean(self.rewards)
        total_regret = np.sum(np.max(self.true_means) - np.array([self.true_means[a] for a in self.chosen_arms]))

        logger.info(f"[Epsilon-Greedy] Average Reward: {mean_reward:.4f}")
        logger.info(f"[Epsilon-Greedy] Total Regret: {total_regret:.4f}")


# In[ ]:




