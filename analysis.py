 # some small logic error

import time
import multiprocessing
import subprocess
import psutil
start_time = time.time() #checks the time it take to execute the code

def get_memory_usage():
    process = psutil.Process()
    memory_info = process.memory_info()
    memory_mb = memory_info.rss / (1024 * 1024)  # Convert to megabytes
    return memory_mb

'''----------------------------------------------START OF CODE FUNTIONALITY--------------------------------'''
print("------------------------------------------ENCODER---------------------------------------------")
print("\n")
def v_xor(bit0, bit1):
    if bit0 == bit1:
        return "0"
    else:
        return "1"

def viterbi_encoder(inputs):
    # Define the shift register with 7 elements (as per the code)
    s_reg = ["0", "0", "0", "0", "0", "0", "0"]
    obs = []

    for t in range(0, len(inputs)):
        # Shifting the bits to the right
        s_reg[6] = s_reg[5]
        s_reg[5] = s_reg[4]
        s_reg[4] = s_reg[3]
        s_reg[3] = s_reg[2]
        s_reg[2] = s_reg[1]
        s_reg[1] = s_reg[0]

        # Inserting input into the shift register
        s_reg[0] = inputs[t]

        # Calculate the encoded bits using XOR operations
        output_bit1 = v_xor(v_xor(v_xor(v_xor(s_reg[0], s_reg[1]), s_reg[2]), s_reg[3]), s_reg[6])
        output_bit2 = v_xor(v_xor(v_xor(v_xor(s_reg[0], s_reg[2]), s_reg[3]), s_reg[5]), s_reg[6])

        # Combine the two encoded bits and append them to the 'obs' list
        encoded_bit = output_bit1 + output_bit2
        obs.append(encoded_bit)
    return obs

# Input sequence
inputs = ["1", "0", "0", "1", "1"] #works for certain inputs ????
print("Input Bits: ", inputs)
obs1 = viterbi_encoder(inputs)
print("Encoded output bits : ", obs1)
print('\n')
print("------------------------------------------DECODER---------------------------------------------")
print("\n")
def Reverse(obs):
	new_tup = obs[::-1]
	return new_tup
	
# Driver Code
print("Encoded Input bits:",obs1)
obs = Reverse(obs1)

#STATE METRIC DEFINE THE INITISAL STATES
start_metric = {'s0': 0, 's1': 0, 's2': 0, 's3': 0, 's4': 0, 's5': 0, 's6': 0, 
                's7': 0, 's8': 0, 's9': 0, 's10': 0, 's11': 0, 's12': 0, 's13': 0, 
                's14': 0, 's15': 0, 's16': 0, 's17': 0, 's18': 0, 's19': 0, 's20': 0, 
                's21': 0, 's22': 0, 's23': 0, 's24': 0, 's25': 0, 's26': 0, 's27': 0, 
                's28': 0, 's29': 0, 's30': 0, 's31': 0, 's32': 0, 's33': 0, 's34': 0,
                's35': 0, 's36': 0, 's37': 0, 's38': 0, 's39': 0, 's40': 0, 's41': 0, 
                's42': 0, 's43': 0, 's44': 0, 's45': 0, 's46': 0, 's47': 0, 's48': 0,
                's49': 0, 's50': 0, 's51': 0, 's52': 0, 's53': 0, 's54': 0, 's55': 0,
                's56': 0, 's57': 0, 's58': 0, 's59': 0, 's60': 0, 's61': 0, 's62': 0,
                's63': 0}

