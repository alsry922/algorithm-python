# import sys

# sys.stdin = open('sample.txt', 'r')
# The number of test cases
T = int(input())
# T = int(sys.stdin.readline())

for test_cases in range(1, T+1):
    # The number of integer and the number will be added up
    num_of_int, count_num = list(map(int, input().split()))
    # num_of_int, count_num = list(map(int, sys.stdin.readline().split()))
    # Make an array with numbers provided
    lst = list(map(int, input().split()))
    # lst = list(map(int, sys.stdin.readline().split()))

    minimum, maximum = sum(lst[0:count_num]), sum(lst[0:count_num])
    result = 0
    index = 0
    
    while(index + count_num <= len(lst)):
        part = lst[index:index+count_num]
        total = sum(part)
        if total <= minimum:
            minimum = total
        elif total >= maximum:
            maximum = total
        index += 1
        

    result = maximum - minimum
    
    print(f'#{test_cases} {result}')
    