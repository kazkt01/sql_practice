# sql_practice

# SQL Minimal (MySQL + Python + HTML)

## 起動
```bash
docker compose up -d --build


# mySQLに入るためのコマンド
docker exec -it mysql-min mysql -h127.0.0.1 -udev -pdevpass -D appdb




CREATE TABLE tests (
    sample_id INTEGER NOT NULL,
    sample_name VARCHAR(15) NOT NULL,  
    PRIMARY KEY (sample_id) 
);

