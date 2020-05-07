"""
module defines the component classes for point_robot_goal_env
# state_sampler - UniformSampler
# reward_func - PointRobotReward
# observation_func
# goal sampler - UniformSampler

"""

import roam_env.robot_env.components as env_components
from collections import OrderedDict


class ObservationFunc(env_components.ObservationFunc):

    def get_obs(self, obs):
        env_obs = OrderedDict()
        env_obs['achieved_goal'] = obs['state'][0, 0]
        return env_obs
