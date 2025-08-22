SELECT COUNT(*) AS total_actors FROM actors;
INSERT INTO actors (first_name, last_name, birth_date)
VALUES ('John', '', NULL);

-- The outcome will be an error, because in our schema all fields are defined with NOT NULL 