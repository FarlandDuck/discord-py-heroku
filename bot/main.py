import os
import discord
import random
import json
import difflib
import io
from discord.ext import commands
import matplotlib.pyplot as plt
import numpy as np

TOKEN = os.getenv('DISCORD_TOKEN')

# Setup intents
intents = discord.Intents.default()
intents.message_content = True

# Create bot instance without the default help command
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

# Directory where container JSON files are stored
CONTAINER_FOLDER = "containers"

# Load all container data dynamically
container_data = {}

for filename in os.listdir(CONTAINER_FOLDER):
    if filename.endswith(".json"):  # Only process JSON files
        file_path = os.path.join(CONTAINER_FOLDER, filename)
        with open(file_path, "r", encoding="utf-8") as f:
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
    embed.add_field(name="`!collection [total items] [owned items] [owned duplicates] [duplicate to item conversion cost]`", value="Simulates the number of containers needed to complete a collection.", inline=False)
    embed.add_field(name="`!open [container name]`", value="Opens a container and gives a random drop.", inline=False)
    embed.add_field(name="`!info`", value="Lists all available containers.", inline=False)
    embed.add_field(name="`!help`", value="Displays this help message.", inline=False)

    await ctx.send(embed=embed)

# Command: Collection Simulation
@bot.command(name="collection")
async def collection(ctx, n: int = None, k: int = None, d: int = None, c: int = None):
    """Simulates the number of containers needed to complete a collection."""

    # If no arguments provided, show usage instruction
    if n is None or k is None or d is None or c is None:
        await ctx.send("Usage: `!collection [total items] [owned items] [owned duplicates] [duplicate to item conversion cost]`")
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

    # Add contextual information in a legend box
    info_text = (
        f"Total Items in Collection: {n}\n"
        f"Items Owned: {k}\n"
        f"Duplicates Owned: {d}\n"
        f"Duplicate Conversion Rate: {c}"
    )
    plt.annotate(
        info_text,
        xy=(0.98, 0.02), xycoords='axes fraction',
        fontsize=10, color='black', ha='right', va='bottom',
        bbox=dict(boxstyle="round,pad=0.5", edgecolor='black', facecolor='white')
    )

    # Save the plot to a BytesIO object
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='png', bbox_inches='tight')
    img_buffer.seek(0)

    # Close the plot
    plt.close()

    # Create a file to send as an attachment
    file = discord.File(img_buffer, filename="collection_simulation.png")

    # Send only the image file
    await ctx.send(file=file)

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

    drop_pool = container["drops"]  # Initial drop pool
    roll = random.uniform(0, 100)  # Generate a random roll
    last_rate = 100  # Used to track probability distribution

    # Traverse drop pools properly
    while True:
        # Check if drop pool uses custom rates
        if "rate" in drop_pool[0]:
            cumulative_rate = 0
            for i, drop in enumerate(drop_pool):
                cumulative_rate += drop["rate"]
                if roll <= cumulative_rate:  # Select the correct drop
                    selected_drop = drop
                    break
        else:
            # Even distribution
            selected_drop = random.choice(drop_pool)

        # If the selected drop has sub-drops (nested pool), continue traversal
        if "drops" in selected_drop:
            drop_pool = selected_drop["drops"]
            roll = random.uniform(0, 100)  # Re-roll for next layer
        else:
            break  # We've reached the final item

    # Embed the result
    embed.description = selected_drop["name"]
    if "link" in selected_drop:
        embed.set_image(url=selected_drop["link"])

    await ctx.send(embed=embed)

# Run the bot
bot.run(TOKEN)
