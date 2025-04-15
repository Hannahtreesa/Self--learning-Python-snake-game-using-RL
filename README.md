# Self--learning-Python-snake-game-using-RL
A self- learning python game using Reinforcement learning.

This project is a reinforcement learning agent that learns to play the classic Snake game using Deep Q-Learning (DQN). 
The agent is trained using PyTorch and plays the game using a simple feedforward neural network.

- `train.py` - Trains the snake AI using DQN.
- `play.py` - Lets the trained model play the game.
- `agent.py` - The brain of the snake: implements DQN logic.
- `model.py` - Defines the neural network architecture.
- `snake_game.py` - The Snake game built using Pygame.

The agent uses Deep Q-Learning (DQN):
- State: Represents the game’s current status (e.g. danger, direction, food location).
 Action: [straight, right, left]
- Reward: +10 for eating food, -10 for dying, 0 for each step.
- Model: A neural network learns the Q-values (best actions for each state).

  
