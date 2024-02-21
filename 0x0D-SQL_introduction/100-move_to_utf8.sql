-- convert db into UTF 8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8 COLLATE utf8_general_ci;
USE hbtn_0c_0;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE first_tablem MODIFY name VARCHAR(256) CHARACTER SET utf8 COLLATE utf8_general_ci;