#FINITE STATE MACHINE FOR 64 STATES AND W.R.T CSDSS CONVENTIONS. ONE VALUE ERROR CAN COUSE THE WHOLE LOGIC TO BOMB
fsm = {
    
    's0': {'b1': {'out_b': '11', 'prev_st': 's1', 'input_b': 0},
           'b2': {'out_b': '00', 'prev_st': 's0', 'input_b': 0}},

    's1': {'b1': {'out_b': '10', 'prev_st': 's3', 'input_b': 0},
           'b2': {'out_b': '01', 'prev_st': 's2', 'input_b': 0}},

    's2': {'b1': {'out_b': '11', 'prev_st': 's5', 'input_b': 0},
           'b2': {'out_b': '00', 'prev_st': 's4', 'input_b': 0}},

    's3': {'b1': {'out_b': '10', 'prev_st': 's7', 'input_b': 0},
           'b2': {'out_b': '01', 'prev_st': 's6', 'input_b': 0}},

    's4': {'b1': {'out_b': '00', 'prev_st': 's9', 'input_b': 0},
           'b2': {'out_b': '11', 'prev_st': 's8', 'input_b': 0}},

    's5': {'b1': {'out_b': '01', 'prev_st': 's11', 'input_b': 0},
           'b2': {'out_b': '10', 'prev_st': 's10', 'input_b': 0}},

    's6': {'b1': {'out_b': '00', 'prev_st': 's13', 'input_b': 0},
           'b2': {'out_b': '11', 'prev_st': 's12', 'input_b': 0}},

    's7': {'b1': {'out_b': '01', 'prev_st': 's15', 'input_b': 0},
           'b2': {'out_b': '10', 'prev_st': 's14', 'input_b': 0}},

    's8': {'b1': {'out_b': '00', 'prev_st': 's17', 'input_b': 0},
           'b2': {'out_b': '11', 'prev_st': 's16', 'input_b': 0}},

    's9': {'b1': {'out_b': '01', 'prev_st': 's19', 'input_b': 0},
           'b2': {'out_b': '10', 'prev_st': 's18', 'input_b': 0}},

    's10': {'b1': {'out_b': '00', 'prev_st': 's21', 'input_b': 0},
            'b2': {'out_b': '11', 'prev_st': 's20', 'input_b': 0}},

    's11': {'b1': {'out_b': '01', 'prev_st': 's23', 'input_b': 0},
           'b2': {'out_b': '10', 'prev_st': 's22', 'input_b': 0}},

    's12': {'b1': {'out_b': '11', 'prev_st': 's25', 'input_b': 0},
           'b2': {'out_b': '00', 'prev_st': 's24', 'input_b': 0}},

    's13': {'b1': {'out_b': '10', 'prev_st': 's27', 'input_b': 0},
           'b2': {'out_b': '01', 'prev_st': 's26', 'input_b': 0}},

    's14': {'b1': {'out_b': '11', 'prev_st': 's29', 'input_b': 0},
           'b2': {'out_b': '00', 'prev_st': 's28', 'input_b': 0}},

    's15': {'b1': {'out_b': '10', 'prev_st': 's31', 'input_b': 0},
           'b2': {'out_b': '01', 'prev_st': 's30', 'input_b': 0}},

    's16': {'b1': {'out_b': '01', 'prev_st': 's33', 'input_b': 0},
           'b2': {'out_b': '10', 'prev_st': 's32', 'input_b': 0}},

    's17': {'b1': {'out_b': '00', 'prev_st': 's35', 'input_b': 0},
           'b2': {'out_b': '11', 'prev_st': 's34', 'input_b': 0}},

    's18': {'b1': {'out_b': '01', 'prev_st': 's37', 'input_b': 0},
           'b2': {'out_b': '10', 'prev_st': 's36', 'input_b': 0}},

    's19': {'b1': {'out_b': '00', 'prev_st': 's39', 'input_b': 0},
           'b2': {'out_b': '11', 'prev_st': 's38', 'input_b': 0}},

    's20': {'b1': {'out_b': '10', 'prev_st': 's41', 'input_b': 0},
           'b2': {'out_b': '01', 'prev_st': 's40', 'input_b': 0}},

    's21': {'b1': {'out_b': '11', 'prev_st': 's43', 'input_b': 0},
           'b2': {'out_b': '00', 'prev_st': 's42', 'input_b': 0}},

    's22': {'b1': {'out_b': '10', 'prev_st': 's45', 'input_b': 0},
           'b2': {'out_b': '01', 'prev_st': 's44', 'input_b': 0}},

    's23': {'b1': {'out_b': '11', 'prev_st': 's47', 'input_b': 0},
           'b2': {'out_b': '00', 'prev_st': 's46', 'input_b': 0}},

    's24': {'b1': {'out_b': '10', 'prev_st': 's49', 'input_b': 0},
           'b2': {'out_b': '01', 'prev_st': 's48', 'input_b': 0}},

    's25': {'b1': {'out_b': '11', 'prev_st': 's51', 'input_b': 0},
           'b2': {'out_b': '00', 'prev_st': 's50', 'input_b': 0}},

    's26': {'b1': {'out_b': '10', 'prev_st': 's53', 'input_b': 0},
           'b2': {'out_b': '01', 'prev_st': 's52', 'input_b': 0}},

    's27': {'b1': {'out_b': '11', 'prev_st': 's55', 'input_b': 0},
           'b2': {'out_b': '00', 'prev_st': 's54', 'input_b': 0}},

    's28': {'b1': {'out_b': '01', 'prev_st': 's57', 'input_b': 0},
           'b2': {'out_b': '10', 'prev_st': 's56', 'input_b': 0}},

    's29': {'b1': {'out_b': '00', 'prev_st': 's59', 'input_b': 0},
           'b2': {'out_b': '11', 'prev_st': 's58', 'input_b': 0}},

    's30': {'b1': {'out_b': '01', 'prev_st': 's61', 'input_b': 0},
           'b2': {'out_b': '10', 'prev_st': 's60', 'input_b': 0}},

    's31': {'b1': {'out_b': '00', 'prev_st': 's63', 'input_b': 0},
           'b2': {'out_b': '11', 'prev_st': 's62', 'input_b': 0}},

    's32': {'b1': {'out_b': '00', 'prev_st': 's1', 'input_b': 1},
           'b2': {'out_b': '11', 'prev_st': 's0', 'input_b': 1}},

    's33': {'b1': {'out_b': '01', 'prev_st': 's3', 'input_b': 1},
           'b2': {'out_b': '10', 'prev_st': 's2', 'input_b': 1}},

    's34': {'b1': {'out_b': '00', 'prev_st': 's5', 'input_b': 1},
           'b2': {'out_b': '11', 'prev_st': 's4', 'input_b': 1}},

    's35': {'b1': {'out_b': '01', 'prev_st': 's7', 'input_b': 1},
           'b2': {'out_b': '10', 'prev_st': 's6', 'input_b': 1}},

    's36': {'b1': {'out_b': '11', 'prev_st': 's9', 'input_b': 1},
           'b2': {'out_b': '00', 'prev_st': 's8', 'input_b': 1}},

    's37': {'b1': {'out_b': '10', 'prev_st': 's11', 'input_b': 1},
           'b2': {'out_b': '01', 'prev_st': 's10', 'input_b': 1}},

    's38': {'b1': {'out_b': '11', 'prev_st': 's13', 'input_b': 1},
           'b2': {'out_b': '00', 'prev_st': 's12', 'input_b': 1}},

    's39': {'b1': {'out_b': '10', 'prev_st': 's15', 'input_b': 1},
           'b2': {'out_b': '01', 'prev_st': 's14', 'input_b': 1}},

    's40': {'b1': {'out_b': '11', 'prev_st': 's17', 'input_b': 1},
           'b2': {'out_b': '00', 'prev_st': 's16', 'input_b': 1}},

    's41': {'b1': {'out_b': '10', 'prev_st': 's19', 'input_b': 1},
           'b2': {'out_b': '01', 'prev_st': 's18', 'input_b': 1}},

    's42': {'b1': {'out_b': '11', 'prev_st': 's21', 'input_b': 1},
            'b2': {'out_b': '00', 'prev_st': 's20', 'input_b': 1}},

    's43': {'b1': {'out_b': '10', 'prev_st': 's23', 'input_b': 1},
           'b2': {'out_b': '01', 'prev_st': 's22', 'input_b': 1}},

    's44': {'b1': {'out_b': '00', 'prev_st': 's25', 'input_b': 1},
           'b2': {'out_b': '11', 'prev_st': 's24', 'input_b': 1}},

    's45': {'b1': {'out_b': '01', 'prev_st': 's27', 'input_b': 1},
           'b2': {'out_b': '10', 'prev_st': 's26', 'input_b': 1}},

    's46': {'b1': {'out_b': '00', 'prev_st': 's29', 'input_b': 1},
           'b2': {'out_b': '11', 'prev_st': 's28', 'input_b': 1}},

    's47': {'b1': {'out_b': '01', 'prev_st': 's31', 'input_b': 1},
           'b2': {'out_b': '10', 'prev_st': 's30', 'input_b': 1}},

    's48': {'b1': {'out_b': '10', 'prev_st': 's33', 'input_b': 1},
           'b2': {'out_b': '01', 'prev_st': 's32', 'input_b': 1}},

    's49': {'b1': {'out_b': '11', 'prev_st': 's35', 'input_b': 1},
           'b2': {'out_b': '00', 'prev_st': 's34', 'input_b': 1}},

    's50': {'b1': {'out_b': '10', 'prev_st': 's37', 'input_b': 1},
           'b2': {'out_b': '01', 'prev_st': 's36', 'input_b': 1}},

    's51': {'b1': {'out_b': '11', 'prev_st': 's39', 'input_b': 1},
           'b2': {'out_b': '00', 'prev_st': 's38', 'input_b': 1}},

    's52': {'b1': {'out_b': '01', 'prev_st': 's41', 'input_b': 1},
           'b2': {'out_b': '10', 'prev_st': 's40', 'input_b': 1}},

    's53': {'b1': {'out_b': '00', 'prev_st': 's43', 'input_b': 1},
           'b2': {'out_b': '11', 'prev_st': 's42', 'input_b': 1}},

    's54': {'b1': {'out_b': '01', 'prev_st': 's45', 'input_b': 1},
           'b2': {'out_b': '10', 'prev_st': 's44', 'input_b': 1}},

    's55': {'b1': {'out_b': '00', 'prev_st': 's47', 'input_b': 1},
           'b2': {'out_b': '11', 'prev_st': 's46', 'input_b': 1}},

    's56': {'b1': {'out_b': '01', 'prev_st': 's49', 'input_b': 1},
           'b2': {'out_b': '10', 'prev_st': 's48', 'input_b': 1}},

    's57': {'b1': {'out_b': '00', 'prev_st': 's51', 'input_b': 1},
           'b2': {'out_b': '11', 'prev_st': 's50', 'input_b': 1}},

    's58': {'b1': {'out_b': '01', 'prev_st': 's53', 'input_b': 1},
           'b2': {'out_b': '10', 'prev_st': 's52', 'input_b': 1}},

    's59': {'b1': {'out_b': '00', 'prev_st': 's55', 'input_b': 1},
           'b2': {'out_b': '11', 'prev_st': 's54', 'input_b': 1}},

    's60': {'b1': {'out_b': '10', 'prev_st': 's57', 'input_b': 1},
           'b2': {'out_b': '01', 'prev_st': 's56', 'input_b': 1}},

    's61': {'b1': {'out_b': '11', 'prev_st': 's59', 'input_b': 1},
           'b2': {'out_b': '00', 'prev_st': 's58', 'input_b': 1}},

    's62': {'b1': {'out_b': '10', 'prev_st': 's61', 'input_b': 1},
           'b2': {'out_b': '01', 'prev_st': 's60', 'input_b': 1}},

    's63': {'b1': {'out_b': '11', 'prev_st': 's63', 'input_b': 1},
           'b2': {'out_b': '10', 'prev_st': 's62', 'input_b': 1}},

}


