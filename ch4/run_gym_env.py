#!/usr/bin/env python
# Handy script for exploring the available Gym environments | Praveen Palanisamy
# Chapter 4, Hands-on Intelligent Agents with OpenAI Gym, 2018

import gym
import sys
import time 

def run_gym_env(argv):
    env = gym.make(argv[1]) # Name of the environment supplied as 1st argument
    s = env.reset()
    print('initial state', s.shape, s)
    for _ in range(int(argv[2])): # Number of steps to be run supplied as 2nd argument
        env.render()
        env.step(env.action_space.sample())
        time.sleep(30/1000)
    env.close()
    
if __name__ == "__main__":
    run_gym_env(sys.argv)
