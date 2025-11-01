-- CREATE TABLE IF NOT EXISTS users (
--   id SERIAL PRIMARY KEY,
--   name TEXT NOT NULL,
--   email TEXT UNIQUE,
--   created_at TIMESTAMPTZ DEFAULT NOW()
-- );

-- INSERT INTO users (name, email) VALUES
-- ('Alice','alice@example.com'),
-- ('Bob','bob@example.com')
-- ON CONFLICT DO NOTHING;


CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (name, email) VALUES
('Alice','alice@example.com'),
('Bob','bob@example.com')
ON DUPLICATE KEY UPDATE email = VALUES(email);

