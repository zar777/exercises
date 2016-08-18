import sys

n_seq= int(sys.stdin.readline().split(" ")[0])
last_answer = 0
sequences = [[] for x in xrange(n_seq)]
for line in sys.stdin:
    line_split = line.split(" ")
    number_seq = (int(line_split[1]) ^ last_answer) % n_seq
    if int(line_split[0]) == 1:
        sequences[number_seq].append(int(line_split[2]))
    else:
        value = int(line_split[2]) % len(sequences[number_seq])
        last_answer = sequences[number_seq][value]
        print last_answer

if __name__ == '__main__':
    pass