# The rest of your code remains the same.
def bits_diff_num(num_1, num_2):
    count = 0
    min_length = min(len(num_1), len(num_2))
    
    for i in range(min_length):
        if num_1[i] != num_2[i]:
            count += 1
    
    # If one number is longer than the other, count the extra differences
    count += abs(len(num_1) - len(num_2))
    
    return count

#VITERBI FUNCTIONALITY STARTS HERE. FACED SOME ISSUES BUT SORTED IT OUT. 
def viterbi(obs, start_metric, state_machine):
    V = [{}]
    for st in state_machine:
        V[0][st] = {"metric": start_metric[st], "branch": None}  # Initialize branch as None

    for t in range(1, len(obs) + 1):
        V.append({})
        for st in state_machine:
            prev_st = state_machine[st]['b1']['prev_st']
            first_b_metric = V[(t-1)][prev_st]["metric"] + bits_diff_num(state_machine[st]['b1']['out_b'], obs[t - 1])
            prev_st = state_machine[st]['b2']['prev_st']
            second_b_metric = V[(t - 1)][prev_st]["metric"] + bits_diff_num(state_machine[st]['b2']['out_b'], obs[t - 1])

            if first_b_metric > second_b_metric:
                V[t][st] = {"metric": second_b_metric, "branch": 'b2'}
            else:
                V[t][st] = {"metric": first_b_metric, "branch": 'b1'}

    # Rest of code deals iwth branch calculation and path metrics.

    smaller = min(V[t][st]["metric"] for st in state_machine)
    source_state = None
    for st in state_machine:
        if V[len(obs)][st]["metric"] == smaller:
            source_state = st
            break

    path = []
    for t in range(len(obs), 0, -1):
        branch = V[t][source_state]["branch"]
        path.append(state_machine[source_state][branch]['input_b'])
        source_state = state_machine[source_state][branch]['prev_st']

    return path


