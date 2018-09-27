import * as dpMaxStockProfit from "./DPMaxStockProfit";
import * as runnerTotalMaxStockProfit from "./RunnerTotalMaxStockProfit";

let printResutls = (name: string, moduleToUse: any, prices: Array<number>) => {
    console.log('------------------------' + name + '-------------------------------------');
    let stockProfitResult: dpMaxStockProfit.TransactionList = moduleToUse.getMaxProfit(prices);
    stockProfitResult.transactions.forEach(element => {
        console.log('*******************************Transaction Start************************************');
        console.log('BuyPrice: ' + element.buyPrise);
        console.log('SellPrise: ' + element.sellPrise);
        console.log('Profit: ' + element.profit); 
        console.log('******************************Transaction End**********************************');
    });
    console.log('////////////////////////////////////////////////////////////////////////////////');
}

module CodeingQuestionsNode {
    //let stockPrices = [100, 180, 260, 310, 40, 535, 695];
    //let stockPrices = [100, 200, 180, 135, 235, 400, 255];
    //let stockPrices = [100, 98, 87, 75, 65, 50, 45];
    let stockPrices = [44, 32, 45, 25, 23, 35, 46, 58, 69, 72, 85, 84, 152, 88, 75, 66, 55, 85, 96, 103];
    console.log('//////////////////////////////////////////////////////////////////////////');
    console.log('stockPrices: ' + stockPrices);
    //printResutls('DPMaxStockProfit', dpMaxStockProfit, stockPrices);
    printResutls('RunnerTotalMaxStockProfit', runnerTotalMaxStockProfit, stockPrices)
}