
# Run SQL

```sql
CREATE DATABASE test

CREATE TABLE test.testtable
(
    `id` Int32,
    `name` String,
    `text` String,
    `small-number` Int8
) ENGINE = MergeTree PARTITION BY id
ORDER BY
  id SETTINGS index_granularity = 8192
  
 
INSERT INTO test.testtable
(id, `name`, `text`, `small-number`)
VALUES(0, 'somename','afdjlasjfklajskfjladf', 3);


SELECT * FROM test.testtable t 
```