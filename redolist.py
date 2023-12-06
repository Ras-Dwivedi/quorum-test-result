import os
import json
def check_file(filename):
    try:
        # print(f"checking file {filename}")
        with open(filename, 'r') as file:
            data = json.load(file)

            # Extract values
            final_tps_av = data.get("tps", {}).get("finalTpsAv", 0)
            peak_tps_av = data.get("tps", {}).get("peakTpsAv", 0)

            # Check if finalTpsAv and peakTpsAv are non-zero
            if final_tps_av > peak_tps_av:
                print(filename)
                return True
            else:
                return False
    except Exception as e:
        print(f"error in processing file {filename}")
            
def process_folder(input_folder):
    # List to store extracted information from all files
    data_list = []
    # Traverse the folder
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.json'):
            is_skipped = False
            file_path = os.path.join(input_folder, file_name)
            # print(f"filepath given is {file_path}")
            check_file(file_path)
            
process_folder("./RAFT_8GB")

# data_list = [
    # (3000, "sequential"),
    # (9000, "threaded2"),
    # (13000, "threaded1"),
    # (12000, "threaded2"),
    # (5000, "threaded3"),
    # (17000, "threaded2"),
    # (9000, "sequential"),
    # (3000, "threaded3"),
    # (19000, "threaded3"),
    # (19000, "threaded2"),
    # (4000, "sequential"),
    # (13000, "sequential"),
    # (12000, "threaded1"),
    # (11000, "threaded2"),
    # (5000, "sequential"),
    # (17000, "threaded3"),
    # (9000, "threaded3")
# ]

# for (a,b) in data_list:
#     print(a,b)
