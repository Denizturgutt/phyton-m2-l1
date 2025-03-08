import aiohttp  # Eşzamansız HTTP istekleri için bir kütüphane
import random
import asyncio

class Pokemon:
    pokemons = {}
    # Nesne başlatma (kurucu)
    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = random.randint(1, 1000)
        self.name = None
        if pokemon_trainer not in Pokemon.pokemons:
            Pokemon.pokemons[pokemon_trainer] = self
        else:
            self = Pokemon.pokemons[pokemon_trainer]

    async def get_name(self):
        # PokeAPI aracılığıyla bir pokémonun adını almak için eşzamansız bir yöntem
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API'si
        async with aiohttp.ClientSession() as session:  # Bir HTTP oturumu açma
            async with session.get(url) as response:  # GET isteği gönderme
                if response.status == 200:
                    data = await response.json()  # JSON yanıtının alınması ve kodunun çözülmesi
                    return data['forms'][0]['name']  # Bir Pokémon'un adını döndürme
                else:
                    return "Pikachu"  # İstek başarısız olursa varsayılan adı döndürür

    async def info(self):
        # Pokémon hakkında bilgi döndüren bir metot
        if not self.name:
            self.name = await self.get_name()  # Henüz yüklenmemişse bir adın geri alınması
            self.hp = await self.get_hp()
            self.attack = await self.get_attack()
            self.superattack = await self.get_superattack()
            
        return f"Pokémonunuzun ismi: {self.name}\nPokémonunuzun canı: {self.hp}\nPokémonunuzun atak: {self.attack}\nPokémonunuzun süperatak:{self.superattack}\n "  # Pokémon'un adını içeren dizeyi döndürür

    async def show_img(self):
        # PokeAPI aracılığıyla bir pokémon görüntüsünün URL'sini almak için eşzamansız bir yöntem
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API'si
        async with aiohttp.ClientSession() as session:  # Bir HTTP oturumu açma
            async with session.get(url) as response:  # GET isteği gönderme
                if response.status == 200:
                    data = await response.json()  # JSON yanıtının alınması ve kodunun çözülmesi
                    return data['sprites']['front_default']  # Bir Pokémon'un adını döndürme
                else:
                    return "Error"  # İstek başarısız olursa varsayılan adı döndürür
                
    async def get_hp(self):
        # PokeAPI aracılığıyla bir pokémon görüntüsünün URL'sini almak için eşzamansız bir yöntem
            url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API'si
            async with aiohttp.ClientSession() as session:  # Bir HTTP oturumu açma
                async with session.get(url) as response:  # GET isteği gönderme
                    if response.status == 200:
                        data = await response.json()  # JSON yanıtının alınması ve kodunun çözülmesi
                        return data['stats'][0]['base_stat'] * 5 # Bir Pokémon'un adını döndürme
                    else:
                        return "Error"  # İstek başarısız olursa varsayılan adı döndürür
                
    async def get_attack(self):
        # PokeAPI aracılığıyla bir pokémon görüntüsünün URL'sini almak için eşzamansız bir yöntem
            url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API'si
            async with aiohttp.ClientSession() as session:  # Bir HTTP oturumu açma
                async with session.get(url) as response:  # GET isteği gönderme
                    if response.status == 200:
                        data = await response.json()  # JSON yanıtının alınması ve kodunun çözülmesi
                        return data['stats'][1]['base_stat']  # Bir Pokémon'un adını döndürme
                    else:
                        return "Error"  # İstek başarısız olursa varsayılan adı döndürür
    async def get_superattack(self):
        # PokeAPI aracılığıyla bir pokémon görüntüsünün URL'sini almak için eşzamansız bir yöntem
            url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API'si
            async with aiohttp.ClientSession() as session:  # Bir HTTP oturumu açma
                async with session.get(url) as response:  # GET isteği gönderme
                    if response.status == 200:
                        data = await response.json()  # JSON yanıtının alınması ve kodunun çözülmesi
                        return data['stats'][3]['base_stat']  # Bir Pokémon'un adını döndürme
                    else:
                        return "Error"  # İstek başarısız olursa varsayılan adı döndürür                

    async def  attack1(self,enemy):
        if enemy.hp>self.attack:
            enemy.hp -= self.attack
            return f"{self.name} saldırdı {self.attack} hasar verdi. {enemy.name} {enemy.hp} canı kaldı."
        else:
            return f"{self.name} saldırdı {self.attack} hasar verdi. {enemy.name} kaybetti."


class Fighter(Pokemon):
    pass
class Wizard(Pokemon):
    pass   












if __name__=="__main__":

    async def sad():   

        trainer1 = Fighter("blazeer")
        trainer2 = Wizard("blazer")
        print(await trainer1.info())
        print(await trainer2.info())
        print("---------------------------------------")
        print(await trainer1.attack1(enemy=trainer2))
        print(await trainer2.attack1(enemy=trainer1))
    asyncio.run(sad())
