from agent import Agent
from snake_game import SnakeGame
import matplotlib.pyplot as plt
import os
import torch

def train():
    record = 0
    n_games = 0 
    agent = Agent()
    game = SnakeGame()

    # ✅ Load previous model if available
    model_path = "model.pth"
    if os.path.exists(model_path):
        print("🔄 Loading saved model...")
        agent.model.load_state_dict(torch.load(model_path))
        agent.model.eval()  # evaluation mode
        print("✅ Model loaded successfully.")

    while True:
        state_old = agent.get_state(game)
        final_move = agent.get_action(state_old)
        reward, done, score = game.play_step(final_move)
        state_new = agent.get_state(game)

        agent.train_short_memory(state_old, final_move, reward, state_new, done)
        agent.remember(state_old, final_move, reward, state_new, done)

        if done:
            game.reset()
            n_games += 1
            agent.train_long_memory()

            if score > record:
                record = score
                agent.model.save()

            print(f'Game {n_games} Score {score} Record: {record}')

if __name__ == '__main__':
    train()
