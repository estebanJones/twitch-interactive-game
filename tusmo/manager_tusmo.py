from . import start_tusmo
from . import join_motus
import webbrowser
import time

min_call_freq = 30
used = {}

async def process_command(command, ctx):
    if (command not in used or time.time() - used[command] > min_call_freq):
        used[command] = time.time()
        await start_game(ctx)
    else:
        await cooldown(command, ctx)

async def start_game(ctx):
    start = start_tusmo.start_motus()
    shortId = start['data']['startMotus']['shortId']
    data = join_motus.join_motus(shortId, "1593d7d09ae39510b762e6b001")

    url = "https://www.tusmo.xyz/{}".format(shortId)
    webbrowser.open_new_tab(url)
    await ctx.send("Une nouvelle partie à commencer. Création impossible pendant 30 secondes")

async def cooldown(command, ctx):
    answer = 'Vous avez utilisé la commande "{}" dans les {} secondes.'.format(command, min_call_freq)
    await ctx.send(answer)