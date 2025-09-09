-- TO-Do Tabelle erstellen
CREATE TABLE IF NOT EXISTS todos (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    completed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Test-Daten einfügen
INSERT INTO todos (title, description) VALUES 
('Docker lernen', 'Container und Images verstehen'),
('Web-App bauen', 'Flask und PostgreSQL verbinden'),
('To-Do App testen', 'Alle Funktionen durchprobieren'); 
