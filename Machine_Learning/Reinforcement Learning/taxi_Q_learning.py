import gym
import random

env = gym.make('Taxi-v3').env
env.reset()
env.render()

print(env.action_space)
# 0 = south, 1 = north, 2 = east, 3 = west, 4 = pickup, 5 = dropoff

print(env.observation_space)

len(env.P)

env.P[484]

# Training
