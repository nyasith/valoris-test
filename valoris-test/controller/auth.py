import services.auth as service

def create_user(data):
    id = data ['id']
    nric = data['nric']
    phone = data['phone']
    email = data['email']
    password = data['password']
    record_date = data ['record_date']
    otp = data ['otp']
    res = service.create_user(id, nric, record_date,phone,email,password,otp)
    return res

def insert_user(data):
    #id = data ['id']
    nric = data['nric']
    phone = data['phone']
    email = data['email']
    password = data['password']
    record_date = data ['record_date']
    otp = data ['otp']
    res = service.insert_user( nric, record_date,phone,email,password,otp)
    return res