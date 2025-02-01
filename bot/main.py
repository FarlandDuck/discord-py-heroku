import os
import discord
import random
import json
import statistics
import difflib
from discord import app_commands
from discord.ext import commands

TOKEN = os.getenv('DISCORD_TOKEN')

# Enable bot intents
intents = discord.Intents.default()
intents.message_content = True

# Create bot instance
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
        container_data[data["nickname"].lower()] = data  # Store by lowercase nickname

# Event: Bot is Ready
@bot.event
async def on_ready():
    await bot.tree.sync()  # Sync slash commands
    print(f'{bot.user.name} is now online!')

# Slash Command: Collection Simulation
@bot.tree.command(name="collection", description="Simulates the number of containers needed to complete a collection.")
@app_commands.describe(
    total_items="Total number of items in the collection",
    owned_items="Number of items you already own",
    duplicates="Number of duplicate items",
    conversion_cost="Number of duplicates needed to convert into an item"
)
async def collection(interaction: discord.Interaction, total_items: int, owned_items: int, duplicates: int, conversion_cost: int):
    """Simulates collection completion"""
    
    # Input validation
    if total_items > 100 or total_items <= 0:
        await interaction.response.send_message("Total items must be between 1 and 100.", ephemeral=True)
        return
    if owned_items > total_items or owned_items < 0:
        await interaction.response.send_message("Owned items must be between 0 and the total items.", ephemeral=True)
        return
    if duplicates < 0:
        await interaction.response.send_message("Duplicates cannot be negative.", ephemeral=True)
        return
    if conversion_cost <= 0:
        await interaction.response.send_message("Conversion cost must be 1 or higher.", ephemeral=True)
        return

    runs = 100000
    total_containers = 0
    results = []

    for _ in range(runs):
        collection = [-1] * (total_items - owned_items) + [1] * owned_items
        containers = 0
        dupes = duplicates
        empties = total_items - owned_items

        while empties > 0:
            containers += 1
            index = random.randint(0, total_items - 1)
            if collection[index] == 1:
                dupes += 1
            else:
                collection[index] = 1
                empties -= 1

            if dupes // conversion_cost >= empties:
                break

        total_containers += containers
        results.append(containers)

    results.sort(reverse=True)
    stdev = statistics.pstdev(results)

    percentiles = [0.0015, 0.025, 0.16, 0.5, 0.84, 0.975, 0.9985]
    percentile_values = [results[int(p * runs)] for p in percentiles]

    response = f"```\n"
    response += f"Average containers needed: {total_containers / runs:.1f}\n"
    response += f"Standard deviation: {stdev:.1f} containers.\n"
    response += f"Expected range: {percentile_values[6]} - {percentile_values[0]} containers.\n"

    labels = ["0.15%", "2.5%", "16%", "50% (Median)", "84%", "97.5%", "99.85%"]
    for label, value in zip(labels, percentile_values):
        response += f"At {label} percentile: {value}\n"
    
    response += "```"
    await interaction.response.send_message(response)

# Slash Command: Open Container
@bot.tree.command(name="open", description="Open a container and receive a drop.")
@app_commands.describe(container_name="Name of the container to open")
@app_commands.choices(container_name=[app_commands.Choice(name=name, value=name) for name in container_data.keys()])
async def open_container(interaction: discord.Interaction, container_name: str):
    """Simulates opening a container"""
    
    # Find closest matching container
    matched_name = difflib.get_close_matches(container_name.lower(), container_data.keys(), n=1, cutoff=0)
    if not matched_name:
        await interaction.response.send_message("Invalid container name. Use `/help` to see available containers.", ephemeral=True)
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
   
