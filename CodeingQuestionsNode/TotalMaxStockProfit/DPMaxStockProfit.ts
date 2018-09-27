import * as minMaxProfit from ".././MaxStockProfit/minMaxProfit";

export interface TransactionItem{
    buyPrise: number,
    sellPrise: number,
    profit: number,
}

export interface TransactionList{
    transactions: Array<TransactionItem>;
}

export let getMaxProfit = (prices: Array<number>) => {
    let results: TransactionList;
    var singleTransactionProgit = minMaxProfit.getMaxProfit(prices);
    var buyPos = 0;
    var profitsChart = getProfitsChart(prices[buyPos], prices.slice(buyPos + 1));
    console.log(profitsChart);




    results = <TransactionList>{
        transactions: new Array<TransactionItem>(singleTransactionProgit)
    }
    return results;
};

let getProfitsChart = (buyPrice: number, prices: Array<number>) => {
    var profitsChart = [];
    for (var i = 0; i < prices.length; i++){
        var profitNow = prices[i] - buyPrice;
        profitNow = profitsChart.length <= 0 || profitNow > profitsChart[profitsChart.length - 1] ? profitNow : profitsChart[profitsChart.length - 1]
        profitsChart.push(profitNow);
    }

    return profitsChart;
}