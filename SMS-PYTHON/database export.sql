--
-- File generated with SQLiteStudio v3.4.4 on Thu May 16 00:01:43 2024
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: details
CREATE TABLE IF NOT EXISTS details (id TEXT (100), name TEXT (100), gender TEXT (100), enrol_date TEXT (100), grade TEXT (100), test_no TEXT (100), marks TEXT (100));
INSERT INTO details (id, name, gender, enrol_date, grade, test_no, marks) VALUES ('1', 'sewmini', 'Male', '2024.05.10', '13', '2nd Term', '29');
INSERT INTO details (id, name, gender, enrol_date, grade, test_no, marks) VALUES ('2', 'sew', 'Female', '2024.05.10', '12', '2nd Term', '29');
INSERT INTO details (id, name, gender, enrol_date, grade, test_no, marks) VALUES ('3', 'ee', 'Female', '2024.08.09', '13', '2nd Term', '25');

-- Table: users
CREATE TABLE IF NOT EXISTS users (name TEXT (100), password TEXT (100), confirm_password TEXT (100));
INSERT INTO users (name, password, confirm_password) VALUES ('ww', 'w', 'w');
INSERT INTO users (name, password, confirm_password) VALUES ('tt', 'tt', 'tt');
INSERT INTO users (name, password, confirm_password) VALUES ('hiru', '23', '23');
INSERT INTO users (name, password, confirm_password) VALUES ('er', 'er', 'er');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
