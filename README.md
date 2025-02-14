# 🎮 Snake AI: Reinforcement Learning in Action

## 🚀 Business Scenario (or Project Context)

Reinforcement Learning (RL) is a powerful technique for training intelligent agents to make decisions in dynamic environments. This project demonstrates how Deep Q-Learning (DQN) can be applied to teach an AI agent to play the classic Snake game. The trained AI learns optimal strategies to maximize its score while avoiding collisions. This project is valuable for:

- **AI Enthusiasts:** Understanding the fundamentals of reinforcement learning
- **Game Developers:** Exploring AI-driven gameplay mechanics
- **Researchers:** Experimenting with RL algorithms in controlled environments
- **Educators:** Demonstrating practical applications of machine learning

---

## 🧠 Problem Statement

Teaching an AI agent to play Snake involves solving several challenges:

- **Decision-Making:** How does the agent decide the next move (left, right, or straight)?
- **Exploration vs Exploitation:** Balancing between trying new actions and leveraging learned strategies
- **Reward Design:** Creating a reward system that encourages efficient gameplay
- **Generalization:** Ensuring the agent performs well across different scenarios

This project addresses these challenges by implementing a Deep Q-Learning model to train the AI agent.

---

## 🛠️ Solution Approach

The project uses Deep Q-Learning (DQN) combined with Pygame to simulate and train the Snake AI. The workflow includes:

### 1️⃣ **Environment Setup**

- **Game Environment:** Developed using Pygame to simulate the Snake game
- **State Representation:** Encoded as 11 binary values:
  - Danger ahead, danger to the right, danger to the left
  - Current direction (up, down, left, right)
  - Food location relative to the snake's head (up, down, left, right)
- **Reward System:**
  - +10 for eating food
  - -10 for collisions
  - Small negative reward for each step to encourage efficiency

### 2️⃣ **Model Development**

- **Neural Network Architecture:**
  - Input Layer: 11 neurons (state representation)
  - Hidden Layer: 256 neurons with ReLU activation
  - Output Layer: 3 neurons (possible actions: left, straight, right)
- **Training Process:**
  - **Exploration vs Exploitation:** Controlled by epsilon-greedy strategy
  - **Experience Replay:** Stores past experiences to stabilize learning
  - **Model Saving:** Best-performing models are saved during training
- **Optimization:** Used PyTorch's Adam optimizer with a learning rate of 0.001

### 3️⃣ **Interactive Dashboard Development**

- **Streamlit App:** Created an interactive dashboard to showcase the AI gameplay and provide technical insights
- **Features:**
  - Watch the AI play Snake in real-time
  - Explore the neural network architecture and state representation
  - View training progress and future work ideas
- **Video Showcase:** Embedded gameplay video for quick reference

---

## 📊 Key Insights

| Insight                            | Description                                                                     |
| ---------------------------------- | ------------------------------------------------------------------------------- |
| **State Representation Matters**   | Encoding danger, direction, and food location enables effective decision-making |
| **Reward Design Impacts Learning** | A well-designed reward system accelerates the agent's learning process          |
| **Epsilon-Greedy Strategy Works**  | Balances exploration and exploitation effectively                               |
| **Deep Q-Learning Scales Well**    | Handles complex state-action spaces efficiently                                 |

---

### 🔖 Additional Observations

- The AI learns to navigate towards food while avoiding walls and its own body.
- Training progress improves over time, with higher scores achieved as the agent gains experience.
- The trained model demonstrates generalization by performing well in unseen scenarios.

---

## ⚠️ Limitations

1️⃣ **Training Time:** Requires significant computational resources and time for convergence  
2️⃣ **Simplified Environment:** The Snake game is a controlled environment, limiting real-world applicability  
3️⃣ **Hyperparameter Sensitivity:** Performance depends heavily on tuning hyperparameters like learning rate and batch size

---

## 🔄 Key Skills Demonstrated

🔹 **Reinforcement Learning Implementation**  
🔹 **Deep Q-Learning (DQN)**  
🔹 **Pygame Game Development**  
🔹 **Neural Network Design and Training**  
🔹 **Interactive Dashboard Development**  
🔹 **Data Visualization**  
🔹 **Python Programming**

---

## 🛠️ Technical Tools & Libraries

- **Python:** Core programming language
- **PyTorch:** Neural network implementation and training
- **Pygame:** Game environment simulation
- **Streamlit:** Web app framework for interactive dashboards
- **NumPy:** Numerical computations
- **Plotly/Matplotlib:** Data visualization

---

## 🚀 Final Thoughts

This project demonstrates the power of reinforcement learning in teaching AI agents to perform complex tasks. By combining Deep Q-Learning with Pygame, we’ve created an intelligent Snake AI that learns to play the game through trial and error. The interactive dashboard provides a platform to explore the AI's behavior and understand the underlying technology. Future work could include experimenting with advanced architectures (e.g., convolutional or recurrent networks) and extending the project to multi-agent scenarios.
