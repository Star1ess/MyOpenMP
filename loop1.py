import os
import csv

# 指定包含txt文件的文件夹
data_folder = 'loop1_auto'

# 创建一个字典以存储每种模式下的loop1和loop2时间
data = {}

# 遍历data文件夹下的所有txt文件
for filename in os.listdir(data_folder):
    if filename.endswith('.txt'):
        with open(os.path.join(data_folder, filename), 'r') as file:
            lines = file.readlines()
            loop1_times = []
            for line in lines:
                if "Total time for 1000 reps of loop 1 =" in line:
                    loop1_times.append(float(line.split()[-1]))
            if loop1_times:
                data[filename] = {
                    'Loop 1 Avg Time': sum(loop1_times) / len(loop1_times)
                }

# 将结果写入CSV文件
output_file = 'loop1_output.csv'
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['File', 'Loop 1 Avg Time'])
    writer.writeheader()
    for filename, times in data.items():
        writer.writerow({'File': filename, 'Loop 1 Avg Time': times['Loop 1 Avg Time']})

print(f"数据已写入{output_file}文件。")
