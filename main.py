import turtle
mWindow = turtle.Screen()

mPen = turtle.Pen()
mPen.pensize(1)
mPen.speed(1)
mPen.right(90)
print("Initial heading: {}".format(mPen.heading()))

class Instruction:
    def __init__(self, operation, choice):
        self.operation = operation
        self.choice = choice
        
    def print_operation(self):

        listOfOperations = {
                    'P' : 'Select pen',
                    'U' :  'Pen up',
                    'D' :  'Pen down',
                    'W' :  'Draw west',
                    'N' :  'Draw north',
                    'E' :  'Draw east',
                    'S' :  'Draw south'
                }

        return listOfOperations.get(self.operation, 'Unknown operation')

    def execute(self):
        if operation == 'W':
            mPen.setheading(270)
            mPen.right(90)
            mPen.forward(self.choice)
        elif operation == 'N':
            mPen.setheading(0)
            mPen.left(90)
            mPen.forward(self.choice)
        elif operation == 'E':
            mPen.setheading(90)
            mPen.right(90)
            mPen.forward(self.choice)
        elif operation == 'S':
            mPen.setheading(180)
            mPen.left(90)
            mPen.forward(self.choice)
        elif operation == 'U':
            mPen.penup()
        elif operation == 'D':
            mPen.pendown()
        
        
# Read and parse instructions
with open('draw_instructions') as reader:
    line = reader.readline()
    cntr = 1
    while line:
        operation = line[0]
        choice = line[2]
        if choice.isdigit():
            instruction = Instruction(operation, float(choice) * 100)
            if operation != "P" and mPen.isdown():
                print("Operation {}: {} {} pixels".format(cntr, instruction.print_operation(), float(choice) * 100))
                mPen.write("{} {}".format(instruction.print_operation(), instruction.choice), False, "right", ("Arial", 12, "normal"))            
        else:
            instruction = Instruction(operation, 0)
            print("Operation {}: {}".format(cntr, instruction.print_operation(), ))
        
        instruction.execute()
        
        # move cursor to next line
        line = reader.readline()
        cntr += 1


mWindow.exitonclick()