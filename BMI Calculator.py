height = input("Enter your height in m ? ")
weight = input("Enter your weight in kg ? ")
bmi_height = float(height)
bmi_weight = float(weight)

def bmi(w_b,h_b):
     return round(w_b/h_b**2,2)
     
print(bmi(bmi_weight,bmi_height))

