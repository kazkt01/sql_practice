# sql_practice

# SQL Minimal (MySQL + Python + HTML)

## 起動
```bash
docker compose up -d --build


# mySQLに入るためのコマンド
docker exec -it mysql-min mysql -h127.0.0.1 -udev -pdevpass -D appdb

# SQL_practices
CREATE TABLE tests (
    sample_id INTEGER NOT NULL,
    sample_name VARCHAR(15) NOT NULL,  
    PRIMARY KEY (sample_id) 
);

CREATE TABLE my_slaves(
 id INTEGER NOT NULL,
 name VARCHAR(15) NOT NULL,
 PRIMARY KEY (id)
);

# テーブルを消すとき
DROP TABLE my_slaves;

# カラムを消すとき
ALETER TABLE テーブル名 DROP COLUMN カラム名；







