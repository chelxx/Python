
-- 1
SELECT countries.name, languages.language, languages.percentage
FROM countries
JOIN languages ON countries.code = languages.country_code
WHERE language = 'Slovene'
ORDER BY languages.percentage DESC;

-- 2
SELECT countries.name, COUNT(cities.id) AS city_count
FROM countries
JOIN cities ON countries.id = cities.country_id
GROUP BY countries.name
ORDER BY city_count DESC;

-- 3
SELECT cities.name, cities.population
FROM cities
JOIN countries ON cities.country_id = countries.id
WHERE countries.name = 'Mexico' AND cities.population > 500000
ORDER BY cities.population DESC;

-- 4
SELECT languages.language, languages.percentage
FROM languages
WHERE languages.percentage > 89
ORDER BY  languages.percentage DESC;

-- 5
SELECT countries.surface_area, countries.population
FROM countries
WHERE countries.surface_area < 501 AND countries.population > 100000
ORDER BY countries.population DESC;

-- 6
SELECT countries.name, countries.government_form, countries.capital, countries.life_expectancy
FROM countries
WHERE countries.government_form = 'Constitutional Monarchy' AND countries.capital > 200 AND countries.life_expectancy > 75
ORDER BY countries.name DESC;

-- 7
SELECT countries.name, cities.name, cities.district, cities.population
FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE countries.name = 'Argentina' AND cities.district = 'Buenos Aires' AND cities.population > 500000
ORDER BY cities.population ASC;

-- 8 
SELECT region, COUNT(name) as country_count
FROM countries
GROUP BY region
ORDER BY country_count DESC;














