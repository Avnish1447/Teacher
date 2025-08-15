def arrivalLine():
    n = int(input())
    CurrentLine = list(map(int, input().split()))
    
    maxHeight = max(CurrentLine)
    minHeight = min(CurrentLine)

    indexMaxHeight = CurrentLine.index(maxHeight)
    
    indexMinHeight = 0
    for i in range(n-1,-1,-1):
        if CurrentLine[i] == minHeight:
            indexMinHeight = i
            break

    swapForMax = indexMaxHeight
    swapForMin = (n-1)-indexMinHeight
    totalSwaps = swapForMin+swapForMax

    if indexMaxHeight > indexMinHeight:
        totalSwaps = totalSwaps-1

    print(totalSwaps)
arrivalLine()