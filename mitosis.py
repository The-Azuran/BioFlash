import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation

# Function to animate mitosis
def animate_mitosis():
    fig, ax = plt.subplots(figsize=(4, 4))

    # Initial state (Interphase)
    nucleus = plt.Circle((0.5, 0.5), 0.4, color='blue')
    ax.add_artist(nucleus)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    # Chromosome line
    chromosome, = ax.plot([], [], color='red')
    
    # Metaphase plate line
    metaphase_plate = ax.axhline(y=0, color='green', alpha=0) 

    # Function to initialize the animation
    def init():
        chromosome.set_data([], [])
        return chromosome,

    # Function to update each frame
    def update(frame):
        # Prophase
        if frame < 20:
            x = [0.5, 0.5]
            y = [0.4 + frame * 0.01, 0.6 - frame * 0.01]
        # Metaphase
        elif frame < 40:
            x = [0.5, 0.5]
            y = [0.4, 0.6]
            metaphase_plate.set_ydata(0.5)
        # Anaphase
        elif frame < 60:
            x = [0.5 - (frame - 40) * 0.01, 0.5 + (frame - 40) * 0.01]
            y = [0.4, 0.6]
        # Telophase
        else:
            x = [0.3, 0.7]
            y = [0.4, 0.6]
            nucleus.radius = 0.3
            nucleus.center = (0.3, 0.5)
            ax.add_artist(plt.Circle((0.7, 0.5), 0.3, color='blue', alpha=0.5))

        chromosome.set_data(x, y)
        return chromosome,

    # Create the animation
    ani = FuncAnimation(fig, update, frames=80, init_func=init, blit=True, interval=100)

    plt.show()

# Animate mitosis
animate_mitosis()
