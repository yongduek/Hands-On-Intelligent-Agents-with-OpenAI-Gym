import gym

env = gym.make("MountainCar-v0")
env.reset()
for _ in range(200):
    env.render()
    r = env.step(env.action_space.sample())  # random action
    print(r)