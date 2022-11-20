-- SQLite

CREATE TABLE IF NOT EXISTS cwr(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  qualification TEXT,
  nric TEXT,
  gender TEXT,
  phone_status TEXT,
  email_status TEXT,
  employer TEXT,
  employment_date TEXT,
  job_title TEXT,
  risk_level TEXT,
  risk_type TEXT,
  balance_amount TEXT,
  loan_type TEXT,
  loan_amt REAL,
  status_date TEXT
);

INSERT INTO cwr (name, qualification,nric,gender,
phone_status,email_status,employer,employment_date,
job_title,risk_level,risk_type,balance_amount,
loan_type,loan_amt,status_date)

VALUES ("name1","quali1","200020541V","female",
"sts1","ests1","yes","2020-02-10","teachet","r1",
"r2","10000","typ1","500000","datests");