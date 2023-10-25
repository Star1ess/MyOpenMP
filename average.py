import os
import csv

# 指定包含txt文件的文件夹
data_folder = 'data'

# 创建一个字典以存储每种模式下的loop1和loop2时间
data = {}

# 遍历data文件夹下的所有txt文件
for filename in os.listdir(data_folder):
    if filename.endswith('.txt'):
        with open(os.path.join(data_folder, filename), 'r') as file:
            lines = file.readlines()
            loop1_times = []
            loop2_times = []
            for line in lines:
                if "Total time for 1000 reps of loop 1 =" in line:
                    loop1_times.append(float(line.split()[-1]))
                elif "Total time for 1000 reps of loop 2 =" in line:
                    loop2_times.append(float(line.split()[-1]))
            if loop1_times and loop2_times:
                data[filename] = {
                    'Loop 1 Avg Time': sum(loop1_times) / len(loop1_times),
                    'Loop 2 Avg Time': sum(loop2_times) / len(loop2_times)
                }

# 将结果写入CSV文件
output_file = 'output.csv'
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['File', 'Loop 1 Avg Time', 'Loop 2 Avg Time'])
    writer.writeheader()
    for filename, times in data.items():
        writer.writerow({'File': filename, 'Loop 1 Avg Time': times['Loop 1 Avg Time'], 'Loop 2 Avg Time': times['Loop 2 Avg Time']})

print(f"数据已写入{output_file}文件。")