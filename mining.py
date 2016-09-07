fileDirectory = "Webscope_G5/ydata-ymessenger-user-communication-pattern-v1_0/ydata-ymessenger-user-communication-pattern-v1_0-d00.txt"

file = open(fileDirectory, "r")#open file for reading based off of directory above

info = []#2d array for info

for line in file:
    info.append(line.split(' '))

print(info[5])
print(len(info))