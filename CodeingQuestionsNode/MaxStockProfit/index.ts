import * as minMaxProfit from "./minMaxProfit";
import * as assumeFirst from "./assumeFirst";
import * as chnageArray from "./chnageArray";

module CodeingQuestionsNode {
    let stockPrices = [100, 180, 260, 310, 40, 535, 695];
    console.log('///////////////////////////////////////////////////////////////////////////////////////');
    console.log('stockPrices: ' + stockPrices);
    console.log('--------------------------------minMaxProfit-----------------------------------------------');
    let minMaxProfitResult: minMaxProfit.TransactionItem = minMaxProfit.getMaxProfit(stockPrices);
    console.log('BuyPrice: ' + minMaxProfitResult.buyPrise);
    console.log('SellPrise: ' + minMaxProfitResult.sellPrise);
    console.log('Profit: ' + minMaxProfitResult.profit);
    console.log('--------------------------------assumeFirst-----------------------------------------------');
    let assumeFirstResult: minMaxProfit.TransactionItem = assumeFirst.getMaxProfit(stockPrices);
    console.log('BuyPrice: ' + assumeFirstResult.buyPrise);
    console.log('SellPrise: ' + assumeFirstResult.sellPrise);
    console.log('Profit: ' + assumeFirstResult.profit);
    console.log('--------------------------------chnageArray-----------------------------------------------');
    let chnageArrayResult: minMaxProfit.TransactionItem = chnageArray.getMaxProfit(stockPrices);
    console.log('BuyPrice: ' + chnageArrayResult.buyPrise);
    console.log('SellPrise: ' + chnageArrayResult.sellPrise);
    console.log('Profit: ' + chnageArrayResult.profit);
    console.log('///////////////////////////////////////////////////////////////////////////////////////');
}