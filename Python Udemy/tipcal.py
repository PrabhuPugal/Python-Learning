total_amount=input("Enter the total amount spent: ")
tip_per=input("Enter the percent of tip you want to give:\n1)10\n2)12\n3)15\n")
total_pers=input("Total people ate: ")
tip_amount=float(total_amount)*float(tip_per)/100
final_amt=float(total_amount)+tip_amount
share=final_amt/int(total_pers)
print("Each person's share: ",round(share,2))