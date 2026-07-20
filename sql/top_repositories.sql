SELECT
    name,
    owner,
    language,
    stars,
    forks,
    popularity_score,
    url
FROM top_repositories
ORDER BY popularity_score DESC
LIMIT 10;