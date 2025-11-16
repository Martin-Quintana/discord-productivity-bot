from discord.ext import commands

tasks_by_user = {}

def setup_tasks(bot: commands.Bot):

    @bot.command(name="addtask")
    async def add_task(ctx, *, description: str):
        user_id = ctx.author.id
        tasks_by_user.setdefault(user_id, [])
        tasks_by_user[user_id].append({"desc": description, "done": False})
        await ctx.send(f"✅ Tarea añadida: **{description}**")

    @bot.command(name="tasks")
    async def list_tasks(ctx):
        user_id = ctx.author.id
        tasks = tasks_by_user.get(user_id, [])
        if not tasks:
            await ctx.send("📭 No tienes tareas pendientes.")
            return

        lines = []
        for i, t in enumerate(tasks, start=1):
            status = "✅" if t["done"] else "🕒"
            lines.append(f"{i}. {status} {t['desc']}")

        await ctx.send("\n".join(lines))

    @bot.command(name="donetask")
    async def done_task(ctx, index: int):
        user_id = ctx.author.id
        tasks = tasks_by_user.get(user_id, [])
        if 1 <= index <= len(tasks):
            tasks[index - 1]["done"] = True
            await ctx.send(f"👌 Marcada como completada: **{tasks[index - 1]['desc']}**")
        else:
            await ctx.send("❌ Índice de tarea no válido.")
