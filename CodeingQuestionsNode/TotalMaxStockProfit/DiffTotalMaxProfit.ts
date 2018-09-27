export interface TransactionItem{
    buyPrise: number,
    sellPrise: number,
    profit: number,
}

export interface TransactionList{
    transactions: Array<TransactionItem>;
}

export let getMaxProfit = (prices: Array<number>): TransactionList => {
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
    for(var i = 0; i < diff.length; i++){
        if(diff[i] > 0){
            
        }
    }

    let results: TransactionList;
    results = <TransactionList>{
        transactions: new Array<TransactionItem>(<TransactionItem>{
            profit:0
        })
    };
    return results;
}