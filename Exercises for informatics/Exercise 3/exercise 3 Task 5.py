height = 1.8
weight = 80

bmi_number = (weight / (height**2))
def get_bmi_category():
    if height < 0 or weight < 0:
        bmi = "N/A"
    elif 0 <= bmi_number <= 18.5:
        bmi = "BMI: {:.2f}".format(bmi_number) + ", Category: Underweight"
    elif 18.5 < bmi_number <= 25:
        bmi = "BMI: {:.2f}".format(bmi_number) + ", Category: Normal weight"
    elif 25 < bmi_number <= 30:
        bmi = "BMI: {:.2f}".format(bmi_number) + ", Category: Pre-obesity"
    elif 30 < bmi_number <= 35:
        bmi = "BMI: {:.2f}".format(bmi_number) + ", Category: Obesity Class I"
    elif 35 < bmi_number <= 40:
        bmi = "BMI: {:.2f}".format(bmi_number) + ", Category: Obesity Class II"
    else:
        bmi = "BMI: {:.2f}".format(bmi_number) + ", Category: Obesity Class III"
    return bmi
print(get_bmi_category())
