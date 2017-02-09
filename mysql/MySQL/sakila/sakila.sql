-- number 1 --
SELECT customer.first_name, customer.last_name, customer.email, address.address
FROM customer
LEFT JOIN address on customer.address_id = address.address_id
WHERE address.city_id = 312;

-- number 2 --
-- What query would you run to get all comedy films? Your query should return film title, description, release year, rating, special features, and genre (category). --
SELECT title, description, release_year, rating, special_features, category.name AS genre
FROM film
LEFT JOIN film_category ON film.film_id = film_category.film_id
LEFT JOIN category ON film_category.category_id = category.category_id
WHERE category.name = 'Comedy';

-- number 3 --
-- What query would you run to get all the films joined by actor_id=5? Your query should return the film title, description, and release year. --
SELECT title, description, release_year
FROM film
LEFT JOIN film_actor ON film_actor.film_id = film.film_id
LEFT JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE actor.actor_id = 5;

-- number 4 --
-- What query would you run to get all the customers in store_id = 1 and inside these cities (1, 42, 312 and 459)? Your query should return customer first name, last name, email, and address. --
SELECT store.store_id, first_name, last_name, email, address.address
FROM customer
LEFT JOIN store ON customer.store_id = store.store_id
LEFT JOIN address ON customer.address_id = address.address_id
WHERE store.store_id = 1 AND (address.city_id = 1 OR address.city_id = 42 OR address.city_id = 312 OR address.city_id = 459);

-- 5 --
-- What query would you run to get all the films with a "rating = G" and "special feature = behind the scenes",--
-- joined by actor_id = 15? Your query should return the film title, description, release year, rating, --
-- and special feature. Hint: You may use LIKE function in getting the 'behind the scenes' part. --
SELECT title, description, release_year, rating, special_features
FROM film
LEFT JOIN film_actor ON film_actor.film_id = film.film_id
LEFT JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE rating = 'G' AND special_features LIKE '%Behind the Scenes%' AND actor.actor_id = 15;

-- 6 --
--  What query would you run to get all the actors that joined in the film_id = 369? Your query should --
-- return the first_name, last name and last_update of the actors. --
SELECT first_name, last_name
FROM actor
LEFT JOIN film_actor ON film_actor.actor_id = actor.actor_id
LEFT JOIN film ON film_actor.film_id = film.film_id
WHERE film.film_id = 369;

-- 7 --
-- What query would you run to get all the action films which are joined by SANDRA KILMER? --
-- Your query should return film title, description, release year, rating, special features, --
-- genre (category), and actor's first name and last name. --
SELECT title, description, release_year, rating, special_features, category.name AS genre, actor.first_name, actor.last_name
FROM film
LEFT JOIN  film_actor ON film_actor.film_id = film.film_id
LEFT JOIN actor ON film_actor.actor_id = actor.actor_id
LEFT JOIN film_category ON film_category.film_id = film.film_id
LEFT JOIN category ON film_category.category_id = category.category_id
WHERE actor.first_name LIKE 'SANDRA' AND actor.last_name LIKE 'KILMER' AND category.name = 'action';


0	652	12:43:31	SELECT title, description, release_year, rating, special_features, category.name AS genre, actor.first_name, actor.last_name
 FROM film
 LEFT JOIN actor ON film_actor.actor_id = actor.actor_id
 LEFT JOIN  film_actor ON film_actor.film_id = film.film_id
 LEFT JOIN film_category ON film_category.film_id = film.film_id
 LEFT JOIN category ON film_category.category_id = category.category_id
 WHERE actor.first_name = 'SANDRA' AND actor.last_name = 'KILMER'
 LIMIT 0, 1000	Error Code: 1054. Unknown column 'film_actor.actor_id' in 'on clause'	0.000 sec