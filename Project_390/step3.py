import matplotlib.pyplot as plt
import pandas as pd
import h5py

with h5py.File('HDF5/data.h5', 'r') as hdf:
    comb_data = hdf['combined_data/combined_raw_data'][()]
    walk_comb_data = hdf['combined_data/combined_walk_data'][()]
    jump_comb_data = hdf['combined_data/combined_jump_data'][()]

# Create a DataFrame from the NumPy array
comb_df = pd.DataFrame(comb_data, columns=['Time (s)', 'Linear Acceleration x (m/s^2)', 'Linear Acceleration y (m/s^2)',
                                         'Linear Acceleration z (m/s^2)', 'Absolute acceleration (m/s^2)', 'label'])

walk_df = pd.DataFrame(walk_comb_data, columns=['Time (s)', 'Linear Acceleration x (m/s^2)', 'Linear Acceleration y (m/s^2)',
                                              'Linear Acceleration z (m/s^2)', 'Absolute acceleration (m/s^2)', 'label'])

jump_df = pd.DataFrame(jump_comb_data, columns=['Time (s)', 'Linear Acceleration x (m/s^2)', 'Linear Acceleration y (m/s^2)',
                                              'Linear Acceleration z (m/s^2)', 'Absolute acceleration (m/s^2)', 'label'])


#_______________________________________________________________________________________________________________________
# Create a figure with a grid of subplots
fig, axs = plt.subplots(3, 3, figsize=(15, 10))

# Graph 1: Acceleration vs Time in x direction for combined (walking/jumping) data
x_acc = comb_df['Linear Acceleration x (m/s^2)']
time = comb_df['Time (s)']
axs[0, 0].plot(time, x_acc)
axs[0, 0].set_title('Combined - Linear Acceleration (x) vs Time')
axs[0, 0].set_ylabel('Linear Acceleration x (m/s^2)')
axs[0, 0].set_xlabel('Time (s)')

# Graph 2: Acceleration vs Time in x direction for walking data
x_acc = walk_df['Linear Acceleration x (m/s^2)']
time = walk_df['Time (s)']
axs[0, 1].plot(time, x_acc)
axs[0, 1].set_title('Walking - Linear Acceleration (x) vs Time')
axs[0, 1].set_ylabel('Linear Acceleration x (m/s^2)')
axs[0, 1].set_xlabel('Time (s)')

# Graph 3: Acceleration vs Time in x direction for jumping data
x_acc = jump_df['Linear Acceleration x (m/s^2)']
time = jump_df['Time (s)']
axs[0, 2].plot(time, x_acc)
axs[0, 2].set_title('Jumping - Linear Acceleration (x) vs Time')
axs[0, 2].set_ylabel('Linear Acceleration x (m/s^2)')
axs[0, 2].set_xlabel('Time (s)')

# Graph 4: Acceleration vs Time in y direction for combined (walking/jumping) data
y_acc = comb_df['Linear Acceleration y (m/s^2)']
time = comb_df['Time (s)']
axs[1, 0].plot(time, y_acc)
axs[1, 0].set_title('Combined - Linear Acceleration (y) vs Time')
axs[1, 0].set_ylabel('Linear Acceleration y (m/s^2)')
axs[1, 0].set_xlabel('Time (s)')

# Graph 5: Acceleration vs Time in y direction for walking data
y_acc = walk_df['Linear Acceleration y (m/s^2)']
time = walk_df['Time (s)']
axs[1, 1].plot(time, y_acc)
axs[1, 1].set_title('Walking - Linear Acceleration (y) vs Time')
axs[1, 1].set_ylabel('Linear Acceleration y (m/s^2)')
axs[1, 1].set_xlabel('Time (s)')

