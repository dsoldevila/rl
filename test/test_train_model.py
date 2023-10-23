import pytest
from os import path

import gymnasium as gym

from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.monitor import Monitor


# Virtual display
from pyvirtualdisplay import Display


@pytest.fixture
def model_name():
    return path.join("output", "ppo-LunarLander-v2")

def test_train_model(model_name):
    env = make_vec_env('LunarLander-v2', n_envs=16)

    model = PPO(
        policy = 'MlpPolicy',
        env = env,
        n_steps = 1024,
        batch_size = 64,
        n_epochs = 4,
        gamma = 0.999,
        gae_lambda = 0.98,
        ent_coef = 0.01,
        verbose=1)
    
    # Train it for 1,000,000 timesteps
    model.learn(total_timesteps=1000000)
    
    # Save the model
    model.save(model_name)

def test_evaluate_model_multiple(model_name):

    eval_env = Monitor(gym.make("LunarLander-v2"))
    model = PPO.load(model_name)

    mean_reward, std_reward = evaluate_policy(model, eval_env, n_eval_episodes=10, deterministic=True)
    print(f"mean_reward={mean_reward:.2f} +/- {std_reward}")


def test_evaluate_model_single(model_name):

    eval_env = Monitor(gym.make("LunarLander-v2", render_mode="human"))
    model = PPO.load(model_name)

    mean_reward, std_reward = evaluate_policy(model, eval_env, n_eval_episodes=1, deterministic=True, render=True)
    print(f"mean_reward={mean_reward:.2f} +/- {std_reward}")