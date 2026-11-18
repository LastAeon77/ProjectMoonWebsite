-- Exact row count for every table in the public schema, one "table count" per line.
-- Used to prove a dump/restore copied everything: run before and after, then diff.
SELECT table_name || ' ' || (xpath('/row/c/text()',
         query_to_xml(format('SELECT count(*) AS c FROM public.%I', table_name), false, true, '')))[1]::text
FROM information_schema.tables
WHERE table_schema = 'public' AND table_type = 'BASE TABLE'
ORDER BY 1;
