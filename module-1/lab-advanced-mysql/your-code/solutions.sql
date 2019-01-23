-- CHALLENGE 1
SELECT au_id, SUM(Aggregated_royalties + advance) AS profits
FROM (
	SELECT title_id, au_id, advance, SUM(sales_royalty) AS Aggregated_royalties 
	FROM (
		SELECT titleauthor.title_id AS title_id, titles.advance as advance, titleauthor.au_id AS au_id,(titles.price * sales.qty * titles.royalty / 100 * titleauthor.royaltyper / 100) AS sales_royalty
		FROM titleauthor
		INNER JOIN titles ON titles.title_id = titleauthor.title_id 
		INNER JOIN sales ON sales.title_id = titles.title_id 
	) as summary
	GROUP BY au_id, title_id
) as summary2
GROUP BY au_id

-- CHALLENGE 2

/* -- TIENE ERRORES PORQUE NO HE SABIDO LLEGAR HASTA EL FINAL 
CREATE TEMPORARY TABLE table_inner
SELECT titleauthor.title_id AS title_id, titles.advance as advance, titleauthor.au_id AS au_id,(titles.price * sales.qty * titles.royalty / 100 * titleauthor.royaltyper / 100) AS sales_royalty
FROM titleauthor
INNER JOIN titles ON titles.title_id = titleauthor.title_id 
INNER JOIN sales ON sales.title_id = titles.title_id 

CREATE TEMPORARY TABLE table_medium
SELECT title_id, au_id, advance, SUM(sales_royalty) AS Aggregated_royalties 
FROM (
	table_inner
	) as summary
GROUP BY au_id, title_id

SELECT au_id, SUM(Aggregated_royalties + advance) AS profits
FROM ( 
	table_medium
) as summary2
GROUP BY au_id
*/

-- CHALLENGE 3
CREATE TABLE most_profiting_authors
SELECT au_id, SUM(Aggregated_royalties + advance) AS profits
FROM (
	SELECT title_id, au_id, advance, SUM(sales_royalty) AS Aggregated_royalties 
	FROM (
		SELECT titleauthor.title_id AS title_id, titles.advance as advance, titleauthor.au_id AS au_id,(titles.price * sales.qty * titles.royalty / 100 * titleauthor.royaltyper / 100) AS sales_royalty
		FROM titleauthor
		INNER JOIN titles ON titles.title_id = titleauthor.title_id 
		INNER JOIN sales ON sales.title_id = titles.title_id 
	) as summary
	GROUP BY au_id, title_id
) as summary2
GROUP BY au_id

SELECT *
FROM most_profiting_authors;
