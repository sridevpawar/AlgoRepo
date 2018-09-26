export interface TransactionItem{
    buyPrise: number,
    sellPrise: number,
    profit: number,
}

export let getMaxProfit = (prices: Array<number>): TransactionItem => {
    // pretty much the same as minMaxProfit so will skip
    return <TransactionItem>{
        profit: prices[0]
    };
}