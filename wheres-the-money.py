'''
This program uses functions to create a 'wheres the money' chart
'''
def calculate_tax(annual_salary):
    """
    Converts yearly salary into a tax. 

    Args: 
    annual_salary (int): total salary per year
   
    Returns:
    int: total tax amount in dollars
    """
    if annual_salary >= 0 and annual_salary <= 15000:
        tax_percentage = 10
        return annual_salary * ( tax_percentage / 100.0)
    elif annual_salary > 15000 and annual_salary <= 75000:
        tax_percentage = 20
        return annual_salary * ( tax_percentage / 100.0)
    elif annual_salary > 75000 and annual_salary <= 200000:
        tax_percentage = 25
        return annual_salary * ( tax_percentage / 100.0)
    elif annual_salary > 200000:
        tax_percentage = 30
        return annual_salary * ( tax_percentage / 100.0) 
    
def wheres_the_money(salary, rent, bills, food, travel):
    """
    Converts salary into an organized financial chart

    Args: 
    salary: total income per year
    rent: total rent per month
    bills: total bills per month
    food: total food per week
    travel: total travel per year

    Returns:
    str: An organized chart showing the breakdown of each arg.
    """
    tax = calculate_tax(salary)

    #Checks if the calc tax function output is more than 75k. 
    #If output is more than 75k, then it sets tax to 75k. 
    if calculate_tax(salary) >= 75000:
        tax = 75000

    extra = (salary)-(rent*12+bills*12+food*52+travel+tax)
    rentp = (rent*12/salary)*100
    billsp = (bills*12/salary)*100
    foodp = (food*52/salary)*100
    travelp = (travel/salary)*100
    taxp = (tax/salary)*100
    extrap = (extra/salary)*100

    renth = (int(rentp))*"#"
    billsh = (int(billsp))*"#"
    foodh = (int(foodp))*"#"
    travelh = (int(travelp))*"#"
    taxh = (int(taxp))*"#"
    extrah = (int(extrap))*"#"


    blength = len("| mortgage/rent | ${:8,.2f} | {:>5.1f}% | ")
    m = rentp
    
    #Checks if the all previous variables are greater than rentp
    #If they are, then it sets m to the greatest variable
    #To create an integter to create the seperator bar
    if billsp > m:
        m = billsp
    if foodp > m:
        m = foodp
    if travelp > m:
        m = travelp
    if taxp > m:
        m = taxp
    if extrap > m:
        m = extrap

    s = '-' * int(blength + int(m))

    isalary = str(salary)
    
    chart= ""
    chart+=(s + "\n")
    chart+=(
        "See the financial breakdown below, "
        "based on a salary of $"+isalary+"\n"
        )
    chart+=(s + "\n")
    chart+=(
        "| mortgage/rent | $ {:10,.2f} | {:5.1f}% | {}\n"
        .format(rent*12,rentp,renth)
        )
    chart+=(
        "|         bills | $ {:10,.2f} | {:5.1f}% | {}\n"
        .format(bills*12,billsp,billsh)
        )
    chart+=(
        "|          food | $ {:10,.2f} | {:5.1f}% | {}\n"
        .format(food*52,foodp,foodh)
        )
    chart+=(
        "|        travel | $ {:10,.2f} | {:5.1f}% | {}\n"
        .format(travel,travelp,travelh)
        )
    chart+=(
        "|           tax | $ {:10,.2f} | {:5.1f}% | {}\n"
        .format(tax,taxp,taxh)
        )
    chart+=(
        "|         extra | $ {:10,.2f} | {:5.1f}% | {}\n".
        format(extra,extrap,extrah)
        )
    chart+=(s)

    print(chart)

    #Checks if the extra amount is less than 0 and prints a warning.
    if extra < 0:
        print(">>> WARNING: DEFICIT <<<")

    #Checks if tax is greater then 75k and prints a limit. 
    if tax >= 75000:
        print(">>> TAX LIMIT REACHED <<<")

def main():
    calculate_tax(150000)
    wheres_the_money(150000, 1500, 500, 300, 1000)
main()
