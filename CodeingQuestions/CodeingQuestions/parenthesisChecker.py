from myStack import myStack

def parenthesisChecker(str):
    parenthesis = {
        "[": {"type" : 1, "state": "open"},
        "]": {"type" : 1, "state": "close"},
        "{": {"type" : 2, "state": "open"},
        "}": {"type" : 2, "state": "close"},
        "(": {"type" : 3, "state": "open"},
        ")": {"type" : 3, "state": "close"},
        }
    stack = myStack(len(str))
    for s in str:
        if s in parenthesis:
            if parenthesis[s]["state"] == "open":
                stack.push(s)
            elif parenthesis[s]["state"] == "close":
                lastP = stack.pop()
                if parenthesis[lastP]["type"] != parenthesis[s]["type"] or parenthesis[lastP]["state"] == parenthesis[s]["state"]:
                    return "Not balanced"

    if stack.isEmpty():
        return "Balanced"
    else:
        "Not balanced"



str = "[(])"
print(parenthesisChecker(str))