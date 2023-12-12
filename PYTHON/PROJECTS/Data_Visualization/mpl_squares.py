#!./env/bin/python3
import matplotlib.pyplot as plt

# Sample data 
x_values = [1, 2, 3, 4, 5]
y_values = [5, 4, 6, 2, 7]

# Create a 3D bar chart
plt.bar(x_values, y_values, zdir='z', color='r')

# Adjust plot size and remove gridlines/axes
plt.rcParams['figure.figsize'] = (10, 8)  
plt.rcParams['axes.grid'] = False
plt.subplots_adjust(left=0, right=1, bottom=0, top=1)  
plt.axis('equal')
plt.axis('off')

# Add title and labels
plt.title("Sample 3D Bar Chart")
plt.xlabel("X Axis")  
plt.ylabel("Y Axis")

# Save and show the figure
plt.savefig('3d_bar_chart.png')
plt.show()






# squares = [1, 4, 9, 16, 25]
# plt.plot(squares, linewidth=5)

# # Set chart title and label axes.
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)

# # Set size of tick labels.
# plt.tick_params(axis='both', labelsize=14)

# plt.show()