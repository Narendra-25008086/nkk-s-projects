print("VOLTING ELIGIBILITY CHECKER!")
while "naren":
  a=int(input("Enter your age: ")) 
  b=input("Enter ur nationality: ")
  if a>=18 and b=="indian":
    print("You are eligible for voting")
  else:
    print("You are not eligible for voting")
    w=input("you want to test again? (yes/no): ")
    if w.lower()=="no":
      break