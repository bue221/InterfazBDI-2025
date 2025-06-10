# InterfazBDI-2025

Este proyecto consiste en una interfaz web para interactuar con una base de datos Oracle, desarrollada con React + TypeScript en el frontend y Node.js en el backend.

## Requisitos Previos

- Node.js (versión 18 o superior)
- pnpm (versión 10.11.0 o superior)
- Oracle Database
- Oracle Instant Client

## Estructura del Proyecto

```
.
├── frontend/          # Aplicación React + TypeScript
├── backend/           # Servidor Node.js
└── InterfazBDI-2025.pdf  # Documentación del proyecto
```

## Instalación

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd InterfazBDI-2025
```

### 2. Configurar el Backend

```bash
cd backend
pnpm install
```

Configura las variables de entorno necesarias para la conexión a Oracle:
- Crea un archivo `.env` en el directorio `backend/` con las siguientes variables:
  ```
  ORACLE_USER=tu_usuario
  ORACLE_PASSWORD=tu_contraseña
  ORACLE_CONNECTION_STRING=tu_connection_string
  ```

### 3. Configurar el Frontend

```bash
cd frontend
pnpm install
```

## Ejecución

### Backend

```bash
cd backend
pnpm start
```

El servidor backend se ejecutará en `http://localhost:3000`

### Frontend

```bash
cd frontend
pnpm dev
```

La aplicación frontend estará disponible en `http://localhost:5173`

## Scripts Disponibles

### Backend
- `pnpm start`: Inicia el servidor backend

### Frontend
- `pnpm dev`: Inicia el servidor de desarrollo
- `pnpm build`: Construye la aplicación para producción
- `pnpm preview`: Previsualiza la versión de producción
- `pnpm lint`: Ejecuta el linter

## Tecnologías Utilizadas

### Frontend
- React
- TypeScript
- Vite
- Tailwind CSS
- shadcn/ui
- Axios

### Backend
- Node.js
- Express
- OracleDB
- CORS

## Desarrollo

1. Asegúrate de tener todas las dependencias instaladas
2. Inicia el servidor backend
3. En otra terminal, inicia el servidor frontend
4. Realiza tus cambios
5. Los cambios en el frontend se reflejarán automáticamente gracias al hot-reload

## Contribución

1. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
2. Commit tus cambios (`git commit -m 'feat: add some amazing feature'`)
3. Push a la rama (`git push origin feature/AmazingFeature`)
4. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia ISC. 