changingParam = ['Red_Blood_Cells','Hypertension']
changingValues = [['Not Present','Present'],['No','Yes']]

def generateProfile(data):
    Person_Profile = []
    for x in data:
        if x in changingParam:
            X_index = changingParam.index(x)
            newStrings = x.replace('_'," ") + '  :  ' + changingValues[X_index][int(data[x])]
        else:
            newStrings = x.replace('_'," ") + '  :  ' + data[x]
        Person_Profile.append(newStrings)
    print(Person_Profile)
    return Person_Profile

def generateOutput(prediction):
    base = 'From the given profile our model has predicted : '
    choice = ['The person does not have Chronic Kidney Disease','The person does have Chronic Kidney Disease']
    
    return base + choice[prediction]