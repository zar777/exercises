import sys

n_skyscrapers = sys.stdin.readline()
skyscrapers = sys.stdin.readline().strip().split(" ")
route = 0
for i in xrange(0, len(skyscrapers)):
    for j in xrange(i+1, len(skyscrapers)):
        if skyscrapers[j] > skyscrapers[i]:
            i += 1
        elif skyscrapers[j] == skyscrapers[i]:
            print " uguaglianze " + skyscrapers[j] + " == " + skyscrapers[i]
            route += 2
print route