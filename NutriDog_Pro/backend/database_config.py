import sqlite3
import os

class Database:
    def __init__(self):
        self.db_name = "canisnutri_ia.db"

    def get_connection(self):
        conn = sqlite3.connect(self.db_name)
        conn.row_factory = sqlite3.Row # Para retornar diccionarios en lugar de tuplas
        return conn

    def inicializar_db(self):
        """Crea las tablas si no existen según el modelo de la tesis."""
        query_usuarios = """
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            rol TEXT CHECK(rol IN ('veterinario', 'dueño'))
        )"""

        query_perros = """
        CREATE TABLE IF NOT EXISTS perros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            dueno_id INTEGER,
            nombre TEXT NOT NULL,
            peso_actual REAL,
            objetivo TEXT,
            alergias TEXT,
            FOREIGN KEY (dueno_id) REFERENCES usuarios(id)
        )"""

        query_logs = """
        CREATE TABLE IF NOT EXISTS logs_progreso (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            perro_id INTEGER,
            peso_registrado REAL,
            fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (perro_id) REFERENCES perros(id)
        )"""

        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(query_usuarios)
        cursor.execute(query_perros)
        cursor.execute(query_logs)
        conn.commit()
        conn.close()
        print("Base de datos inicializada correctamente.")

# Al ejecutar este archivo directamente, se crea la base de datos
if __name__ == "__main__":
    db = Database()
    db.inicializar_db()