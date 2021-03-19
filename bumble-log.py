import re
import datetime

inputFile_1 = input("first file path: ")
name_1 = input("first contact name: ")
inputFile_2 = input("second file path: ")
name_2 = input("second contact name: ")
outputFile = input("output file path: ")

def parse(line, name):
    line = line.lstrip()
    result = re.search('(.*)\)', line).group(1)[4:]
    time = datetime.datetime.strptime(result, '%Y-%m-%d %H:%M:%S')
    out = name + line[2:]
    out = out.strip()
    return time, out

with open(inputFile_1) as f_1:
    with open(inputFile_2) as f_2:
        with open(outputFile, 'w') as f_out:
            line_1 = f_1.readline()[:-1]
            line_2 = f_2.readline()[:-1]
            time_1, out_1 = parse(line_1, name_1)
            time_2, out_2 = parse(f_2.readline(), name_2)
            while line_1 or line_2:
                if time_1 <= time_2:
                    f_out.write(out_1 + "\n")
                    line_1 = f_1.readline()
                    if(line_1):
                        time_1, out_1 = parse(line_1, name_1)
                    else:
                        time_1 = datetime.datetime.max
                else:
                    f_out.write(out_2 + "\n")
                    line_2 = f_2.readline()
                    if(line_2):
                        time_2, out_2 = parse(line_2, name_2)
                    else:
                        time_2 = datetime.datetime.max
            f_out.close()
        f_2.close()
    f_1.close()

print("\nresult written to " + outputFile)