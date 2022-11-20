
import services.loan as service

def createloan(data):
    id = data['id']
    full_name = data['full_name']
    dob = data['dob']
    nric = data['nric']
    old_nric = data['old_nric']
    gender = data['gender']
    nation = data['nation']
    religion = data['religion']
    citizenship = data['citizenship']
    marital_status = data['marital_status']
    phone_home = data ['phone_home']
    phone_mobile = data ['phone_mobile']
    email = data['email']
    agency_help = data['agency_help']
    monthly_income = data['monthly_income']
    high_edu_institution = data['high_edu_institution']
    study_level = data['study_level']
    year_of_study = data['year_of_study']
    health_status = data['health_status']
    disabled_status = data['disabled_status']
    bankruptcy_status = data['bankruptcy_status']
    disabilities = data['disabilities']
    work_status = data['work_status']
    vulnerable_groups = data['vulnerable_groups']
    program1 = data['program1']
    program2 = data['program2']
    permanent_address = data['permanent_address']
    permanent_city = data['permanent_city']
    permanent_zip_code = data['permanent_zip_code']
    permanent_state = data['permanent_state']
    mail_address = data['mail_address']
    res = service.createloan(id,full_name,dob,nric,old_nric,gender,nation,religion,citizenship,marital_status,phone_home,
                                 phone_mobile,email,agency_help,monthly_income,high_edu_institution,study_level,year_of_study
                                 ,health_status,disabled_status,bankruptcy_status,disabilities,work_status,vulnerable_groups,
                                 program1,program2,permanent_address,permanent_city,permanent_zip_code,permanent_state,mail_address)
    return res

def getloandetails(nric):
    res = service.getloandetails(nric)
    return res


    