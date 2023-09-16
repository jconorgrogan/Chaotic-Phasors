import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class PhasorSystem:
    TWO_PI = 2 * np.pi
    
    def __init__(self, num_circles=4, phasors_per_circle=4, time_step=0.001, total_frames=900):
        self.num_circles = num_circles
        self.phasors_per_circle = phasors_per_circle
        self.time_step = time_step
        np.random.seed(0)
        
        # Increase the spread/randomness of angles and double the speed range
        self.angles = np.random.uniform(0, self.TWO_PI, (self.num_circles, self.phasors_per_circle))
        self.speeds = np.random.uniform(-40.0, 40.0, (self.num_circles, self.phasors_per_circle))
        
        self.circle_offsets = np.array([(np.cos(self.TWO_PI * n / self.num_circles) * 0.5, np.sin(self.TWO_PI * n / self.num_circles) * 0.5) for n in range(self.num_circles)])
        self.angular_momentum_log = np.zeros(total_frames)
        
        # Create an array to store the sum of phasors at each frame
        self.sum_of_phasors = np.zeros(total_frames, dtype=complex)

    def check_collision(self, circle_i, circle_j, index_i, index_j):
        phasor_size = 0.05
        x1, y1 = np.cos(self.angles[circle_i, index_i]) + self.circle_offsets[circle_i, 0], np.sin(self.angles[circle_i, index_i]) + self.circle_offsets[circle_i, 1]
        x2, y2 = np.cos(self.angles[circle_j, index_j]) + self.circle_offsets[circle_j, 0], np.sin(self.angles[circle_j, index_j]) + self.circle_offsets[circle_j, 1]
        distance = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return distance < 2 * phasor_size

    def resolve_collision(self, circle_i, circle_j, index_i, index_j):
        self.speeds[circle_i, index_i], self.speeds[circle_j, index_j] = self.speeds[circle_j, index_j], self.speeds[circle_i, index_i]

    def update(self, frame):
        self.angles += self.time_step * self.speeds
        self.angles %= self.TWO_PI
        
        collisions_to_resolve = []

        for i in range(self.num_circles):
            for j in range(i + 1, self.num_circles):
                for index_i in range(self.phasors_per_circle):
                    for index_j in range(self.phasors_per_circle):
                        if self.check_collision(i, j, index_i, index_j):
                            collisions_to_resolve.append((i, j, index_i, index_j))

        for i, j, index_i, index_j in collisions_to_resolve:
            self.resolve_collision(i, j, index_i, index_j)
        
        # Calculate the sum of all phasors and store it in the array
        self.sum_of_phasors[frame] = np.sum(np.exp(1j * self.angles))

def plot_system(frame, system, ax):
    ax.clear()
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_aspect('equal', 'box')
    system.update(frame)
    for n in range(system.num_circles):
        offset_x, offset_y = system.circle_offsets[n]
        x, y = np.cos(system.angles[n, :]) + offset_x, np.sin(system.angles[n, :]) + offset_y
        ax.scatter(x, y)
        for xi, yi in zip(x, y):
            circle = plt.Circle((xi, yi), 0.05, color='grey', fill=False)
            ax.add_artist(circle)
        ax.add_artist(plt.Circle((offset_x, offset_y), 1, color='grey', fill=False, linestyle='dotted'))

def plot_red_arrow(frame, system, ax):
    ax.clear()
    ax.set_xlim(-6, 6)  # Zoomed out right-hand side
    ax.set_ylim(-6, 6)  # Zoomed out right-hand side
    ax.set_aspect('equal', 'box')
    
    # Plot the real-time sum of phasors as a vector
    phasor_sum = system.sum_of_phasors[frame]
    sum_angle = np.angle(phasor_sum)
    sum_magnitude = np.abs(phasor_sum)
    
    # Leave a trail by plotting all previous positions of the red arrow
    for i in range(frame):
        phasor = system.sum_of_phasors[i]
        angle = np.angle(phasor)
        magnitude = np.abs(phasor)
        ax.quiver(0, 0, magnitude * np.cos(angle), magnitude * np.sin(angle), angles='xy', scale_units='xy', scale=1, color='black', alpha=0.2)
    
    # Plot the current position of the red arrow
    ax.quiver(0, 0, sum_magnitude * np.cos(sum_angle), sum_magnitude * np.sin(sum_angle), angles='xy', scale_units='xy', scale=1, color='red')

if __name__ == '__main__':
    total_frames = 900
    system = PhasorSystem(total_frames=total_frames)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))  # Create two side-by-side subplots
    ani1 = FuncAnimation(fig, plot_system, frames=range(total_frames), fargs=(system, ax1), interval=50)
    ani2 = FuncAnimation(fig, plot_red_arrow, frames=range(total_frames), fargs=(system, ax2), interval=50)
    
    plt.show()
