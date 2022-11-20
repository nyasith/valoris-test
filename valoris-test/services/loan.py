import random
from db import get_db
from flask import jsonify, make_response

# status [draft - 0, submitted - 1, Send for approval - 9, Approved 49, disapproved - 99]
# def insert_loans(fullname, dob, nric, oldNric, gender, nation, religion, citizenship, maritalStatus, phoneHome, phoneMobile, email, agencyHelp, monthlyIncome, highEduInstitution, studyLevel, yearsOfStudy, healthStatus, disabledStatus, bankruptcyStatus, disabilities, workStatus, vulnerableGroups, program1, program2, add1, add2, add3, permanentCity, permanentZipCode, permanentState, madd1, madd2, madd3, mailCity, mailZipCode, mailState, guarantee1, guarantee2, gName1, gNric1, gBankruptcyStatus1, gDebtStatus1, gPhone1, gPhoneVeriDate1, gMail1, gMailVeriDate1, status1, gName2, gNric2, gBankruptcyStatus2, gDebtStatus2, gPhone2, gPhoneVeriDate2, gMail2, gMailVeriDate2, status2):
#     db = get_db()
#     cursor = db.cursor()
#     statement = "INSERT INTO loans (fullname, dob, nric, oldNric, gender, nation, religion, citizenship, maritalStatus, phoneHome, phoneMobile, email, agencyHelp, monthlyIncome, highEduInstitution, studyLevel, yearsOfStudy, healthStatus, disabledStatus, bankruptcyStatus, disabilities, workStatus, vulnerableGroups, program1, program2, add1, add2, add3, permanentCity, permanentZipCode, permanentState, madd1, madd2, madd3, mailCity, mailZipCode, mailState, guarantee1, guarantee2, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
#     cursor.execute(statement, [fullname, dob, nric, oldNric, gender, nation, religion, citizenship, maritalStatus, phoneHome, phoneMobile, email, agencyHelp, monthlyIncome, highEduInstitution, studyLevel, yearsOfStudy, healthStatus, disabledStatus,
#                    bankruptcyStatus, disabilities, workStatus, vulnerableGroups, program1, program2, add1, add2, add3, permanentCity, permanentZipCode, permanentState, madd1, madd2, madd3, mailCity, mailZipCode, mailState, guarantee1, guarantee2, '1'])
#     db.commit()
#     statement = "INSERT INTO guarantees (gName, gNric, gBankruptcyStatus, gDebtStatus, gPhone, gPhoneVeriDate, gMail, gMailVeriDate, status, gNo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
#     cursor.execute(statement, [gName1, gNric1, gBankruptcyStatus1, gDebtStatus1,
#                    gPhone1, gPhoneVeriDate1, gMail1, gMailVeriDate1, status1, 1])
#     db.commit()
#     statement = "INSERT INTO guarantees (gName, gNric, gBankruptcyStatus, gDebtStatus, gPhone, gPhoneVeriDate, gMail, gMailVeriDate, status, gNo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
#     cursor.execute(statement, [gName2, gNric2, gBankruptcyStatus2, gDebtStatus2,
#                    gPhone2, gPhoneVeriDate2, gMail2, gMailVeriDate2, status2, 2])
#     db.commit()
#     data = cursor.fetchone()
#     return make_response(jsonify({"message": "Loan details added successfully", "data": data, "error": "0", "meta": None}), 200)

def remove_loan_draft(nric):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM loans WHERE nric=? AND status=0"
    cursor.execute(statement, [nric])
    db.commit()
    return make_response(jsonify({"message": "Draft Loan Removed!", "data": None, "error": "0", "meta": None}), 200)


def createloan(nric):
    loanNo = random.randint(1000, 10000)
    db = get_db()
    cursor = db.cursor()

    statement = "SELECT phone,email FROM user_contact WHERE nric=? AND status='1';"
    cursor.execute(statement, [nric])
    data = cursor.fetchone()
    db.commit()

    statement = "INSERT INTO loans (fullname, dob, nric, oldNric, gender, nation, religion, citizenship, maritalStatus, phoneHome, phoneMobile, email, agencyHelp, monthlyIncome, highEduInstitution, studyLevel, yearsOfStudy, healthStatus, disabledStatus, bankruptcyStatus, disabilities, workStatus, vulnerableGroups, program1, program2, add1, add2, add3, permanentCity, permanentZipCode, permanentState, madd1, madd2, madd3, mailCity, mailZipCode, mailState, guarantee1, guarantee2, status,loanNo,step,course) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?,?,?)"
    cursor.execute(statement, ["", "", nric, "", "", "", "", "", "", "", data[0], data[1], "", "", "", "", "", "",
                   "", "", "", "", "", "ya", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", '0', loanNo, '0', ""])  # 43 fields
    db.commit()

    statement = "INSERT INTO guarantees (gName, gNric, gBankruptcyStatus, gDebtStatus, gPhone, gPhoneVeriDate, gMail, gMailVeriDate, gNo, status, loanNo, gQR) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?);"
    cursor.execute(statement, [
                   "", "", "", "", "", "", "", "", "1", "0", loanNo, ""])
    db.commit()

    statement = "INSERT INTO guarantees (gName, gNric, gBankruptcyStatus, gDebtStatus, gPhone, gPhoneVeriDate, gMail, gMailVeriDate, gNo, status, loanNo, gQR) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?);"
    cursor.execute(statement, [
                   "", "", "", "", "", "", "", "", "2", "0", loanNo, ""])
    db.commit()

    return make_response(jsonify({"message": "Loan details added successfully", "data": loanNo, "error": "0", "meta": None}), 200)


