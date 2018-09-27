export class LetterPosition{
    row: number;
    col: number;
    constructor(row: number, col: number){
        this.col = col;
        this.row = row;
    }
}

export let solve = (dictionary: Array<string>, boggle: Array<Array<string>>): Array<string> => {
    let result = new Array<string>();
    dictionary.forEach((element: string) => {
        if(checkWordInBoggle(element, boggle)){
            result.push(element);
        }
    });

    return result;
}

let checkWordInBoggle = (word: string, boggle: Array<Array<string>>) => {
    let result = true;
    let currentLetterPos: LetterPosition = <LetterPosition>{
        row: null,
        col: null
    };

    word.split("").forEach((letter: string) => {
        if(!result)return;
        var resultPos = checkAdjacentOrPresent(currentLetterPos, letter, boggle);
        if(resultPos == null){
            result = false;
        } else {
            currentLetterPos = resultPos;
        }
    });

    return result;
}

let checkAdjacentOrPresent = (letterPosition: LetterPosition, letter: string, boggle: Array<Array<string>>): LetterPosition => {
    let result = null;
    if (letterPosition.row == null && letterPosition.col == null){
        boggle.forEach((element: Array<string>, indexBoggle: number) => {
            var letterIndex = element.indexOf(letter);
            if (letterIndex >= 0 && result == null){
                result = new LetterPosition(indexBoggle, letterIndex);
            }
        });

        return result;
    }

    // Top
    if (letterPosition.row > 0){
        if (boggle[letterPosition.row - 1][letterPosition.col] == letter){
            return new LetterPosition(letterPosition.row - 1, letterPosition.col);
        }
    }

    //Bottom
    if (letterPosition.row < boggle.length - 1){
        if (boggle[letterPosition.row + 1][letterPosition.col] == letter){
            return new LetterPosition(letterPosition.row + 1, letterPosition.col);
        }
    }

    //Right
    if (letterPosition.col < boggle[letterPosition.row].length - 1){
        if (boggle[letterPosition.row][letterPosition.col + 1] == letter){
            return new LetterPosition(letterPosition.row, letterPosition.col + 1);
        }
    }

    //Left
    if (letterPosition.col > 0){
        if (boggle[letterPosition.row][letterPosition.col -1 ] == letter){
            return new LetterPosition(letterPosition.row, letterPosition.col - 1);
        }
    }

    //RightUp
    if (letterPosition.row > 0 && letterPosition.col < boggle[letterPosition.row].length - 1){
        if (boggle[letterPosition.row - 1][letterPosition.col + 1] == letter){
            return new LetterPosition(letterPosition.row - 1, letterPosition.col + 1);
        }
    }

    //RightDown
    if (letterPosition.row < boggle.length - 1 && letterPosition.col < boggle[letterPosition.row].length - 1){
        if (boggle[letterPosition.row + 1][letterPosition.col + 1] == letter){
            return new LetterPosition(letterPosition.row + 1, letterPosition.col + 1);
        }
    }

    //LeftUp
    if (letterPosition.col > 0 && letterPosition.row > 0){
        if (boggle[letterPosition.row - 1][letterPosition.col -1 ] == letter){
            return new LetterPosition(letterPosition.row - 1, letterPosition.col - 1);
        }
    }

    //LeftDown
    if (letterPosition.col > 0 && letterPosition.row < boggle.length - 1){
        if (boggle[letterPosition.row + 1][letterPosition.col -1 ] == letter){
            return new LetterPosition(letterPosition.row + 1, letterPosition.col - 1);
        }
    }

    return null;
}