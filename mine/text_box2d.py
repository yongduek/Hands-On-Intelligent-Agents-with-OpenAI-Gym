# pip install gym[all]  installs everything.

import time 
import gym
# env = gym.make('BipedalWalker-v3')
# env=gym.make('LunarLander-v2')
# env = gym.make('CarRacing-v0')
env = gym.make('Assault-v0')

env.reset()
for i in range(1000):
    env.render()
    s, r, done, info = env.step(env.action_space.sample())
    time.sleep(30/1000.)
    # print(i, s, r, done, info)
    # if done:
    #     pass 

print('Finished.')