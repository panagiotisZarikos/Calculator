class Math:
  def add(x,y):
    return x + y
  def subtract(x,y):
    return x - y 
  def multiply(x,y):
    return x * y 
  def divide(x,y):
    return x / y
    pass

print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
while True: 
 num_choice = input("Select one of these numbers ")
 if num_choice in {"1","2","3","4"}:
    break
    
     
 else:
    print("Invalid input, try again")





num1 = float(input("Your first number "))
num2 = float(input("Your second number "))           
if num_choice == "1":
  print(num1,"+",num2,"=",Math.add(num1,num2))
elif num_choice == "2":
  print(num1,"-",num2,"=",Math.subtract(num1,num2))
elif num_choice == "3":
  print(num1,"*",num2,"=",Math.multiply(num1,num2))
elif num_choice == "4":
  try:
   print(num1,"/",num2,"=",Math.divide(num1,num2))
  except ZeroDivisionError:
    print("You cannot divide by 0")
  
  

  



  
