import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to generate fireworks
def create_fireworks(num_fireworks=10, num_frames=100):
    fig, ax = plt.subplots()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')  # Hide the axes

    # Initialize scatter points
    fireworks = [ax.scatter([], [], s=100, c='yellow') for _ in range(num_fireworks)]

    def init():
        for fw in fireworks:
            fw.set_offsets([])
        return fireworks

    def update(frame):
        for fw in fireworks:
            x = np.random.rand() * 10
            y = np.random.rand() * 10
            fw.set_offsets([x, y])
            fw.set_sizes(np.random.randint(50, 300, size=1))  # Vary the size of the fireworks
        return fireworks

    ani = animation.FuncAnimation(fig, update, frames=num_frames, init_func=init, blit=True, interval=100)
    return ani

# Streamlit UI
st.
