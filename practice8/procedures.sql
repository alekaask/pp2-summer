-- Upsert procedure: insert a new user or update the name on an existing phone
CREATE OR REPLACE PROCEDURE upsert_user(p_name TEXT, p_phone TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO phonebook(name, phone)
    VALUES (p_name, p_phone)
    ON CONFLICT (phone) DO UPDATE SET name = EXCLUDED.name;
END;
$$;

-- Bulk-insert procedure: adds multiple users, validating phone format
-- and reporting errors for invalid rows via RAISE NOTICE
CREATE OR REPLACE PROCEDURE bulk_insert_users(p_names TEXT[], p_phones TEXT[])
LANGUAGE plpgsql
AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1..array_length(p_names, 1) LOOP
        IF p_phones[i] ~ '^\+7\d{10}$' THEN
            INSERT INTO phonebook(name, phone)
            VALUES (p_names[i], p_phones[i])
            ON CONFLICT (phone) DO NOTHING;
        ELSE
            RAISE NOTICE 'Invalid phone skipped: % (name: %)', p_phones[i], p_names[i];
        END IF;
    END LOOP;
END;
$$;

-- Delete procedure: removes a record by username or phone number
CREATE OR REPLACE PROCEDURE delete_user_proc(p_value TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM phonebook WHERE name = p_value OR phone = p_value;
END;
$$;
