-- init.sql

\c todo_db;

-- Maak een tabel voor de users
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    --username VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    hashed_password VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Maak een tabel voor de todo lists, met een foreign key naar de users tabel
CREATE TABLE IF NOT EXISTS todo (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    date DATE NOT NULL,
    task VARCHAR(255) NOT NULL,
    done BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);


-- Voeg voorbeeldgebruikers toe
INSERT INTO users (email) 
VALUES 
('bas@example.com'),
('jane@example.com');

-- Voeg to-do items toe voor deze gebruikers
INSERT INTO todo (user_id, date, task, done) 
VALUES 
(1, '2024-10-08', 'Finish FastAPI project', FALSE),
(1, '2024-10-09', 'Buy groceries', TRUE),
(2, '2024-10-10', 'Prepare for meeting', FALSE),
(2, '2024-10-11', 'Call the client', FALSE);

