import os
import discord
import random
import json
import statistics
import difflib
from discord.ext import commands
import matplotlib.pyplot as plt
import numpy as np

TOKEN = os.getenv('DISCORD_TOKEN')

# Setup intents
intents = discord.Intents.default()
intents.message_content = True

# Create bot instance without the default help command
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

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
    print(f'{bot.user.name} has connected to Discord!')

# Custom Help Command
@bot.command(name="help")
async def custom_help(ctx):
    """Provides a cleaner help message."""
    embed = discord.Embed(
        title="Available Commands",
        description="Here are the available commands for the bot:",
        color=discord.Color.blue()
    )
    embed.add_field(name="`!collection [total] [owned] [dupes] [cost]`", value="Simulates the number of containers needed to complete a collection.", inline=False)
    embed.add_field(name="`!open [container_name]`", value="Opens a container and gives a random drop.", inline=False)
    embed.add_field(name="`!info`", value="Lists all available containers.", inline=False)
    embed.add_field(name="`!help`", value="Displays this help message.", inline=False)

    await ctx.send(embed=embed)

# Command: Collection Simulation
@bot.command(name="collection")
async def collection(ctx, n: int = None, k: int = None, d: int = None, c: int = None):
    """Simulates the number of containers needed to complete a collection."""

    # If no arguments provided, show usage instruction
    if n is None or k is None or d is None or c is None:
        await ctx.send("Usage: `!collection [total_items] [owned_items] [duplicates] [conversion_cost]`")
        return
    
    if n > 100 or n <= 0 or k > n or k < 0 or d < 0 or c <= 0:
        await ctx.send("Invalid input values. Please check the command usage.")
        return

    runs = 100000
    results = []

    for _ in range(runs):
        collection = [-1] * (n - k) + [1] * k
        containers = 0
        dupes = d
        empties = n - k

        while empties > 0:
            containers += 1
            index = np.random.randint(0, n)
            if collection[index] == 1:
                dupes += 1
            else:
                collection[index] = 1
                empties -= 1

            if dupes // c >= empties:
                break

        results.append(containers)

    results.sort()
    percentiles = np.linspace(0, 100, len(results))

    # Generate the plot
    plt.figure(figsize=(10, 5))
    plt.plot(percentiles, results, label="Number of Containers Needed", color='b')
    plt.xlabel("Percentile of Players")
    plt.ylabel("Number of Containers Opened")
    plt.title("Containers Needed to Complete a Collection by Percentile")
    plt.grid(True)
    plt.legend()

    # Save the plot to a BytesIO object
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)

    # Close the plot
    plt.close()

    # Create a file to send as an attachment
    file = discord.File(img_buffer, filename="collection_simulation.png")

    await ctx.send("Percentile Graph:", file=file)

# Command: Info
@bot.command(name="info")
async def info(ctx):
    """Lists available containers."""
    await ctx.send(f"Use `!open [container name]`. Available containers: {', '.join(sorted(container_data.keys()))}")

# Command: Open Container
@bot.command(name="open")
async def open_container(ctx, *, container_name: str = None):
    """Simulates opening a container and getting a random drop."""

    # If no container name is provided
    if container_name is None:
        await ctx.send("Usage: `!open [container_name]`\nUse `!info` to see available containers.")
        return

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
bot.run(TOKEN)
