print("Enter talents:")
talent=float(input())
print("Enter pounds:")
pound=float(input())
print("Enter lots:")
lot=float(input())
lot2=lot*13.3
pound2=pound*32*13.3
talent2=talent*20*32*13.3
gram=lot2+pound2+talent2
kilogram=gram//1000
gram2=gram%1000
print(f"{kilogram} kilograms, {gram2} grams")