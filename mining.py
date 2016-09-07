fileDirectory = "Webscope_G5/ydata-ymessenger-user-communication-pattern-v1_0/ydata-ymessenger-user-communication-pattern-v1_0-d"

info = []#2d array for info

for x in range(0, 28): #there are 28 total files needed to read in
    if x < 10:
        file = open(fileDirectory + "0" + repr(x) + ".txt", "r")# open file for reading based off of directory above
    else:
        file = open(fileDirectory + repr(x) + ".txt", "r")

    for line in file:
        line = line[:-1]
        info.append(line.split(' '))


#print info[5]

for x in range(0, 50):
    print info[x]