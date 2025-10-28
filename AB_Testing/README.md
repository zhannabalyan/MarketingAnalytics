# Multi-Armed Bandit A/B Testing Simulation

This project implements two algorithms, Epsilon-Greedy and Thompson Sampling, to simulate a multi-armed bandit problem in an A/B testing context. The objective is to analyze how each algorithm balances exploration and exploitation while identifying the option that yields the highest reward.

Both algorithms learn from experience across multiple trials and adjust their selection strategies over time, similar to how online systems optimize choices between competing advertisements or product recommendations.

# Project Structure

The project consists of the following files:
- Bandit.py:Contains the base class that defines the shared interface for all bandit algorithms.
- EpsilonGreedy.py:Implements the Epsilon-Greedy algorithm, using a decaying exploration rate (epsilon = 1/t).
- ThompsonSampling.py:Implements the Thompson Sampling algorithm based on Bayesian updating with Beta distributions.
- run_experiments.py:The main file that runs both algorithms, records their results, and logs performance metrics.
- plots.py:Implements the visualizations.
- outputs.csv:Output file storing experiment results.
- requirements.txt:Dependencies (e.g., loguru).


# How to Run

- Launch experiment.ipynb using Jupyter Notebook or VSCode with the Jupyter plugin.

- Execute all cells to run experiments for both algorithms.

- Create visualizations of rewards and regret over time.

- Export the output data to results.csv.



- When executed, the script will simulate a series of trials for both algorithms, calculate rewards and regrets, and log the outcomes. The log messages will display information such as average reward and regret for each method. Example output is shown below:

2025-10-28 13:20:49 | INFO | [Epsilon-Greedy] Average Reward: 4.0062
2025-10-28 13:20:49 | INFO | [Epsilon-Greedy] Average Regret: -0.0062
2025-10-28 13:20:49 | INFO | [Thompson Sampling] Average Reward: 3.9727
2025-10-28 13:20:49 | INFO | [Thompson Sampling] Average Regret: 0.0273

# Algorithm Overview

The Epsilon-Greedy algorithm begins by exploring randomly with a high probability and gradually decreases exploration using an inverse relationship with time (epsilon = 1/t). As trials progress, the algorithm favors exploitation, repeatedly selecting the arm that has shown the best estimated performance.

The Thompson Sampling algorithm takes a probabilistic approach. It assumes a Beta prior for each arm and samples from the posterior distributions to decide which arm to pull. The parameters of the Beta distributions are updated after each trial depending on whether the observed reward was positive or negative. This method naturally balances exploration and exploitation without relying on an explicit decay schedule.

# Results

After running the experiment, the log output provides the average reward and regret for both algorithms. Typically, Thompson Sampling achieves lower average regret and converges faster toward the optimal arm, while Epsilon-Greedy performs adequately but requires more trials to stabilize.

