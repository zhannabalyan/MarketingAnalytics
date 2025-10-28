#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from loguru import logger
from Bandit import Bandit

class ThompsonSampling(Bandit):
    """
    Thompson Sampling algorithm for multi-armed bandits.

    This algorithm keeps track of uncertainty for each arm using Beta distributions.
    At each trial, it samples from each arm's posterior and chooses the arm with
    the highest sampled value. The posterior is updated based on observed rewards.

    Class Attributes:
        arm_means(np.ndarray): True mean rewards of each arm.
        
        num_arms(int): Total number of arms.
        
        posterior_a(np.ndarray): Alpha parameters of Beta distributions (success counts).
        
        posterior_b(np.ndarray): Beta parameters of Beta distributions (failure counts).
        
        collected_rewards(list): Rewards recorded for each trial.
        
        chosen_arm_indices(list): Indices of arms chosen at each trial.
    """

    def __init__(self, arm_means):
        """
        Initialize the Thompson Sampling bandit.

        Args:
            arm_means (Sequence[float]): Real mean reward for each arm.

        Sets initial Beta priors and empties lists to track results.
        """
        self.arm_means = np.array(arm_means)
        self.num_arms = len(arm_means)
        self.posterior_a = np.ones(self.num_arms)
        self.posterior_b = np.ones(self.num_arms)
        self.collected_rewards = []
        self.chosen_arm_indices = []

    def __repr__(self):
        return f"ThompsonSampling(num_arms={self.num_arms})"

    def pull(self):
        """
        Select an arm by sampling from the current posterior of each arm.

        Returns:
            tuple: (selected arm index, simulated reward)
        """
        sampled_values = np.random.beta(self.posterior_a, self.posterior_b)
        selected = np.argmax(sampled_values)
        reward = np.random.normal(self.arm_means[selected], 1)
        return selected, reward

    def update(self, arm_index, reward):
        """
        Update the posterior of the selected arm based on the observed reward.

        Args:
            arm_index (int): Index of the arm pulled.
            reward (float): Observed reward from the arm.
        """
        if reward > 0:
            self.posterior_a[arm_index] += 1
        else:
            self.posterior_b[arm_index] += 1

    def experiment(self, trials=20000):
        """
        Run Thompson Sampling for a number of trials and record results.

        Args:
            trials (int): Number of trials to run.

        Returns:
            pd.DataFrame: Trial results including chosen arm, reward, regret, and algorithm.
        """
        logger.info("Starting Thompson Sampling simulation")

        for _ in range(trials):
            arm, reward = self.pull()
            self.update(arm, reward)
            self.chosen_arm_indices.append(arm)
            self.collected_rewards.append(reward)

        regret = np.max(self.arm_means) - np.array([self.arm_means[a] for a in self.chosen_arm_indices])
        results_df = pd.DataFrame({
            "Arm": self.chosen_arm_indices,
            "Reward": self.collected_rewards,
            "Regret": regret,
            "Algorithm": "Thompson Sampling"
        })
        
        logger.success("Thompson Sampling simulation complete.")
        return results_df

    def report(self):
        """
        Log mean reward and mean regret using loguru.
        """
        mean_reward = np.mean(self.collected_rewards)
        mean_regret = np.mean(np.max(self.arm_means) - np.array(self.collected_rewards))
        logger.info(f"[Thompson Sampling] Mean Reward: {mean_reward:.4f}")
        logger.info(f"[Thompson Sampling] Mean Regret: {mean_regret:.4f}")


# In[ ]:




