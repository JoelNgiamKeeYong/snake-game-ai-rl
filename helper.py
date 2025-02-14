import matplotlib.pyplot as plt
from IPython import display

plt.ion()

# Create single compact figure
fig = plt.figure(figsize=(8, 5))
ax = plt.gca()

def plot(scores, mean_scores):
    display.clear_output(wait=True)
    ax.clear()
    
    # Plot scores and mean
    ax.plot(scores, label='Score', color='skyblue')
    ax.plot(mean_scores, label='Average', color='red')
    
    # Add current stats as text
    ax.text(len(scores)-1, scores[-1], str(scores[-1]))
    ax.text(len(mean_scores)-1, mean_scores[-1], str(round(mean_scores[-1], 2)))
    
    # Configure plot
    ax.set_title('Training...')
    ax.set_xlabel('Games')
    ax.set_ylabel('Score')
    ax.set_ylim(ymin=0)
    ax.legend(loc='upper left')
    ax.grid(True, alpha=0.2)
    
    plt.tight_layout()
    display.display(fig)
    plt.pause(0.1)