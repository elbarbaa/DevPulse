SELECT
    license,
    repository_count,
    avg_stars
FROM license_analysis
ORDER BY repository_count DESC;