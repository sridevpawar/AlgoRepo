export interface TransactionItem{
    buyPrise: number,
    sellPrise: number,
    profit: number,
}

export let getMaxProfit = (prices: Array<number>): TransactionItem => {
    let computeDiff = (prices: Array<number>): Array<number> => {
        let result: Array<number> = Array<number>();
        let prev: number = null;
        prices.forEach((price: number) => {
            if (prev === null){
                prev = price;
                return;
            }

            result.push(price - prev);
            prev = price;
        });

        return result;
    }

    let diff: Array<number> = computeDiff(prices);
    let rSum: number = -1;
    let maxSum: number = -1;
    console.log(diff);
    diff.forEach((priceChange: number) => {
        rSum = rSum + priceChange;
        
        if (rSum < 0){
            rSum = 0
        }

        if (rSum > maxSum){
            maxSum = rSum;
        }
    });

    return <TransactionItem>{
        profit: maxSum
    };
}