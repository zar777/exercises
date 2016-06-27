-- Create a database
CREATE DATABASE index_db
-- Create user with a specific option
CREATE USER gianluca
-- Grant all privileges on a specific database to given user
grant all privileges on database index_db to gianluca;
-- Grant SELECT, INSERT, UPDATE, DELETE on all tables to given user
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public to gianluca;
-- Grant all default privileges on a specific schema about tables and sequences to given user
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON TABLES TO gianluca;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON sequences TO gianluca;
-- Create a table with a specific fields
CREATE TABLE index(Word INTEGER, File text, Occurrence integer[]);
