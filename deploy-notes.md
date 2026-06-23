# Deploy Notes - Gestor de Tareas

## Pasos de despliegue simulado

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo
```

### 2. Configurar variables de entorno
Crear archivo `.env` con:
DB_NAME=taskdb

DB_USER=postgres

DB_PASSWORD=postgres

DB_HOST=db

DB_PORT=5432

SECRET_KEY=clave-secreta-produccion

DEBUG=False

### 3. Levantar con Docker Compose
```bash
docker-compose up --build -d
```

### 4. Validar desde el navegador
Abrir: http://localhost:8000/tareas/

## Pipeline CI/CD
- **Job test:** Corre los tests automáticos con PostgreSQL
- **Job build:** Construye la imagen Docker y la guarda como artefacto
- **Job deploy-simulado:** Simula el despliegue copiando el proyecto