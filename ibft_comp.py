import matplotlib.pyplot as plt
import numpy as np

#QBFT 8 gB
qbft_8_avg = [96.68537492902124, 102.20324727568101, 115.43521189058598, 103.71252170867555]
qbft_8_avg_std = [10.211896229266324, 6.123011343683894, 8.533949396766312, 7.6514130330559755]
qbft_8_peak = [103.98521748394003, 104.37435579015342, 120.24313818808567, 109.2860345560011]
qbft_8_peak_std = [9.12809790584352, 10.361234693402508, 6.4167996184118685, 10.452552487764216]


#IBFT 8 GB
ibft_8_avg = [88.61811155633302, 101.59820605967484, 112.65024753131537, 103.19278505829644]
ibft_8_avg_std = [9.162583016378097, 7.136358136645045, 5.658396989203818, 6.498999223888256]
ibft_8_peak = [93.77885006682114, 103.35220245276167, 114.52331599258899, 106.48342295991718]
ibft_8_peak_std= [8.829558412823138, 7.381158452860294, 4.997395751938968, 3.902974573880183]

#RAFT 8 GB
raft_8_avg = [58.29224211916728, 63.225988870476904, 80.38645363231916, 66.87448156989713]
raft_8_avg_std = [20.865896438710628, 25.94876863753805, 11.16240305101142, 18.21083987359756]
raft_8_peak = [65.28383769439465, 68.75159736389962, 85.14401459000838, 73.69845396913178]
raft_8_peak_std= [16.691543334383198, 20.67157138361509, 7.102526141779648, 15.07598991523226]

# 32 GB experiment
qbft_32_avg = [156.70189120981962, 174.17405159309948, 180.47361386883796, 184.04709851771858]
qbft_32_avg_std = [14.734528266209685, 30.170879299882895, 51.617851220185685, 18.941500981192338]
qbft_32_peak = [165.1454727535389, 172.29910240493473, 188.2510871580385, 198.27180874306762]
qbft_32_peak_std= [15.924547634667594, 59.81071062333284, 51.509293223754355, 20.802443278394914]

#IBFT 32 GB
ibft_32_avg = [130.44317678060926, 178.9985513196977, 196.66380692986772, 172.74895312703558]
ibft_32_avg_std = [41.38149263660223, 21.50656157604873, 21.537959036917627, 28.24766265102131]
ibft_32_peak = [134.13623166311868, 187.31870415222448, 203.60857316776273, 185.38078162140187]
ibft_32_peak_std = [43.413190509798724, 17.981977734197457, 22.777290410863575, 18.658570093829876]

#RAFT 32 GB
raft_32_avg = [152.65109276017702, 172.50849276001182, 193.57519921139516, 168.50592861810492]
raft_32_avg_std = [25.673251080057963, 18.263862116247857, 12.750380547041239, 23.344562631408525]
raft_32_peak = [155.39442188357168, 181.26271946755028, 195.98711205965577, 179.30851135851967]
raft_32_peak_std = [25.66377351225544, 9.987165793985756, 12.150259319958685, 12.017138618397333]

## Multinode data

#QBFT multi node
qbft_multinode_avg = [129.78664382567703, 152.82359258828762, 159.8396219322083, 161.57556968254912]
qbft_multinode_avg_std = [31.395046162597538, 17.305278375082445, 29.971862886414492, 24.48110676153029]
qbft_multinode_peak = [143.37568090752046, 167.08831395324404, 178.94187360830801, 164.4736248283873]
qbft_multinode_peak_std = [31.948349430465424, 19.782715153706214, 32.067617891992484, 58.31987718470724]

# IBFT multinode
ibft_multinode_avg = [133.83572837442307, 136.7715963680028, 147.4621198229102, 131.73655842381905]
ibft_multinode_avg_std = [14.276619865247481, 23.97229155183365, 26.057164848093173, 25.250080142813136]
ibft_multinode_peak = [142.28863963375622, 160.1703016442225, 174.40421654434516, 159.0193050996344]
ibft_multinode_peak_std = [8.514714643799058, 18.484305487731252, 14.534019697450772, 12.975170796289541]

# RAFT Multinode

raft_multinode_avg = [105.94899698881326, 105.94899698881326, 132.44780551506983, 120.78205505729406]
raft_multinode_avg_std = [9.899597237538805, 9.899597237538805, 14.920459556351702, 17.654098998354936]
raft_multinode_peak = [115.34257711309847, 115.34257711309847, 137.4731276660009, 123.88068700265782]
raft_multinode_peak_std = [9.486584083834511, 9.486584083834511, 15.06493555073281, 18.905091570968356]

# # Data for IBFT on 8GB VM
# ibft_8gb_avg = [88.62, 101.60, 112.65, 103.19]
# ibft_8gb_std = [9.16, 7.14, 5.66, 6.50]

# # Data for IBFT on 32GB VM
# ibft_32gb_avg = [130.44, 178.99, 196.66, 172.75]
# ibft_32gb_std = [41.38, 21.51, 21.54, 28.25]

# # Data for 4-node IBFT
# ibft_4node_avg = [133.84, 136.77, 147.46, 131.74]
# ibft_4node_std = [14.28, 23.97, 26.06, 25.25]


# Data for IBFT on 8GB VM
ibft_8gb_avg = [93.78, 104.37, 114.52, 106.48]
ibft_8gb_std = [8.83, 7.38, 4.99, 3.90]

