import discord
from discord.ext import commands
from config import token
from logic import Pokemon
from main import Pokemon,Wizard,Fighter
import random


# Bot için niyetleri (intents) ayarlama
intents = discord.Intents.default()  # Varsayılan ayarların alınması
intents.messages = True              # Botun mesajları işlemesine izin verme
intents.message_content = True       # Botun mesaj içeriğini okumasına izin verme
intents.guilds = True                # Botun sunucularla (loncalar) çalışmasına izin verme

# Tanımlanmış bir komut önekine ve etkinleştirilmiş amaçlara sahip bir bot oluşturma
bot = commands.Bot(command_prefix='!', intents=intents)

# Bot çalışmaya hazır olduğunda tetiklenen bir olay
@bot.event
async def on_ready():
    print(f'Giriş yapıldı:  {bot.user.name}')  # Botun adını konsola çıktı olarak verir

# '!go' komutu
@bot.command()
async def go(ctx):
    author = ctx.author.name  # Mesaj yazarının adını alma
    # Kullanıcının zaten bir Pokémon'u olup olmadığını kontrol edin. Eğer yoksa, o zaman...
    if author not in Pokemon.pokemons.keys():
        x = random.randint(0,2)
        if 0 == x:
            pokemon = Pokemon(author)
        if 1 == x:
            pokemon = Wizard(author)  
        if 2 == x:
            pokemon = Fighter(author) 
            
        await ctx.send(await pokemon.info())  # Pokémon hakkında bilgi gönderilmesi
        image_url = await pokemon.show_img()  # Pokémon resminin URL'sini alma
        if image_url:
            embed = discord.Embed()  # Gömülü mesajı oluşturma
            embed.set_image(url=image_url)  # Pokémon'un görüntüsünün ayarlanması
            await ctx.send(embed=embed)  # Görüntü içeren gömülü bir mesaj gönderme
        else:
            await ctx.send("Pokémonun görüntüsü yüklenemedi!")
    else:
        await ctx.send("Zaten kendi Pokémonunuzu oluşturdunuz!")  # Bir Pokémon'un daha önce yaratılıp yaratılmadığını gösteren bir mesaj
# Botun çalıştırılması

@bot.command()
async def info():
    author = ctx.author.name
    if author in Pokemon.pokemons:
        pokemon =  Pokemon.pokemons[author]
        await ctx.send(await pokemon.info())
    else:
        await ctx.send("Pokemon yok sende")
@bot.command()
async def attack(ctx,target):
    author = author.ctx.name
    if target in Pokemon.pokemons and author  in  Pokemon.pokemons:
        pokemon = Pokemon.pokemons [author]
        enemy = Pokemon.pokemons [target]
        await ctx.send(await pokemon.attack1(enemy))

    else:
        await ctx.send(f"Senin Poğemonun yoğ")


        
        




bot.run(token)
