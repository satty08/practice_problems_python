def findMaxProfit(numOfPredictedDay, predictedSharePrices):
    # Participants code will be here
    buyingPrice = min(predictedSharePrices)
    j = 0
    for i in range(numOfPredictedDay):
        if predictedSharePrices[i] == buyingPrice:
            j = i
            break
    print(j)
    sellingPrice = max(predictedSharePrices[j:])
    print(sellingPrice)
    if sellingPrice > buyingPrice:
        return sellingPrice - buyingPrice
        
    return -1

predictedShare = [100, 10, 12, 5, 6, 14, 5, 6]
num = 8

print(findMaxProfit(num, predictedShare))