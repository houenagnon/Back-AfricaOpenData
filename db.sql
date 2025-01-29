CREATE DATABASE opendata_app;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Table des utilisateurs
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    username VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(150) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    profession VARCHAR(150),
    is_admin VARCHAR(50) CHECK (role IN ('admin', 'user')) DEFAULT 'user',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table des thématiques
CREATE TABLE themes (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table des sous-thématiques
CREATE TABLE subthemes (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    theme_id UUID NOT NULL,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_theme FOREIGN KEY (theme_id) REFERENCES themes (id) ON DELETE CASCADE
);

-- Table des fichiers de données
CREATE TABLE files (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    subtheme_id UUID NOT NULL,
    filename VARCHAR(255) NOT NULL,
    file_path VARCHAR(500) NOT NULL,
    source VARCHAR(255),
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_subtheme FOREIGN KEY (subtheme_id) REFERENCES subthemes (id) ON DELETE CASCADE
);

-- Table des téléchargements
CREATE TABLE downloads (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL,
    file_id UUID NOT NULL,
    downloaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE,
    CONSTRAINT fk_file FOREIGN KEY (file_id) REFERENCES files (id) ON DELETE CASCADE
);

-- Table des logs (suivi des actions)
CREATE TABLE logs (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL,
    action VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_log_user FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE SET NULL
);


-- Index sur les emails des utilisateurs pour des recherches rapides
CREATE INDEX idx_users_email ON users (email);

-- Index sur les noms des thématiques et sous-thématiques
CREATE INDEX idx_themes_name ON themes (name);
CREATE INDEX idx_subthemes_name ON subthemes (name);

-- Index sur les fichiers pour une recherche rapide par nom
CREATE INDEX idx_files_filename ON files (filename);


INSERT INTO users (username, email, password, profession, role)
VALUES ('john_doe', 'john@example.com', 'hashed_password', 'Data Scientist', 'user');

INSERT INTO themes (name, description)
VALUES ('Économie', 'Données économiques globales');

INSERT INTO subthemes (theme_id, name, description)
VALUES ((SELECT id FROM themes WHERE name = 'Économie'), 'PIB par habitant', 'Produit Intérieur Brut par habitant');

INSERT INTO files (subtheme_id, filename, file_path, source)
VALUES ((SELECT id FROM subthemes WHERE name = 'PIB par habitant'), 'pib_2023.csv', '/data/economy/pib_2023.csv', 'Banque Mondiale');

