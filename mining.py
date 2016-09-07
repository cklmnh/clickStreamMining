line = "D00-MON 02:07:24 U16329 Z1678 U02390 y"#this is an example line, will eventually grab files to fill 2d array

info = []
info.append(line.split(' '))
info.append(line.split(' '))

time = info[0][1]

print(info)
print(time)