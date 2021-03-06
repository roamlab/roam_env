"""
module defines the component classes for point_robot_env
    state_sampler - UniformSampler
    reward_func - PointRobotReward
    observation_func - PointRobotObservationFunc
    
"""

import roam_env.robot_env.components as env_components

class RewardFunc(env_components.RewardFunc):
    """ make the point robot go to -1.0 on the x-axis """

    def __call__(self, obs, action):
        x = obs['state'][0, 0]
        reward = -(x-1.0)**2
        return reward


class ObservationFunc(env_components.ObservationFunc):

    def get_obs(self, obs):
        return obs