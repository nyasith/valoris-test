import services.profile as service

def createloan(data):
    nric = data['nric']
    pw = data['password']
    res = service.createloan(nric, pw)
    return res

def updatelogin(data):
    nric = data['nric']
    displayName = data['displayName']
    hobbies = data['hobbies']
    res = service.login(nric, displayName, hobbies)     
    return res