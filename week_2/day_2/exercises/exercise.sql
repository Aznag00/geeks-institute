SELECT * FROM customer
SELECT first_name, last_name FROM customer AS full_name
SELECT DISTINCT create_date FROM customer
SELECT * FROM customer ORDER BY first_name DESC
SELECT film_id, title, description, release_year FROM film ORDER BY rental_rate ASC
SELECT * FROM film WHERE film_id IN (15, 150)
SELECT film_id, title, description, length, rental_rate FROM film WHERE title ILIKE 'batman';
SELECT film_id, title, description, length, rental_rate FROM film WHERE title ILIKE LEFT('game of thrones',2) || '%';
SELECT film_id, title, rental_rate FROM film ORDER BY rental_rate ASC LIMIT 10;
SELECT film_id, title, rental_rate FROM film ORDER BY rental_rate ASC OFFSET 10 LIMIT 10;
SELECT c.customer_id, c.first_name, c.last_name, p.amount, p.payment_date FROM customer c JOIN payment p ON c.customer_id = p.customer_id ORDER BY c.customer_id;
SELECT f.film_id, f.title FROM film f LEFT JOIN inventory i ON f.film_id = i.film_id WHERE i.inventory_id IS NULL;
SELECT ci.city, co.country FROM city ci JOIN country co ON ci.country_id = co.country_id;
SELECT c.customer_id, c.first_name, c.last_name,
       p.amount, p.payment_date, s.staff_id, s.first_name AS staff_first_name, s.last_name AS staff_last_name
FROM payment p JOIN customer c ON p.customer_id = c.customer_id JOIN staff s ON p.staff_id = s.staff_id ORDER BY s.staff_id;