from agent import Agent
from snake_game import SnakeGame

def play():
    game = SnakeGame()
    agent = Agent()
    agent.load_model()  # Load trained model

    done = False
    score = 0
    game.reset()

    while not done:
        state = agent.get_state(game)
        final_move = agent.get_action(state)
        reward, done, score = game.play_step(final_move)

    print(f"Final Score: {score}")

if __name__ == "__main__":
    play()
