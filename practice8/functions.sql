CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    phone TEXT UNIQUE NOT NULL
);

-- Pattern-search function: matches name or phone against a pattern
CREATE OR REPLACE FUNCTION search_pattern(p_pattern TEXT)
RETURNS TABLE(id INT, name TEXT, phone TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT p.id, p.name, p.phone
    FROM phonebook p
    WHERE p.name ILIKE '%' || p_pattern || '%'
       OR p.phone ILIKE '%' || p_pattern || '%';
END;
$$;

-- Paginated query function
CREATE OR REPLACE FUNCTION get_paginated(p_page INT, p_limit INT)
RETURNS TABLE(id INT, name TEXT, phone TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT p.id, p.name, p.phone
    FROM phonebook p
    ORDER BY p.id
    LIMIT p_limit OFFSET (p_page - 1) * p_limit;
END;
$$;
