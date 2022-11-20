-- SQLite

CREATE TABLE IF NOT EXISTS digital_certificate(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  dc_id TEXT,
  dept_name TEXT,
  ministry TEXT,
  cert_title TEXT,
  course TEXT,
  level TEXT,
  name  TEXT,
  nric TEXT,
  college_name TEXT,
  state TEXT,
  cert_no1 TEXT,
  cert_no2 TEXT,
  generated_date TEXT,
  status INTEGER
);

INSERT INTO digital_certificate (dc_id, dept_name, ministry, cert_title, course, level, name,
 nric, college_name, state, cert_no1, cert_no2, generated_date, status)
 VALUES ("2022-NY-123456789-B", "education dep", "education ministry", 
 "engineering", "computing", "level1",
  "ramesh", "987050024V", "nibm", "state1", 
  "certL02223", "certS102447930", "2020-12-24", 2);