# Graph 6: Acceleration vs Time in y direction for jumping data
y_acc = jump_df['Linear Acceleration y (m/s^2)']
time = jump_df['Time (s)']
axs[1, 2].plot(time, y_acc)
axs[1, 2].set_title('Jumping - Linear Acceleration (y) vs Time')
axs[1, 2].set_ylabel('Linear Acceleration y (m/s^2)')
axs[1, 2].set_xlabel('Time (s)')

# Graph 7: Acceleration vs Time in z direction for combined (walking/jumping) data
z_acc = comb_df['Linear Acceleration z (m/s^2)']
time = comb_df['Time (s)']
axs[2, 0].plot(time, z_acc)
axs[2, 0].set_title('Combined - Linear Acceleration (z) vs Time')
axs[2, 0].set_ylabel('Linear Acceleration z (m/s^2)')
axs[2, 0].set_xlabel('Time (s)')

# Graph 8: Acceleration vs Time in z direction for walking data
z_acc = walk_df['Linear Acceleration z (m/s^2)']
time = walk_df['Time (s)']
axs[2, 1].plot(time, z_acc)
axs[2, 1].set_title('Walking - Linear Acceleration (z) vs Time')
axs[2, 1].set_ylabel('Linear Acceleration z (m/s^2)')
axs[2, 1].set_xlabel('Time (s)')

# Graph 9: Acceleration vs Time in z direction for jumping data
z_acc = jump_df['Linear Acceleration z (m/s^2)']
time = jump_df['Time (s)']
axs[2, 2].plot(time, z_acc)
axs[2, 2].set_title('Jumping - Linear Acceleration (z) vs Time')
axs[2, 2].set_ylabel('Linear Acceleration z (m/s^2)')
axs[2, 2].set_xlabel('Time (s)')

# Adjust spacing between subplots
plt.subplots_adjust(wspace=0.3, hspace=0.3)

# Show the plot
plt.show()


#_______________________________________________________________________________________________________________________
# Create a figure with a grid of subplots
fig, axs = plt.subplots(1, 3, figsize=(15, 10))

# Graph 10: Absolute Acceleration vs Time for combined (walking/jumping) data
a_acc = comb_df['Absolute acceleration (m/s^2)']
time = comb_df['Time (s)']
axs[0].plot(time, a_acc)
axs[0].set_title('Combined - Absolute Acceleration vs Time')
axs[0].set_ylabel('Absolute acceleration (m/s^2)')
axs[0].set_xlabel('Time (s)')


# Graph 11: Absolute Acceleration vs Time for walking data
a_acc = walk_df['Absolute acceleration (m/s^2)']
time = walk_df['Time (s)']
axs[1].plot(time, a_acc)
axs[1].set_title('Walking - Absolute Acceleration vs Time')
axs[1].set_ylabel('Absolute acceleration (m/s^2)')
axs[1].set_xlabel('Time (s)')

# Graph 12: Absolute Acceleration vs Time for jumping data
a_acc = jump_df['Absolute acceleration (m/s^2)']
time = jump_df['Time (s)']
axs[2].plot(time, a_acc)
axs[2].set_title('Jumping - Absolute Acceleration vs Time')
axs[2].set_ylabel('Absolute acceleration (m/s^2)')
axs[2].set_xlabel('Time (s)')

# Adjust spacing between subplots
plt.subplots_adjust(wspace=0.3, hspace=0.3)

# Show the plot
plt.show()

#_______________________________________________________________________________________________________________________
# Graph 13: Comparison of Walking vs jumping plots for Acceleration

x_time = walk_df['Time (s)']
y_walk = walk_df['Linear Acceleration x (m/s^2)']
y_jump = jump_df['Linear Acceleration y (m/s^2)']

fig, ax = plt.subplots()
ax.plot(x_time, y_jump, label='Jumping Data')
ax.plot(x_time, y_walk, label='Walking Data')
ax.legend()
plt.title('Comparison of Walking and Jumping Acceleration vs Time')
plt.xlabel('Linear Acceleration (x-Walk & y-Jump) [m/s^2]')
plt.ylabel('Time (s)')
plt.show()




