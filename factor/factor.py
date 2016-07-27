import math


def solution(N):
    if N == 1:
        return 1
    sqrt = int(math.sqrt(N))
    factors = 2
    while sqrt > 1:
        if N % sqrt == 0:
            if N / sqrt == sqrt:
                factors += 1
            else:
                factors += 2
        sqrt -= 1
    return factors

if __name__ == '__main__':
    N = 25
    print solution(N)

# java version
# class Solution {
#     public int solution(int N) {
#         if (N == 1)
#             return 1;
#         int sqrt = (int)(Math.sqrt(N));
#         int factors = 2;
#         while (sqrt > 1){
#             if (N % sqrt == 0){
#                 if (N / sqrt == sqrt)
#                     factors += 1;
#                 else
#                     factors += 2;
#             }
#             sqrt -=1;
#         }
#         return factors;
#     }
# }