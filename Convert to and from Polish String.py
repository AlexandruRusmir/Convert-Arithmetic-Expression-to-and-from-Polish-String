class Stack():
    def __init__(self):
        self.items = list()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items


#Arithmetic operators priorities
priority = {
    "+" : 1,
    "-" : 1,
    "*" : 2,
    "/" : 2
}


def toPolishString(expression):
    s = Stack() #Operators stack

    ps = ""
    for el in expression:
        if el not in priority:
            if el == "(":
                s.push(el)
                
            elif el == ")":
                s.push(el)
                print(s.get_stack())
                s.pop()
                while s.peek() != "(":
                    ps = ps + s.peek()
                    s.pop()
                s.pop()
                
            else:
                ps = ps + el

                
        else:
            if s.is_empty():
                s.push(el)

            elif s.peek() == "(":
                s.push(el)
            
            elif priority[s.peek()] < priority[el]:
                s.push(el)
                
            else:
                if s.peek() == "(":
                    s.push(el)
                    
                else:
                    print(s.get_stack(), end = " ")
                    print("The last element is bothered by: " + el)
                    ps = ps + s.peek()
                    s.pop()
                    s.push(el)

    print("Remaining elements from the stack: ", end = " ")
    print(s.get_stack())
    while not s.is_empty():
        ps = ps + s.peek()
        s.pop()
    
    return ps


def fromPolishString(ps):
    s = Stack() #Operands stack
    
    for el in ps:
        if el not in priority:
            s.push(el)

        else:
            print(s.get_stack(), end = " ")
            print("Operator to introduce: ", end = " ")
            print(el)
            new_operand = ""
            operand2 = s.peek()
            s.pop()
            operand1 = s.peek()
            s.pop()

            if priority[el] == 1:
                new_operand = operand1 + el + operand2
                s.push(new_operand)

            else:
                if ("+" in operand1) or ("-" in operand1):
                    new_operand = "(" + operand1 + ")" + el
                else:
                    new_operand = operand1 + el

                if ("+" in operand2) or ("-" in operand2):
                    new_operand += "(" + operand2 + ")"
                else:
                    new_operand += operand2

                s.push(new_operand)
    end = s.peek()
    return end

expression = input()
ps = toPolishString(expression)
print(ps)
print()
expression = fromPolishString(ps)
print(expression)
