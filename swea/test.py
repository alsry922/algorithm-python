T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
def countNumber(originNumber):
    if originNumber // 10 == 0:
        numberList[originNumber] += 1
        return

    remains = originNumber % 10
    numberList[remains] += 1
    countNumber(originNumber // 10)

def findMaxDigit(numList):
    maxNumberOfRepeat = max(numList)
    maxNumberList = []
    for i in range(len(numList)):
        if numList[i] == maxNumberOfRepeat:
            maxNumberList.append(i)
    
    return max(maxNumberList), maxNumberOfRepeat

for test_case in range(1, T + 1):
    theNumOfCard = int(input())
    number = int(input())
    numberList = [0] * 10
    
    countNumber(number)
    maxNumber, repeatCount = findMaxDigit(numberList)
    print(f'#{test_case}{maxNumber} {repeatCount}')

