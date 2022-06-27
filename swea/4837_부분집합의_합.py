# import sys

# sys.stdin = open("sample.txt", "r")

# T = int(sys.stdin.readline())
T = int(input())

lst = [1,2,3,4,5,6,7,8,9,10,11,12]

for test_case in range(1, T+1):
    # theNumOfEle, subsetSum = map(int, sys.stdin.readline().split())
    theNumOfEle, subsetSum = map(int, input().split())
    subsetList = [] # 부분집합 리스트
    count = 0 # 각 부분집합의 합이 subsetSum과 일치하는 경우의 수

    for i in range((1<<3)-1, (1<<len(lst))):
        countEle = 0 # 부분집합 원소의 갯수
        temp = []
        for j in range(len(lst)):
            if i & (1<<j):
                countEle += 1
                if countEle > theNumOfEle: # 부분집합 원소의 갯수가 theNumOfEle개를 넘어갈 때
                    break
                temp.append(lst[j])
        if countEle == theNumOfEle: # 부분집합 원소의 갯수가 theNumOfEle개일 때 subsetList에 추가
            subsetList.append(temp)
    

    for i in range(len(subsetList)):
        if sum(subsetList[i]) == subsetSum:
            count += 1
    print(f'#{test_case} {count}')