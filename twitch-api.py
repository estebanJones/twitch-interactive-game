from twitchio.ext import commands
import pyautogui
import time
from tusmo import manager_tusmo

class Bot(commands.Bot):
    nbTryWord = 0

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        super().__init__(token='TOKEN', prefix='!', initial_channels=['interact_me'])
        

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    @commands.command()
    async def hello(self, ctx: commands.Context):
        await self.send_message(ctx, f'Hello {ctx.author.name}!')

    @commands.command()
    async def start(self, ctx: commands.Context):
        await manager_tusmo.process_command("start", ctx)

    # WRITE LETTER COMMAND
    @commands.command()
    async def w(self, ctx: commands.Context, letter):
        if(len(letter) == 1):
            pyautogui.press(letter)
            answer = '{} a proposé la lettre {}!'.format(ctx.author.name, letter)
            await self.send_message(ctx, answer)
            await self.thinking_await(ctx)
    
    # ONE-SHOT WORD COMMAND
    @commands.command()
    async def os(self, ctx: commands.Context, word):
        if(len(word) >= 4 and len(word) < 10):
            if(word.lower() != 'enter'):
                arrayWord = list(word)
                for letter in arrayWord:
                    pyautogui.press(letter)
                
                answer = '{} tente un oneshot avec le mot {}!'.format(ctx.author.name, word)
                await self.send_message(ctx, answer)
                pyautogui.press('enter')
                await self.thinking_await(ctx)

     # Validate word
    @commands.command()
    async def valid(self, ctx: commands.Context):
        pyautogui.press('enter')
        await self.send_message(ctx, 'Touche "Entrée" invoquée')

     # Validate word
    @commands.command()
    async def tab(self, ctx: commands.Context):
        pyautogui.press('tab')
        await self.send_message(ctx, 'Touche "Tab" invoquée')

     # Validate word
    @commands.command(aliases="del")
    async def delete(self, ctx: commands.Context, nombre):
        print("nombre {}".format(int(nombre)))
        for i in range(int(nombre)):
            print("i {}".format(i))
            pyautogui.press('delete')
            
        await self.send_message(ctx, 'Touche "Del" invoquée')
        
    # SEND MESSAGE WITH TWITCH API
    async def send_message(self, ctx: commands.Context, answer):
        await ctx.send(answer)

    # WAIT TO LIMIT FLOOD AS thinking_await
    async def thinking_await(self, ctx: commands.Context):
        answer = 'Je vous laisse, 3 secondes de réfléxion. Inutile de flood.'
        await self.send_message(ctx, answer)

        time.sleep(3)

        answer = 'Délais de réflexion terminé. J\'attends vos propositions'
        await self.send_message(ctx, answer)

    # SEND MESSAGE WITH TWITCH API
    async def send_message(self, ctx: commands.Context, answer):
        await ctx.send(answer)

    
    

bot = Bot()
bot.run()
