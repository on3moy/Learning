# Imports
from matplotlib import animation
import matplotlib.pyplot as plt 
import random
import seaborn as sns
import sys

def update(frame_number, rolls, faces, frequencies):
    """Configures bar plot contents for each animation frame"""
    
    # Roll die and update frequencies
    for i in range(rolls):
        frequencies[random.randrange(1,7)-1] += 1

    # Reconfigure plot for updated die frequencies
    plt.cla() # Clears old contents of previous axis
    axes = sns.barplot(faces, frequencies, palette='bright') # New barplot
    axes.set_title(f'Die Frequencies for {sum(frequencies):,} Rolls')
    axes.set(xlabel='Die Value', ylabel='Frequency')
    axes.set_ylim(top=max(frequencies) * 1.10) # 10 % buffer to show in graph

    # Display frequency & percentage above each patch (bar)
    for bar, frequency in zip(axes.patches, frequencies):
        text_x = bar.getx() + bar.get_width() / 2.0
        text_y = bar.get_height()
        text = f'{frequency:,}\n{frequency / sum(frequencies): .3%}'
        axes.text(text_x, text_y, text, ha='center', va='bottom')
    
# Read command-line arguments for number of frames and rolls per frame
number_of_frames = int(sys.argv[1])
rolls_per_frame = int(sys.argv[2])
print(number_of_frames,rolls_per_frame)

sns.set_style('whitegrid')
figure = plt.figure('Rooling a Six-Sided Die') # Figure for animation
values = list(range(1,7)) # Die faces
frequencies = [0] * 6 # 6 element list of die frequencies

# Configure and start animation that calls function update
die_animation = animation.FuncAnimation(figure, update, repeat=False, frames=number_of_frames, interval=33,
fargs=(rolls_per_frame, values, frequencies))

plt.show() # Displays window