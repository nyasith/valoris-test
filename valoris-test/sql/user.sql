-- SQLite

CREATE TABLE IF NOT EXISTS user_contact(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nric TEXT NOT NULL,
  phone TEXT NOT NULL,
  email TEXT NOT NULL,
  status INTEGER,
  record_date TEXT,
  otp TEXT
);

CREATE TABLE IF NOT EXISTS login(
  id INTEGER PRIMARY KEY NOT NULL,
  nric TEXT NOT NULL,
  password TEXT NOT NULL,
  status INTEGER,
  record_date TEXT
);

CREATE TABLE IF NOT EXISTS profile(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  nric TEXT NOT NULL,
  employer TEXT,
  job_title TEXT,
  annual_income REAL
);


INSERT INTO user_contact (nric,phone,email,status,record_date,otp)
VALUES ("967050024V", "0110123456", "abc@gmail.com","1","2022-10-14","o1");

INSERT INTO login("nric","password","status","record_date")
VALUES ("967050024V","abc","1","2022-11-17");

INSERT INTO profile("name","nric","employer","job_title","annual_income")
VALUES ("name1","967050024V", "employer1","teacher","1000");