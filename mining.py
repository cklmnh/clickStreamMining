fileDirectory = "Webscope_G5/ydata-ymessenger-user-communication-pattern-v1_0/ydata-ymessenger-user-communication-pattern-v1_0-d"

info = []#2d array for info

def percentFriends(startIndex, stopIndex):
    friends = 0
    for x in range(startIndex, stopIndex):
        if info[x][5] == 'y':
            friends += 1
    return friends / (stopIndex - startIndex)

for x in range(0, 1): #there are 28 total files needed to read in
    if x < 10:
        file = open(fileDirectory + "0" + repr(x) + ".txt", "r")# open file for reading based off of directory above
    else:
        file = open(fileDirectory + repr(x) + ".txt", "r")

    for line in file:
        line = line[:-1]
        info.append(line.split(' '))

#print(len(info))
print(percentFriends(0, 100)*100,'% of people in the first file are communicating with friends')



