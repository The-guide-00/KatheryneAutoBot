import discum
import time
import logging
import datetime
import random

#token
bot = discum.Client(token='TOKEN GOES HERE', log=False)

#channel id
channel_id = CHANNEL ID HERE
channel_id_str = str(channel_id)
i=0
banners = ("Albedo","Albedo 2","Albedo 3","Ayaka","Ayaka 2","Ayato","Beginner","Cyno","Eula","Eula 2","Ganyu","Ganyu 2","Ganyu 3","Hu Tao","Hu Tao 2","Itto","Itto 2","Kazuha","Kazuha 2","Keqing","Klee","Klee 2","Klee 3","Kokomi","Kokomi 2","Kokomi 3","Nahida","Nilou","Raiden","Raiden 2","Shenhe","Standard","Tartaglia","Tartaglia 2","Tartaglia 3","Tighnari","Venti","Venti 2","Venti 3","Venti 4","Weapons","Xiao","Xiao 2","Xiao 3","Yae","Yelan","Yoimiya","Yoimiya 2","Yoimiya 3","Zhongli","Zhongli 2","Zhongli 3","Zhongli 4")
now = datetime.datetime.now()
print("initilazation at", (now.strftime('%Y-%m-%d %H:%M:%S')))




def roll():
    now = datetime.datetime.now()
    print("roll started in " + channel_id_str,"at",(now.strftime('%Y-%m-%d %H:%M:%S')))
    #BANNER
    bot.sendMessage("1038290309416763402","*wish BANNER noani")
    time.sleep(18)
    now = datetime.datetime.now()
    print("roll   ended in " + channel_id_str,"at",(now.strftime('%Y-%m-%d %H:%M:%S')))
    



     
@bot.gateway.command
def helloworld(resp):
    if resp.event.ready_supplemental: #ready_supplemental is sent after ready
        user = bot.gateway.session.user
        print("Logged in as {}#{}".format(user['username'], user['discriminator']))
        print("channel_id is " + channel_id_str)
while i == i:
    roll()

bot.gateway.run(auto_reconnect=True)

#note:legit cobbled togther by a bored 15 year old who does not know what he his doing, discord self botting violates discords TOS dont do it if you are dont want your account banned, also sometimes spamming a bot annoys people, keep that in mind
#AND FOR THE LOVE OF GOD DONT POST YOUR DISCORD TOKEN 


