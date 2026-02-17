-- =============================================
-- NORMALIZATION NOTES
-- =============================================

-- 1NF: Atomic columns (no arrays, no repeating groups)
-- employees.name is atomic ✔

-- 2NF: No partial dependency
-- employees fully depends on employee_id ✔

-- 3NF: No transitive dependency
-- department stored in separate table ✔

-- This schema follows 3NF.
