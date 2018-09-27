export interface TransactionItem{
    buyPrise: number,
    sellPrise: number,
    profit: number,
}

export let getMaxProfit = (prices: Array<number>) => {
    var min = prices[0];
    var max = 0;
    let result: TransactionItem = {
        profit: 0,
        buyPrise: 0,
        sellPrise: 0
    };
    prices.forEach(price => {
        if (price < min){
            min = price;
            max = 0;
        }

        if (price > max && price > min){
            max = price;
        }
        
        if (max > 0){
            if (result.profit < max - min){
                result = <TransactionItem>{
                    buyPrise: min,
                    sellPrise: max,
                    profit: max - min
                }
            }
        }
    });

    return result;
}