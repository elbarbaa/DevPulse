SELECT
    language,
    repository_count,
    avg_stars,
    avg_popularity
FROM language_popularity
ORDER BY avg_popularity DESC;