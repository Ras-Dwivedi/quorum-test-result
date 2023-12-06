import subprocess
import os
import time
import shutil
import json
timestamp = int(time.time())
filename_prefix = "mac_raft_8GB"
def run_exp(a,b):
    a=str(a)
    b=str(b)
    
    # Step 1: Start tps.py in the background
    tps_process = subprocess.Popen(["python", "tps.py"])
    print("tps.py started in the background.")

    # Step 2: Start send.py with arguments a and b
    # a='10'
    # b='sequential'
    send_process = subprocess.Popen(["python", "send.py", a, b])
    print(f"send.py started with arguments {a} and {b}.")

    # Step 3: Wait for send.py to finish
    send_process.wait()
    print("send.py has finished.")

    # Step 4: Wait for tps.py to exit
    tps_process.wait()
    print("tps.py has finished.")

    time.sleep(30)
    # Step 5: Rename exp.json to a_b.json
    folder_path = "./"  # Provide the actual path to the folder
    old_file_path = os.path.join(folder_path, "last-experiment.json")
    filename = f"{filename_prefix}_{a}_{b}_{timestamp}.json"
    new_file_path = os.path.join(folder_path, filename)

    if os.path.exists(old_file_path):
        shutil.move(old_file_path, new_file_path)
        print(f"last-experiment.json renamed to {filename} .")
    else:
        print("last-experiment.json not found.")


def check_tps(filename):
    print(f"checking file {filename}")
    try:
        with open(filename, 'r') as file:
            data = json.load(file)

            # Extract values
            final_tps_av = data.get("tps", {}).get("finalTpsAv", 0)
            peak_tps_av = data.get("tps", {}).get("peakTpsAv", 0)

            # Check if finalTpsAv and peakTpsAv are non-zero
            if final_tps_av != 0 and peak_tps_av != 0:
                return True
            else:
                return False

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return False
    except json.JSONDecodeError:
        print(f"Error decoding JSON in '{filename}'.")
        return False
    except Exception:
        print(e)
        return False
#main code
for a in range(18000,21000,1000):
    for b in ['sequential', 
              'threaded1', 
              'threaded2', 
              'threaded3'
              ]:
        is_exp_success = False
        count = 1
        while(is_exp_success==False):
            try:
                print(f"Running {a} trx in {b} mode")
                run_exp(a,b)
                filename = f"{filename_prefix}_{a}_{b}_{timestamp}.json"
                if check_tps(filename):
                    is_exp_success = True
                    # time.sleep(120)
            except Exception as e:
                print(e)
                time.sleep(count*30)
                count = count+1
                # time.sleep(300)
    # time.sleep(120)
# a='1000'
# b='sequential'
# timestamp ='1701607041'                
# filename = f"{filename_prefix}_{a}_{b}_{timestamp}.json"
# print (check_tps(filename))
