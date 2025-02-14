import streamlit as st
import os

def main():
    # Page Configuration
    st.set_page_config(
        page_title="Snake AI Portfolio",
        layout="centered",
        page_icon="🐍"
    )

    # Title of the Page
    st.title("Snake AI Portfolio 🐍")
    st.markdown("""
    Welcome to my **Snake AI Project**! This project demonstrates how Deep Q-Learning can be used to train an AI agent 
    to play the classic Snake game. The AI learns through experience, developing strategies to maximize its score while avoiding collisions.
    """)

     # GitHub Link
    st.markdown("""
    **View full code on GitHub:**  
    [![GitHub](https://img.shields.io/badge/GitHub-Repo-blue?style=for-the-badge&logo=github)](https://github.com/JoelNgiamKeeYong/snake-game-ai-rl)
    """)

    # Section 1: Video Showcase
    st.header("🎮 Snake AI Gameplay Showcase")
    video_path = "./training-example.mp4"  # Path to your MP4 video file

    # Check if the video file exists
    if os.path.exists(video_path):
        st.subheader("Watch the AI in Action!")
        st.video(video_path)
    else:
        st.error("Video file not found. Please ensure the file exists at the specified path.")

    # Section 2: Project Overview
    st.header("📚 Project Overview")
    st.markdown("""
    This project combines **Reinforcement Learning**, **Deep Learning**, and **Game Development** to create an intelligent Snake AI. 
    Below are the key aspects of the project:
    - **Technologies Used**: Python, PyTorch, Pygame, Streamlit
    - **Learning Algorithm**: Deep Q-Learning (DQN)
    - **State Representation**: Encoded as 11 binary values (details below)
    - **Reward System**: Positive rewards for eating food, negative rewards for collisions
    - **Training Process**: Experience replay and epsilon-greedy exploration
    """)

    # Section 3: Technical Implementation
    st.header("🛠️ Technical Implementation")

    # Neural Network Architecture
    st.subheader("Neural Network Architecture")
    st.markdown("""
    The neural network consists of three layers:
    - **Input Layer**: 11 neurons representing the game state
    - **Hidden Layer**: 256 neurons with ReLU activation
    - **Output Layer**: 3 neurons representing possible actions (left, straight, right)
    """)
    with st.expander("View Neural Network Code"):
        st.code("""
class Linear_QNet(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        self.linear1 = nn.Linear(input_size, hidden_size)
        self.linear2 = nn.Linear(hidden_size, output_size)
        
    def forward(self, x):
        x = F.relu(self.linear1(x))
        x = self.linear2(x)
        return x
        """)

    # State Representation
    st.subheader("State Representation")
    st.markdown("""
    The game state is encoded as 11 binary values:
    1. Danger straight ahead
    2. Danger to the right
    3. Danger to the left
    4. Current direction (4 values: up, down, left, right)
    5. Food location relative to the snake's head (4 values: up, down, left, right)
    """)
    with st.expander("Why These Features?"):
        st.markdown("""
        These features provide a concise representation of the game environment, allowing the AI to make informed decisions. 
        By encoding danger, direction, and food location, the model can effectively learn optimal policies for gameplay.
        """)

    # Training Process
    st.subheader("Training Process")
    st.markdown("""
    The training process involves the following steps:
    - **Exploration vs Exploitation**: Controlled by epsilon-greedy strategy
    - **Experience Replay**: Stores past experiences to stabilize learning
    - **Reward System**: 
      - +10 for eating food
      - -10 for collisions
      - Small negative reward for each step to encourage efficiency
    - **Model Saving**: Best-performing models are saved during training
    """)

    # Section 4: Future Work
    st.header("🚀 Future Work")
    st.markdown("""
    While this project demonstrates the potential of Deep Q-Learning, there are several areas for improvement:
    - **Hyperparameter Tuning**: Experiment with learning rates, batch sizes, and discount factors
    - **Advanced Architectures**: Explore convolutional or recurrent neural networks for better performance
    - **Multi-Agent Training**: Extend the project to include multiple snakes competing or cooperating
    - **Deployment**: Host the trained model on a web platform for interactive demos
    """)

if __name__ == "__main__":
    main()