--Exercise 1:

SELECT * FROM language ;
SELECT f.title, f.description, l.name AS language_name FROM film f JOIN language l ON l.language_id = f.language_id;
SELECT f.title, f.description, l.name AS language_name FROM language l LEFT JOIN film f ON l.language_id = f.language_id; 
CREATE TABLE new_film (id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL) ;
INSERT INTO new_film (name) VALUES ('Inception'), ('The Dark knight'), ('Interstellar'), ('The Godfather');
CREATE TABLE customer_review (
    review_id SERIAL PRIMARY KEY,
    film_id INT NOT NULL,
    language_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    score INT CHECK (score BETWEEN 1 AND 10),
    review_text TEXT,
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_film FOREIGN KEY (film_id)
        REFERENCES new_film(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_language FOREIGN KEY (language_id)
        REFERENCES language(language_id)
);

INSERT INTO customer_review (film_id, language_id, title, score, review_text, last_update)
VALUES
    (1, 1, 'Great Mystery', 9, 'a very engaging and suspenseful movie', NOW()),
    (2, 2, 'Inspiring', 8, 'nice story', NOW());

DELETE FROM new_film WHERE id = 1;
--All reviews linked to that film (film_id = 1) will be automatically deleted from customer_review


--Exercise 2:

UPDATE film
SET language_id = 2 WHERE film_id IN (1, 2, 3);

SELECT
    tc.constraint_name, 
    kcu.column_name, 
    ccu.table_name AS foreign_table, 
    ccu.column_name AS foreign_column
FROM information_schema.table_constraints tc
JOIN information_schema.key_column_usage kcu
    ON tc.constraint_name = kcu.constraint_name
JOIN information_schema.constraint_column_usage ccu
    ON ccu.constraint_name = tc.constraint_name
WHERE tc.table_name = 'customer'
AND tc.constraint_type = 'FOREIGN KEY';

DROP TABLE IF EXISTS customer_review;

SELECT COUNT(*) AS outstanding_rentals
FROM rental
WHERE return_date IS NULL;

SELECT f.film_id, f.title, f.rental_rate
FROM rental r
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE r.return_date IS NULL LIMIT 30;

SELECT f.film_id, f.title
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
WHERE a.first_name = 'PENELOPE'
  AND a.last_name = 'MONROE'
  AND (f.description ILIKE '%sumo%' OR f.title ILIKE '%sumo%');

SELECT f.film_id, f.title, f.length
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
WHERE c.name = 'Documentary'
  AND f.length < 60
  AND f.rating = 'R';

SELECT f.film_id, f.title
FROM rental r
JOIN payment p ON r.rental_id = p.rental_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
JOIN customer c ON r.customer_id = c.customer_id
WHERE c.first_name = 'MATTHEW'
  AND c.last_name = 'MAHAN'
  AND p.amount > 4
  AND r.return_date BETWEEN '2005-07-28' AND '2005-08-01';

SELECT f.film_id, f.title, f.replacement_cost
FROM rental r
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
JOIN customer c ON r.customer_id = c.customer_id
WHERE c.first_name = 'MATTHEW'
  AND c.last_name = 'MAHAN'
  AND (f.title ILIKE '%boat%' OR f.description ILIKE '%boat%')
ORDER BY f.replacement_cost DESC
LIMIT 1;