# Data for IBFT on 32GB VM
ibft_32gb_avg = [134.14, 187.32, 203.61, 185.38]
ibft_32gb_std = [43.41, 17.98, 22.78, 18.66]

# Data for 4-node IBFT
ibft_4node_avg = [142.29, 160.17, 174.40, 159.02]
ibft_4node_std = [8.51, 18.48, 14.53, 12.98]

def plot_8gb():
	bar_width = 0.2

	# Set up bar positions
	index = np.arange(len(ibft_8_avg))

	# Plotting
	fig, ax = plt.subplots()
	bar1 = ax.bar(index - bar_width, ibft_8_avg, bar_width, yerr=ibft_8_avg_std, label='IBFT')
	bar2 = ax.bar(index, qbft_8_avg, bar_width, yerr=qbft_8_avg_std, label='QBFT')
	bar3 = ax.bar(index + bar_width, raft_8_avg, bar_width, yerr=raft_8_avg_std, label='RAFT')
	# bar2 = ax.bar(index, ibft_32gb_avg, bar_width, yerr=ibft_32gb_std, label='IBFT 32GB')
	# bar3 = ax.bar(index + bar_width, ibft_4node_avg, bar_width, yerr=ibft_4node_std, label='4-node IBFT')

	# Set labels and title
	ax.set_xlabel('Scenarios')
	ax.set_ylabel('Average Peak Throughput (TPS)')
	ax.set_title('Performance of Different Consensus On 8GB VM')
	ax.set_xticks(index)
	ax.set_xticklabels(['Sequential', 'Threaded 1', 'Threaded 2', 'Threaded 3'])
	ax.legend()

	# Show the plot
	plt.show()

def plot_32gb():
	bar_width = 0.2

	# Set up bar positions
	index = np.arange(len(ibft_8_avg))

	# Plotting
	fig, ax = plt.subplots()
	bar1 = ax.bar(index - bar_width, ibft_32_avg, bar_width, yerr=ibft_32_avg_std, label='IBFT')
	bar2 = ax.bar(index, qbft_32_avg, bar_width, yerr=qbft_32_avg_std, label='QBFT')
	bar3 = ax.bar(index + bar_width, raft_32_avg, bar_width, yerr=raft_32_avg_std, label='RAFT')
	# bar2 = ax.bar(index, ibft_32gb_avg, bar_width, yerr=ibft_32gb_std, label='IBFT 32GB')
	# bar3 = ax.bar(index + bar_width, ibft_4node_avg, bar_width, yerr=ibft_4node_std, label='4-node IBFT')

	# Set labels and title
	ax.set_xlabel('Scenarios')
	ax.set_ylabel('Average Peak Throughput (TPS)')
	ax.set_title('Performance of Different Consensus On 32 GB VM')
	ax.set_xticks(index)
	ax.set_xticklabels(['Sequential', 'Threaded 1', 'Threaded 2', 'Threaded 3'])
	ax.legend()
	# Show the plot
	plt.show()

def plot_multinode():
	bar_width = 0.2

	# Set up bar positions
	index = np.arange(len(ibft_8_avg))

	# Plotting
	fig, ax = plt.subplots()
	bar1 = ax.bar(index - bar_width, ibft_multinode_avg, bar_width, yerr=ibft_multinode_avg_std, label='IBFT')
	bar2 = ax.bar(index, qbft_multinode_avg, bar_width, yerr=qbft_multinode_avg_std, label='QBFT')
	bar3 = ax.bar(index + bar_width, raft_multinode_avg, bar_width, yerr=raft_multinode_avg_std, label='RAFT')
	# bar2 = ax.bar(index, ibft_32gb_avg, bar_width, yerr=ibft_32gb_std, label='IBFT 32GB')
	# bar3 = ax.bar(index + bar_width, ibft_4node_avg, bar_width, yerr=ibft_4node_std, label='4-node IBFT')

	# Set labels and title
	ax.set_xlabel('Scenarios')
	ax.set_ylabel('Average Peak Throughput (TPS)')
	ax.set_title('Performance of Different Consensus On 4-node deployment')
	ax.set_xticks(index)
	ax.set_xticklabels(['Sequential', 'Threaded 1', 'Threaded 2', 'Threaded 3'])
	ax.legend()
	# Show the plot
	plt.show()
	
def plot_qbft():
	bar_width = 0.2

	# Set up bar positions
	index = np.arange(len(ibft_8_avg))

	# Plotting
	fig, ax = plt.subplots()
	bar1 = ax.bar(index - bar_width, qbft_8_avg, bar_width, yerr=qbft_8_avg_std, label='8 GB VM')
	bar2 = ax.bar(index, qbft_32_avg, bar_width, yerr=qbft_32_avg_std, label='32 GB VM')
	bar3 = ax.bar(index + bar_width, qbft_multinode_avg, bar_width, yerr=qbft_multinode_avg_std, label='4 node network')

	# Set labels and title
	ax.set_xlabel('Scenarios')
	ax.set_ylabel('Average Peak Throughput (TPS)')
	ax.set_title('Performance of QBFT on different deployments')
	ax.set_xticks(index)
	ax.set_xticklabels(['Sequential', 'Threaded 1', 'Threaded 2', 'Threaded 3'])
	ax.legend()
	# Show the plot
	plt.show()

# plot_8gb()
# plot_32gb()
# plot_multinode()
plot_qbft()


