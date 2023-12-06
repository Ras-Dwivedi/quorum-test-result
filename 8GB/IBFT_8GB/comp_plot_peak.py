import matplotlib.pyplot as plt
import numpy as np

# Data for QBFT - 8 GB
qbft_avg = [96.69, 102.20, 115.44, 103.71]
qbft_peak = [103.99, 104.37, 120.24, 109.29]

# Data for IBFT - 8 GB
ibft_avg = [88.62, 101.60, 112.65, 103.19]
ibft_peak = [93.78, 103.35, 114.52, 106.48]

# Bar width
bar_width = 0.35

# Set up bar positions
index = np.arange(len(qbft_avg))

# Plotting
fig, ax = plt.subplots()
bar1 = ax.bar(index - bar_width/2, qbft_peak, bar_width, label='QBFT - 8GB (Peak)')
bar2 = ax.bar(index + bar_width/2, ibft_peak, bar_width, label='IBFT - 8GB (Peak)')

# Add error bars for standard deviation
ax.errorbar(index - bar_width/2, qbft_peak, yerr=[10.21, 6.12, 8.53, 7.65], fmt='none', color='black')
ax.errorbar(index + bar_width/2, ibft_peak, yerr=[9.16, 7.14, 5.66, 6.50], fmt='none', color='black')

# Set labels and title
ax.set_xlabel('Scenarios')
ax.set_ylabel('Average Peak Throughput (TPS)')
ax.set_title('Comparison of QBFT and IBFT on 8GB VM')
ax.set_xticks(index)
ax.set_xticklabels(['Sequential', 'Threaded 1', 'Threaded 2', 'Threaded 3'])
ax.legend()

# Show the plot
plt.show()

