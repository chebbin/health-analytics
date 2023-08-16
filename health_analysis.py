import pandas as pd
import numpy as np
# this is the number variable
age = 50
print(age)

## this is the string variable
name = ('Chevi')
print(name)

### this is the list
work_places = ['hospital', 'subacute rehab', 'outpatient clinic', 'home care']
print(work_places)

#### this is the dictionary
education = {
    'high school' : 'Beth Jacob',
    'universities' : ['Brooklyn College', 'Hunter College', 'NYU', 'Stony Brook University'],
    'degrees' : {
    'undergraduate' : 1995,
    'masters' : 2002,
    'second masters' : 'not yet completed'
    }
}
print(education)



##### This is the function 
def cholesterolChecker(ldl, hdl):
    total_chol_output = ldl + hdl
    print('Your total cholesterol is: ', total_chol_output)

    if total_chol_output < 200:
        print('Your cholesterol numbers are within the normal range')
    else:
        print('Your cholesterol numbers are too high')
    
    return total_chol_output     
    

patients = [
    [99, 40],
    [160, 35],
    [80, 60],
    [175, 30],
    [240, 30]
]


for x in patients:
    print('\n')
    print(f'Now analyzing data: ldl: {x[0]}, hdl: {x[1]}')
    ldl = x[0]
    hdl = x[1]
    print('total cholesterol: ', cholesterolChecker(ldl, hdl))



