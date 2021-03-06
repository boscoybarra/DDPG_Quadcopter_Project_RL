import numpy as np
from physics_sim import PhysicsSim
import math

class TakeOff_Task():
    """TakeOff (environment) that defines the goal and provides feedback to the agent."""
    def __init__(self, init_pose=None, init_velocities=None, 
        init_angle_velocities=None, runtime=5., target_pos=None):
        """Initialize a Task object.
        Params
        ======
            init_pose: initial position of the quadcopter in (x,y,z) dimensions and the Euler angles
            init_velocities: initial velocity of the quadcopter in (x,y,z) dimensions
            init_angle_velocities: initial radians/second for each of the three Euler angles
            runtime: time limit for each episode
            target_pos: target/goal (x,y,z) position for the agent
        """
        # Simulation
        self.sim = PhysicsSim(init_pose, init_velocities, init_angle_velocities, runtime) 
        self.action_repeat = 3

        self.state_size = self.action_repeat * 6
        self.action_size = 4
        self.action_low = 0
        self.action_high = 900
        

        # Goal: Takeoff the Quadcopter starting from land
        self.target_pos = target_pos if target_pos is not None else np.array([0., 0., 10.]) 

    def get_reward(self):
        """Uses current pose of sim to return reward."""

        # Keep the Euler angles stable plotting them in a sin funtion
        # Multiply each angle and store, we want them to be between -1 and 1.

        optimal_reward = (1. - abs(math.sin(self.sim.pose[3])))
        optimal_reward *= (1. - abs(math.sin(self.sim.pose[4])))
        optimal_reward *= (1. - abs(math.sin(self.sim.pose[5])))

        # How long we are
        delta = abs(self.sim.pose[:3] - self.target_pos[:3])
        
        # Make sure we get positive numbers, dot product in order to apply the square root.
        distance = math.sqrt(np.dot(delta, delta))
        
        if(distance > 0.01): 
            penalty = distance
        else: penalty = 0
        reward = 1. - penalty
        # Take into account Euler angles
        reward *= optimal_reward
        return reward

    def step(self, rotor_speeds):
        """Uses action to obtain next state, reward, done."""
        reward = 0
        pose_all = []
        for _ in range(self.action_repeat):
            done = self.sim.next_timestep(rotor_speeds) # update the sim pose and velocities
            reward += self.get_reward() 
            pose_all.append(self.sim.pose)
        next_state = np.concatenate(pose_all)
        return next_state, reward, done

    def reset(self):
        """Reset the sim to start a new episode."""
        self.sim.reset()
        state = np.concatenate([self.sim.pose] * self.action_repeat) 
        return state

        

class Land_Task():
    """Land_Task (environment) that defines the goal and provides feedback to the agent."""
    def __init__(self, init_pose=None, init_velocities=None, 
        init_angle_velocities=None, runtime=5., target_pos=None):
        """Initialize a Task object.
        Params
        ======
            init_pose: initial position of the quadcopter in (x,y,z) dimensions and the Euler angles
            init_velocities: initial velocity of the quadcopter in (x,y,z) dimensions
            init_angle_velocities: initial radians/second for each of the three Euler angles
            runtime: time limit for each episode
            target_pos: target/goal (x,y,z) position for the agent
        """
        # Simulation
        self.sim = PhysicsSim(init_pose, init_velocities, init_angle_velocities, runtime) 
        self.action_repeat = 3

        self.state_size = self.action_repeat * 6
        self.action_size = 4
        self.action_low = 0
        self.action_high = 900
        

        # Goal: Land the Quadcopter starting from the sky
        self.target_pos = target_pos if target_pos is not None else np.array([0., 0., 0.]) 

    def get_reward(self):
        """Uses current pose of sim to return reward."""

        # Keep the Euler angles stable plotting them in a sin funtion
        # Multiply each angle and store, we want them to be between -1 and 1.
        optimal_reward = (1. - abs(math.sin(self.sim.pose[3])))
        optimal_reward *= (1. - abs(math.sin(self.sim.pose[4])))
        optimal_reward *= (1. - abs(math.sin(self.sim.pose[5])))

        # How long we are
        delta = abs(self.sim.pose[:3] - self.target_pos[:3])
        
        # Make sure we get positive numbers, dot product in order to apply the square root.
        distance = math.sqrt(np.dot(delta, delta))
        
        if(distance > 0.01): 
            penalty = distance
        else: penalty = 0
        reward = 1. - penalty
        # Take into account Euler angles
        reward *= optimal_reward
        return reward

    def step(self, rotor_speeds):
        """Uses action to obtain next state, reward, done."""
        reward = 0
        pose_all = []
        for _ in range(self.action_repeat):
            done = self.sim.next_timestep(rotor_speeds) # update the sim pose and velocities
            reward += self.get_reward() 
            pose_all.append(self.sim.pose)
        next_state = np.concatenate(pose_all)
        return next_state, reward, done

    def reset(self):
        """Reset the sim to start a new episode."""
        self.sim.reset()
        state = np.concatenate([self.sim.pose] * self.action_repeat) 
        return state


class Task():
    """Task (environment) for testing in notebook that defines the goal and provides feedback to the agent."""
    def __init__(self, init_pose=None, init_velocities=None, 
        init_angle_velocities=None, runtime=5., target_pos=None):
        """Initialize a Task object.
        Params
        ======
            init_pose: initial position of the quadcopter in (x,y,z) dimensions and the Euler angles
            init_velocities: initial velocity of the quadcopter in (x,y,z) dimensions
            init_angle_velocities: initial radians/second for each of the three Euler angles
            runtime: time limit for each episode
            target_pos: target/goal (x,y,z) position for the agent
        """
        # Simulation
        self.sim = PhysicsSim(init_pose, init_velocities, init_angle_velocities, runtime) 
        self.action_repeat = 3

        self.state_size = self.action_repeat * 6
        self.action_size = 4
        self.action_low = 0
        self.action_high = 900
        

        # Goal: Takeoff the Quadcopter starting from land
        self.target_pos = target_pos if target_pos is not None else np.array([0., 0., 10.]) 

    def get_reward(self):
        """Uses current pose of sim to return reward."""

        reward = 1.-.3*(abs(self.sim.pose[:3] - self.target_pos)).sum()
        return reward


    def step(self, rotor_speeds):
        """Uses action to obtain next state, reward, done."""
        reward = 0
        pose_all = []
        for _ in range(self.action_repeat):
            done = self.sim.next_timestep(rotor_speeds) # update the sim pose and velocities
            reward += self.get_reward() 
            pose_all.append(self.sim.pose)
        next_state = np.concatenate(pose_all)
        return next_state, reward, done

    def reset(self):
        """Reset the sim to start a new episode."""
        self.sim.reset()
        state = np.concatenate([self.sim.pose] * self.action_repeat) 
        return state

