createdb -h localhost -U postgres index_db

CREATE USER name [ [ WITH ] option [ ... ] ]

grant all privileges on database index_db to gianluca;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public to gianluca;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON TABLES TO gianluca;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON sequences TO gianluca;

psql -d index_db -U gianluca

CREATE TABLE Index(Word INTEGER, File text, Occurrence integer[]);
