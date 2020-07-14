-- script that lists the number of records with the same score in
-- the table second_table of the database hbtn_0c_0 in your MySQL server;
SELECT name AS number FROM second_table GROUP BY name ORDER BY score DESC;
