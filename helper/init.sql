-- init.sql

-- Maak de database aan (deze stap is optioneel, omdat we deze al hebben gespecificeerd in docker-compose)
CREATE DATABASE IF NOT EXISTS todo_db;

-- Gebruik de database
\c todo_db;

-- Maak de todo tabel aan
CREATE TABLE IF NOT EXISTS todo (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    task VARCHAR(255) NOT NULL,
    done BOOLEAN DEFAULT FALSE
);

-- Vul de tabel met 10 dummy rows
INSERT INTO todo (date, task, done) VALUES
('2024-10-01', 'Buy groceries', FALSE),
('2024-10-02', 'Read a book', TRUE),
('2024-10-03', 'Go for a walk', FALSE),
('2024-10-04', 'Finish project report', TRUE),
('2024-10-05', 'Cook dinner', FALSE),
('2024-10-06', 'Clean the house', FALSE),
('2024-10-07', 'Watch a movie', TRUE),
('2024-10-08', 'Workout', FALSE),
('2024-10-09', 'Attend a meeting', TRUE),
('2024-10-10', 'Call a friend', FALSE);
