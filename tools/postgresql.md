# PostgreSQL

* Create a DB in RDS:
    ```
    psql -h <endpoint> -d postgres -U postgres
    create user <user> with password '<password>' createdb;
    create database <db-name>;
    alter user <user> nocreatedb;
    ```
* Restore SQL dump to RDS: 
    ```
    pg_restore -h <endpoint> -d <db-name> -U <user> <dump-file>
    ```
* Get version: `select version();`
* Convert time to seconds since epoch: `pqp "select extract(epoch from timestamp '2016-05-12T19:40:56.820Z')"`
* Query for column types: `select column_name, data_type, character_maximum_length from infromation_schema.columns where table_name='<table-name>'`
* Terminate all connections to a DB: `SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE pid <> pg_backend_pid() AND datname = '<db-name>';`
* List DBs: `\l`
* Describe tables: `\d` or `\d <table-name>`

# Choosing a DB

* [Why Uber Engineering Switched from Postgres to MySQL](https://eng.uber.com/postgres-to-mysql-migration/)
