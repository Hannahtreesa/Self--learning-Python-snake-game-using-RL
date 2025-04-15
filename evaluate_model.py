import csv
from agent import Agent
from snake_game import SnakeGame

def evaluate_model(num_games=100, csv_file="model_eval_data.csv"):
    agent = Agent()
    agent.load_model()  # This should load your model.pth
    game = SnakeGame()

    with open(csv_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Game", "Score"])  # CSV Header

        for i in range(1, num_games + 1):
            game.reset()
            done = False
            score = 0

            while not done:
                state = agent.get_state(game)
                final_move = agent.get_action(state)
                reward, done, score = game.play_step(final_move)

            print(f"Game {i} Score: {score}")
            writer.writerow([i, score])  # Save to CSV

    print(f"✅ Evaluation complete. Data saved to {csv_file}")

if __name__ == "__main__":
    evaluate_model()
