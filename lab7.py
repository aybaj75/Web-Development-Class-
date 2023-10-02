#Ayaan Bajwa
#Student ID: 100864399
#Lab 7 OOP

class BasicCalculator:
    
    def addition(self, a,b):
        return a+b
    
    def subtraction(self, a,b):
        return a-b
    
    def multiplication(self, a,b):
        return a*b
    
    def division(self, a,b):
        return a/b
    
class AdvancedCalculator(BasicCalculator):
    def addition(self, a,b):
        try:
            final = super().addition(a,b)
        except TypeError:
            print("Invalid Input! Please enter number only.")
            
        else: 
            print(f"{a} + {b} = {final}")
        return final
    
    def subtraction(self,a, b):
        try:
            final = super().subtraction(a,b)
        except TypeError:
            print("Invalid Input! Please enter number only.")
            
        else:
            print(f"{a} - {b} = {final}")
        return final
    
    def multiplication(self, a,b):
        try:
            final=super().multiplication(a,b)
        except TypeError:
            print("Invalid Input! Please enter number only.")
            
        else:
            print(f"{a} * {b} = {final}")
        return final
    
    def division(self, a, b):
        try:
            final=super().division(self,a,b)
        except TypeError:
            print("Invalid Input! Please enter number only.")
            
        else:
            print(f"{a} / {b} = {final}")
        return final
    
def main():
    calc = AdvancedCalculator()
    opo = []

    while True:
        try:
            op = input("Enter an operation (addition(+), subtraction(-), multiplication(*), division(/)): ")
            
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if op == '+':
                final = calc.addition(a, b)
            if op == 'addition':
                final = calc.addition(a,b)
            if op == '-':
                final = calc.subtraction(a, b)
            if op == 'subtraction':
                final = calc.subtraction(a,b)
            if op == '*':
                final = calc.multiplication(a, b)
            if op == 'multiplcation':
                final = calc.multiplication(a,b)
            if op == '/':
                final = calc.division(a,b)
            elif op == 'division':
                final = calc.division(a,b)

            opo.append(f"{a} {op} {b} = {final}")
            print(f"{a} {op} {b} = {final}")

            more_ops = input("Do you want to perform another operation? (yes/no): ")
            if more_ops.lower() != "yes":
                break
        except ValueError:
            print("Error has occurred")
        except Exception:
            print("error has occurred")

    print("\n Operations performed:\n" + "\n".join(opo)) 
    
main()
    
     