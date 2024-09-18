import sys
import re
input_data = sys.stdin.read()
sentences = re.split(r'[.?!]', input_data)
for sentence in sentences:
    line = [word for word in sentence.split()]
    new_line = ""
    for i in range(len(line)):
        if(i==0):
            new_line += line[i][0].upper() + line[i][1:].lower()
        else:
            new_line += ' ' + line[i].lower()
    print(new_line)