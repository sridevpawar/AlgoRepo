import * as solveWordBoggle from "./solveWordBoggle";

module CodeingQuestionsNode {
    let dictionary = ['geeks', 'for', 'quiz', 'go'];
    let boggle = [['g', 'i', 'z'], ['u', 'e', 'k'], ['q', 's', 'e']];
    console.log(solveWordBoggle.solve(dictionary, boggle));
}