export interface TransactionItem{
    buyPrise: number,
    sellPrise: number,
    profit: number,
}

export interface TransactionPointer{
    buyPos: number,
    sellPos: number,
    profit: number,
}

export interface TransactionList{
    transactions: Array<TransactionItem>;
}

export let getMaxProfit = (prices: Array<number>): TransactionList => {
    let transactionPointer: TransactionPointer;
    let pricesToCheck = prices;
    let results: TransactionList = <TransactionList>{
        transactions: new Array<TransactionItem>()
    };
    
    while(pricesToCheck.length > 1){
        transactionPointer = getFirstProfit(pricesToCheck);
        results.transactions.push(<TransactionItem>{
            buyPrise: pricesToCheck[transactionPointer.buyPos],
            sellPrise: pricesToCheck[transactionPointer.sellPos],
            profit: transactionPointer.profit
        });
        pricesToCheck = pricesToCheck.slice(transactionPointer.sellPos + 1);
    }
    
    return results;
}

let getFirstProfit = (pricesToCheck: Array<number>) => {
    let buyPos;
    let sellPos;
    for(var i = 0; i < pricesToCheck.length; i++){
        if(pricesToCheck[i] < pricesToCheck[i + 1]){
            buyPos = i;
            break;
        }
    }

    var prev = pricesToCheck[buyPos + 1];
    for(i = buyPos + 2; i < pricesToCheck.length; i++){
        if(pricesToCheck[i] < prev){
            sellPos = i - 1;
            break;
        }

        prev = pricesToCheck[i];
    }

    if(!sellPos)
    {
        sellPos = pricesToCheck.length - 1;
    }

    return <TransactionPointer>{
        buyPos: buyPos,
        sellPos: sellPos,
        profit: pricesToCheck[sellPos] - pricesToCheck[buyPos]
    }
}