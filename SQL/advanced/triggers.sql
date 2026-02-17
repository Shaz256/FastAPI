CREATE OR REPLACE FUNCTION set_default_hire_date()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.hire_date IS NULL THEN
        NEW.hire_date := CURRENT_DATE;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_set_hire_date
BEFORE INSERT ON employees
FOR EACH ROW
EXECUTE FUNCTION set_default_hire_date();
