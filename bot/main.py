import os
import discord
import random
import json
import statistics
import difflib
from discord.ext import commands

TOKEN = os.getenv('DISCORD_TOKEN')

# Setup intents
intents = discord.Intents.default()
intents.message_content = True

# Create a bot instance with command prefix "!"
bot = commands.Bot(command_prefix="!", intents=intents)

# Load container data
container_files = [
    "Supercontainer.json", "SantasGift2021.json", "SantasBigGift2021.json", 
    "SantasMegaGift2021.json", "SantasGift2022.json", "SantasBigGift2022.json", 
    "SantasMegaGift2022.json", "SantasGift2023.json", "SantasBigGift2023.json", 
    "SantasMegaGift2023.json", "SantasGift2024.json", "SantasMegaGift2024.json"
]

container_data = {}
for filename in container_files:
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        container_data[data["nickname"].lower()] = data  # Store by lowercase nickname for easy lookup

# Bot Ready Event
@bot.event
async def on_ready():
    await bot.tree.sync()  # Force sync
    print(f'{bot.user.name} has connected to Discord!')

# Command: Collection Simulation
@bot.command(name="collection")
async def collection(ctx, n: int, k: int, d: int, c: int):
    """Simulates the number of containers needed to complete a collection."""
    
    # Input validation
    if n > 100 or n <= 0:
        await ctx.send("There must be between 1 and 100 items in a collection.")
        return
    if k > n or k < 0:
        await ctx.send("The number of owned items must be between 0 and the total number of items.")
        return
    if d < 0:
        await ctx.send("Duplicates cannot be negative.")
        return
    if c <= 0:
        await ctx.send("Conversion cost of duplicates must be 1 or higher.")
        return

    runs = 100000
    total_containers = 0
    results = []

    for _ in range(runs):
        collection = [-1] * (n - k) + [1] * k
        containers = 0
        dupes = d
        empties = n - k

        while empties > 0:
            containers += 1
            index = random.randint(0, n - 1)
            if collection[index] == 1:
                dupes += 1
            else:
                collection[index] = 1
                empties -= 1

            if dupes // c >= empties:
                break

        total_containers += containers
        results.append(containers)

    results.sort(reverse=True)
    stdev = statistics.pstdev(results)

    # Generate response
    percentiles = [0.0015, 0.025, 0.16, 0.5, 0.84, 0.975, 0.9985]
    percentile_values = [results[int(p * runs)] for p in percentiles]

    response = f"```\n"
    response += f"On average, you will need to open {total_containers / runs:.1f} containers.\n"
    response += f"Standard deviation: {stdev:.1f} containers.\n"
    response += f"Expected range: {percentile_values[6]} - {percentile_values[0]} containers.\n"
    
    labels = ["0.15%", "2.5%", "16%", "50% (Median)", "84%", "97.5%", "99.85%"]
    for label, value in zip(labels, percentile_values):
        response += f"At {label} percentile: {value}\n"
    
    response += "```"
    await ctx.send(response)

# Command: Info
@bot.command(name="info")  # Change the command name
async def info(ctx):
    """Provides info message for available containers."""
    await ctx.send(f"Use `!open [container name]`. Available containers: {', '.join(sorted(container_data.keys()))}")

# Command: Open Container
@bot.command(name="open")
async def open_container(ctx, *, container_name: str):
    """Simulates opening a container and getting a random drop."""
    
    # Find best matching container name
    matched_name = difflib.get_close_matches(container_name.lower(), container_data.keys(), n=1, cutoff=0)
    if not matched_name:
        await ctx.send("Invalid container name. Use `!info` to see available containers.")
        return

    container = container_data[matched_name[0]]
    
    # Embed for Discord message
    embed = discord.Embed(title=container["name"], color=discord.Color.from_str(container["color"]))
    
    drop_pool = container["drops"]
    roll = random.uniform(0, 100)
    drop_index = 0
    last_rate = 100

    # Determine the drop
    while "drops" in drop_pool[drop_index]:
        drop_pool = drop_pool[drop_index]["drops"]
        roll = random.uniform(0, 100)
        drop_index = 0

    if "rate" in drop_pool[0]:  # Manual rate distribution
        while roll >= 0:
            roll -= drop_pool[drop_index]["rate"] / 100 * last_rate
            drop_index += 1
    else:  # Even distribution
        drop_index = int(roll // (last_rate / len(drop_pool)))

    drop = drop_pool[drop_index]

    # Embed the result
    embed.description = drop["name"]
    if "link" in drop:
        embed.set_image(url=drop["link"])

    await ctx.send(embed=embed)

# Run the bot
import asyncio

async def main():
    async with bot:
        await bot.start(TOKEN)

asyncio.run(main())

