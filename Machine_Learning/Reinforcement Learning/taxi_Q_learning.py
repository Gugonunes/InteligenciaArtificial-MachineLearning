# Important: this code has to run in the python shell, so execute it as: python taxi_Q_learning.py
# Don't use the "run button" in vscode

import gym
import random
import numpy as np
from time import sleep

env = gym.make('Taxi-v3').env
env.reset()
env.render()

print(env.action_space)
# 0 = south, 1 = north, 2 = east, 3 = west, 4 = pickup, 5 = dropoff

print(env.observation_space)

print(len(env.P))

print(env.P[484])

# Training

q_table = np.zeros([env.observation_space.n, env.action_space.n])

from IPython.display import clear_output

alpha = 0.1
gamma = 0.6
epsilon = 0.1

for i in range(100000):
    state = env.reset()

    penalty, reward = 0, 0
    done = False
    while not done:
        #exploration
        if random.uniform(0,1) < epsilon:
            action = env.action_space.sample()
        #exploitation
        else:
            action = np.argmax(q_table[state])

        next_state, reward, done, info = env.step(action)

        q_previous = q_table[state, action]
        next_max_value = np.max(q_table[next_state])

        q_new = (1 - alpha) * q_previous + alpha * (reward + gamma * next_max_value)
        q_table[state, action] = q_new
        if reward == -10:
            penalty +=1

        state = next_state

    if i % 100 == 0:
        clear_output(wait=True)
        print('Episode: ', i)

print('Finished training')

total_penalty = 0
episodes = 50
frames = []
for _ in range(episodes):
    state = env.reset()
    penalty, reward = 0, 0
    done = False
    while not done:
        action = np.argmax(q_table[state])
        state, reward, done, info = env.step(action)

        if reward == -10:
            penalty += 1

        frames.append({
            'frame': env.render(mode='ansi'),
            'state': state,
            'action': action,
            'reward': reward
        })
    total_penalty += penalty

print('Episodes', episodes)
print('Penaltys', total_penalty)

for frame in frames:
    clear_output(wait=True)
    print(frame['frame'])
    print('State', frame['state'])
    print('Action', frame['action'])
    print('Reward', frame['reward'])
    sleep(.3)
