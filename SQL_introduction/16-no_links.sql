-- Script that lists all recorded scores by order of second_table
SELECT score, name FROM second_table WHERE name IS  NOT NULL ORDER BY score DESC;