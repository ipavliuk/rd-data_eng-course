/*
 Завдання на SQL до лекції 03.
 */


/*
1.
Вивести кількість фільмів в кожній категорії.
Результат відсортувати за спаданням.
*/
-- SQL code goes here...
SELECT
	c.name, 
	Count(f.film_id) AS film_number
FROM
	public.film AS f
INNER JOIN public.film_category AS fc ON
	fc.film_id = f.film_id
INNER JOIN public.category AS c ON
	c.category_id = fc.category_id
GROUP BY
	c.name
ORDER BY
	c.name;

/*
2.
Вивести 10 акторів, чиї фільми брали на прокат найбільше.
Результат відсортувати за спаданням.
*/
-- SQL code goes here...
SELECT
	a.actor_id,
	CONCAT(a.first_name, ' ', a.last_name) AS full_name,
	COUNT(r.rental_id) AS total_rent
FROM
	public.actor AS a
INNER JOIN public.film_actor AS fa ON
	fa.actor_id = a.actor_id
INNER JOIN public.inventory AS i ON
	i.film_id = fa.film_id
INNER JOIN public.film AS f ON
	f.film_id = i.film_id
INNER JOIN public.rental AS r ON
	r.inventory_id = i.inventory_id
GROUP BY
	a.actor_id,
	full_name
ORDER BY
	total_rent DESC
LIMIT 10;


/*
3.
Вивести категорія фільмів, на яку було витрачено найбільше грошей
в прокаті
*/
-- SQL code goes here...

SELECT
	c.name AS category,
	SUM(p.amount) AS total_amount
FROM
	public.category AS c
INNER JOIN public.film_category AS fc ON
	fc.category_id = c.category_id
INNER JOIN public.inventory AS i ON
	i.film_id = fc.film_id
INNER JOIN public.rental AS r ON
	r.inventory_id = i.inventory_id
INNER JOIN public.payment AS p ON
	p.rental_id = r.rental_id
GROUP BY
	c.name
ORDER BY
	total_amount DESC;
/*
4.
Вивести назви фільмів, яких не має в inventory.
Запит має бути без оператора IN
*/
-- SQL code goes here...
SELECT
	f.title,
	i.inventory_id
FROM
	public.film AS f
LEFT JOIN public.inventory AS i ON
	i.film_id = f.film_id
WHERE
	i.inventory_id IS NOT NULL
ORDER BY
	f.title;

/*
5.
Вивести топ 3 актори, які найбільше зʼявлялись в категорії фільмів “Children”.
*/
-- SQL code goes here...
SELECT
	a.actor_id,
	CONCAT(a.first_name, ' ', a.last_name) AS full_name,
	COUNT(a.actor_id) AS roles_played
FROM
	public.actor AS a
INNER JOIN public.film_actor AS fa ON
	fa.actor_id = a.actor_id
INNER JOIN public.film_category AS fc ON
	fc.film_id = fa.film_id
INNER JOIN public.category AS c ON
	c.category_id = fc.category_id
WHERE
	c.name = 'Children'
GROUP BY
	a.actor_id,
	full_name
ORDER BY
	roles_played
LIMIT 3;