output_bits = viterbi(obs, start_metric, fsm)
output_bits = [str(bit) for bit in output_bits]
print("Decoded Bits:", ''.join(output_bits))
print('\n')

''' ----------------------------------------------------- END OF FUNCTIONALITY ---------------------------------------'''
print('Analysis : \n')
end_time = time.time()

# Calculate the execution time
execution_time = end_time - start_time

print(f"Execution time: {execution_time} seconds")

#FOR CALCULATING THE MEMORY USAGE
# Check memory usage after running a section of your code
memory_used = get_memory_usage()
print(f"Memory used: {memory_used:.2f} MB")

#FOR CALCULATING THE NUMBER OF PROCESSORS IT TAKES TO EXECUTE OUR CODE. TO MANY INPUTS CAN INCRESE THE USAGE
num_processors = multiprocessing.cpu_count()
print(f"Number of CPU cores: {num_processors}")

# Define the command to run nvidia-smi
command = "nvidia-smi"

# Run nvidia-smi and capture its output
try:
    output = subprocess.check_output(command, shell=True, universal_newlines=True)
    # Print or process the captured output as needed
    print(output)
except subprocess.CalledProcessError as e:
    # Handle any errors that occur while running the command
    print(f"Error: {e}")

# Define the path of the file or directory you want to check
path = "D:/Krithick/FINAL YEAR PROJECT/Codes/Viterbi codes/analysis.py"

# Check if the path exists
if psutil.disk_partitions(all=True):
    partitions = psutil.disk_partitions(all=True)
    for partition in partitions:
        if path.startswith(partition.mountpoint):
            usage = psutil.disk_usage(partition.device)
            total_size = usage.total / (1024 ** 3)
            total_free = usage.free / (1024 ** 3)
            total_used = usage.used / (1024 ** 3)

            print(f"Total Size: {total_size:.2f} GB")
            print(f"Used Size: {total_used:.2f} GB")
            print(f"Free Size: {total_free:.2f} GB")
            break
    else:
        print(f"The path '{path}' does not exist.")
else:
    print("No disk partitions found.")