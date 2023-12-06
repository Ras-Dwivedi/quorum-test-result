"""
This files scans all the json in the folder and then creates the csv file with the relevant data
"""
import os
import json
import csv
import pandas as pd
import numpy as np
# from scipy.stats import zscore


from matplotlib import pyplot as plt


# Function to extract required information from a JSON file
def extract_info(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        send_data = data.get('send', {})
        node_data = data.get('node', {})
        tps_data = data.get('tps', {})

        data = {
            'block_first': send_data.get('block_first', 0),
            'block_last': send_data.get('block_last', 0),
            'empty_blocks': send_data.get('empty_blocks', 0),
            'num_txs': send_data.get('num_txs', 0),
            'peakTpsAv': tps_data.get('peakTpsAv', 0),
            'finalTpsAv': tps_data.get('finalTpsAv', 0),
            'start_epochtime': tps_data.get('start_epochtime', 0)
        }
        data['trx_per_block'] = get_avg_trx_per_block(data)
        return data


def get_avg_trx_per_block(data):
    """
    Calculates the average transaction per block
    returns: average transactions per block or None in case data is incorrect
    """
    first_block = data.get('block_first')
    last_block = data.get('block_last')
    # empty_blocks = data.get('empty_blocks')
    num_txs = data.get('num_txs')
    useful_blocks = last_block - first_block
    if useful_blocks < 1:
        print("incorrect data", data)
        return None
    else:
        return num_txs / useful_blocks


# Function to process all JSON files in a folder and create a CSV file
def process_folder(input_folder, output_file):
    # List to store extracted information from all files
    data_list = []
    skipped_files = [
        'sequential',
        'threaded1',
        'threaded2',
        # 'threaded3',
        'contract'
    ]
    # Traverse the folder
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.json'):
            is_skipped = False
            file_path = os.path.join(input_folder, file_name)
            print(f"filepath given is {file_path}")
            for skipped_file in skipped_files:
                if file_path.__contains__(skipped_file):
                    is_skipped = True
            if is_skipped:
                print(f"{file_name} has been skipped")
                continue
            else:
                print(f'{file_name} processed')
            extracted_info = extract_info(file_path)
            data_list.append(extracted_info)

    # Sort the list of dictionaries by 'num_txs'
    data_list.sort(key=lambda x: x['num_txs'])

    # Write the data into a CSV file
    with open(output_file, 'w', newline='') as csv_file:
        fieldnames = ['block_first', 'block_last', 'empty_blocks', 'num_txs', 'peakTpsAv', 'finalTpsAv',
                      'start_epochtime','trx_per_block']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Write header
        writer.writeheader()

        # Write data rows
        for data_row in data_list:
            writer.writerow(data_row)


# def plot_figure(data_file):
#     df = pd.read_csv(data_file)
#
#     # Plot the graph
#     plt.figure(figsize=(10, 6))
#     plt.plot(df['num_txs'], df['peakTpsAv'], label='Peak Tps')
#     plt.plot(df['num_txs'], df['finalTpsAv'], label='Final Tps')
#
#     # Set labels and title
#     plt.xlabel('num_txs')
#     plt.ylabel('Tps')
#     plt.title('Tps vs num_txs')
#
#     # Display legend
#     plt.legend()
#
#     # Show the plot
#     plt.show()


def plot_figure(data_file):
    df = pd.read_csv(data_file)

    # Plot the graph with circles for data points and a smooth curve
    plt.figure(figsize=(10, 6))
    plt.plot(df['num_txs'], df['peakTpsAv'], marker='o', linestyle='-', label='Peak Tps')
    plt.plot(df['num_txs'], df['finalTpsAv'], marker='o', linestyle='--', label='Average Tps', color='red')
    plt.plot(df['num_txs'], df['trx_per_block'], marker='o', linestyle='--', label='Average Tps', color='green')

    # Set labels and title
    plt.xlabel('No. of Transactions sent')
    plt.ylabel('Throughput(TPS)')
    plt.title(f'Throughput vs Number of Transactions: Threaded1')

    # calculating mean throughput
    calculate_mean_and_stddev_without_outliers(df['finalTpsAv'])
    calculate_mean_and_stddev_without_outliers(df['peakTpsAv'])
    # Display legend
    plt.legend()

    # Show the plot
    plt.show()


def calculate_mean_and_stddev(numbers):
    mean_value = np.mean(numbers)
    std_deviation = np.std(numbers)
    # print(f"Mean: {mean_value}")
    # print(f"Standard Deviation: {std_dev}")
    return mean_value, std_deviation


def calculate_mean_and_stddev_without_outliers(numbers, _threshold=3):
    # Calculate Z-scores
    mean, std = calculate_mean_and_stddev(numbers)
    threshold = _threshold * std

    # Identify and remove outliers
    outliers = np.abs(numbers - mean) > threshold
    filtered_data = numbers[~outliers]

    mean_value, std_deviation = calculate_mean_and_stddev(filtered_data)
    # z_scores = zscore(numbers)

    # # Identify outliers using the threshold
    # outliers = np.abs(z_scores) > threshold

    # # Remove outliers
    # filtered_numbers = np.array(numbers)[~outliers]

    # # Calculate mean and standard deviation without outliers
    # mean_value = np.mean(filtered_numbers)
    # std_deviation = np.std(filtered_numbers)
    print(f"Mean: {mean_value}")
    print(f"Standard Deviation: {std_deviation}")
    return mean_value, std_deviation


# Example usage:


# Example usage:
# plot_figure('output.csv')

# Specify the input folder containing JSON files and the output CSV file
input_folder = './'
output_file = 'output.csv'

# Call the function to process the folder and create the CSV file
process_folder(input_folder, output_file)
plot_figure('output.csv')
