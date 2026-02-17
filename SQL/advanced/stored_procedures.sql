CREATE OR REPLACE PROCEDURE give_bonus(
    dept_id INT,
    bonus_pct NUMERIC
)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE employees
    SET salary = salary * (1 + bonus_pct / 100)
    WHERE department_id = dept_id;
END;
$$;
