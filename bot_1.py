import random
import discord
from discord.ext import commands
from discord.ui import View, Button

# try :
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

#List of trash can

trash_list_o = ['Leaf', 'fruit', 'Dirt']

trash_list_a = ['Plastic', 'Bottle', 'Tissue']

trash_list_b = ['Battery', 'Lamp', 'Drug']

#on command

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

#Hello

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

# =========================
#   RPS BUTTON VIEW
# =========================

class RPSView(View):
    def __init__(self, player_vs=None, challenger=None):
        super().__init__(timeout=20)
        self.player_vs = player_vs     # lawan
        self.challenger = challenger   # penantang
        self.result = {}               # simpan pilihan

    # Remove button after choose
    async def disable_all(self):
        for child in self.children:
            child.disabled = True

    async def process(self, interaction: discord.Interaction, player_choice):
        player = interaction.user

        # Cegah orang lain ikut pencet
        if player != self.challenger and player != self.player_vs:
            return await interaction.response.send_message(
                "Kamu bukan bagian dari game ini!", ephemeral=True
            )

        self.result[player.id] = player_choice

        await interaction.response.send_message(f"Pilihanmu tercatat!", ephemeral=True)

        # Jika mode VS bot
        if self.player_vs == "bot":
            bot_choice = random.choice(["rock", "paper", "scissors"])

            # Tentukan hasil
            player_c = player_choice
            bot_c = bot_choice

            if player_c == bot_c:
                result = "Seri!"
            elif (
                (player_c == "rock" and bot_c == "scissors") or
                (player_c == "paper" and bot_c == "rock") or
                (player_c == "scissors" and bot_c == "paper")
            ):
                result = f"{player.mention} menang! 🎉"
            else:
                result = "Bot menang! 😎"

            await self.disable_all()
            return await interaction.message.edit(
                content=f"**{player.mention} vs Bot**\n\n"
                        f"Kamu: **{player_c}**\nBot: **{bot_c}**\n\n**Hasil:** {result}",
                view=self
            )

        # Jika mode player vs player
        if len(self.result) == 2:  # dua orang sudah memilih
            p1 = self.challenger
            p2 = self.player_vs

            p1_choice = self.result[p1.id]
            p2_choice = self.result[p2.id]

            if p1_choice == p2_choice:
                result = "Seri!"
            elif (
                (p1_choice == "rock" and p2_choice == "scissors") or
                (p1_choice == "paper" and p2_choice == "rock") or
                (p1_choice == "scissors" and p2_choice == "paper")
            ):
                result = f"{p1.mention} menang! 🎉"
            else:
                result = f"{p2.mention} menang! 🎉"

            await self.disable_all()

            await interaction.message.edit(
                content=f"**{p1.mention} vs {p2.mention}**\n\n"
                        f"{p1.mention}: **{p1_choice}**\n"
                        f"{p2.mention}: **{p2_choice}**\n\n"
                        f"**Hasil:** {result}",
                view=self
            )

    # Tombol
    @discord.ui.button(label="🪨 Rock", style=discord.ButtonStyle.secondary)
    async def rock(self, interaction, button):
        await self.process(interaction, "rock")

    @discord.ui.button(label="📄 Paper", style=discord.ButtonStyle.primary)
    async def paper(self, interaction, button):
        await self.process(interaction, "paper")

    @discord.ui.button(label="✂️ Scissors", style=discord.ButtonStyle.danger)
    async def scissors(self, interaction, button):
        await self.process(interaction, "scissors")


# =========================
#       RPS COMMAND
# =========================

@bot.command()
async def rps(ctx, target: str = None):
    # Case 1: main lawan bot
    if target is None or target.lower() == "bot":
        view = RPSView(player_vs="bot", challenger=ctx.author)
        return await ctx.send(f"{ctx.author.mention} bermain melawan **Bot**!\nPilih gerakanmu:", view=view)

    # Case 2: tantang player lain
    # harus mention user
    if len(ctx.message.mentions) == 0:
        return await ctx.send("Kamu harus mention player yang mau kamu tantang!\nContoh: `$rps @nopal`")

    opponent = ctx.message.mentions[0]

    if opponent.bot:
        return await ctx.send("Bot lain tidak bisa ditantang, pilih `$rps bot` untuk main lawan bot!")

    if opponent == ctx.author:
        return await ctx.send("Ga bisa tantang diri sendiri, wkwk!")

    view = RPSView(player_vs=opponent, challenger=ctx.author)
    await ctx.send(
        f"🎮 **Duel RPS Dimulai!**\n"
        f"{ctx.author.mention} menantang {opponent.mention}\n"
        f"Kedua pemain pilih gerakan secara rahasia.",
        view=view
    )


#emotion

@bot.command()
async def smile(ctx):
    await ctx.send(f':D')

@bot.command()
async def cry(ctx):
    await ctx.send(f':_(')

#Calculator

@bot.command()
async def plus(ctx, letter_1, letter_2):
    await ctx.send(int(letter_1) + int(letter_2))

@bot.command()
async def multiply(ctx, number_1, number_2):
    await ctx.send(int(number_1) * int(number_2))

@bot.command()
async def rank_number(ctx, number_1, number_2):
    await ctx.send(int(number_1) ** int(number_2))

#Trash can

@bot.command()
async def trash(ctx):
    await ctx.send('Enter the trash name')
    msg = await bot.wait_for("message")
    if msg.content in trash_list_a:
        await ctx.send('Put it in the inorganic trash')
    elif msg.content in trash_list_o:
        await ctx.send('Put it in the organic trash')
    elif msg.content in trash_list_b:
        await ctx.send('Put it in the dangerous trash can')

#hehehe

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

#Token

bot.run("SECRET TOKEN")
