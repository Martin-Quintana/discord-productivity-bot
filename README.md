# Discord Productivity Bot

Bot de productividad para Discord con comandos para gestionar tareas y (próximamente) pomodoros y estadísticas.

## ✨ Funcionalidades

- `!addtask <texto>`: añade una tarea a tu lista personal.
- `!tasks`: muestra tus tareas pendientes y completadas.
- `!donetask <n>`: marca una tarea como completada.

## 🛠 Tecnologías

- Python 3.10+
- [discord.py](https://discordpy.readthedocs.io/)
- dotenv para gestionar el token de forma segura

## 🚀 Instalación y ejecución

```bash
git clone https://github.com/TU_USER/discord-productivity-bot.git
cd discord-productivity-bot

python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate

pip install -r requirements.txt

# Crear archivo .env con tu token de Discord:
# DISCORD_TOKEN=TU_TOKEN_AQUI

python -m src.bot
