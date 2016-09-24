def solution(a,b,c):

    while b <= 4 and a < 12:
        a = (a + a) * c

    return a,b

if __name__ == '__main__':

    print solution(2, 0, 1)



    include <map>
    # I assume I have a function parseInt that parses a string into an int

    unsigned long normalise(unsigned long input_time)
    {
        map < string, int > m = {{'Sun', 0}, {'Mon;, 1}, {'Tue', 2}, {'Wed', 3},{'Thu', 4},{'Fri', 5},{'Sat', 6}};

    int total = 0;
    string str_time = format_time(input_time);
    total += str_time.substr(17, 2).parseInt();
    total += str_time.substr(14, 2).parseInt() * 60;
    total += str_time.substr(11, 2).parseInt() * 60 * 60;
    total += m[str_time.substr(0, 3)] * 60 * 60 * 24;
    input_time -= total;
    }
    return input_time;