#-*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
from os import urandom
import datetime as dt

from discord.ext.commands import Bot
import discord.ext as ext
import discord
import datetime, re
import asyncio
import base64
import subprocess
import os.path
from math import *
import io
from io import BytesIO
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import requests
import json
from pprint import pprint
import os
import codecs
import ffmpy
import math
import html
import requests
import random
import threading
from urllib.request import urlopen
import urllib.parse
import urllib
import nltk
import asyncio
import google
import youtube_dl
from bs4 import BeautifulSoup
import time
import random
from googlesearch import search
import textwrap
import urbandictionary as ud
import osuapi
def get_syntax_error(e):
    if e.text is None:
        return '```py\n{0.__class__.__name__}: {0}\n```'.format(e)
    return '```py\n{0.text}{1:>{0.offset}}\n{2}: {0}```'.format(e, '^', type(e).__name__)
initial_extensions = [
    'ext.music'
]
prefix="l!"
a=len(prefix)
client = Bot(command_prefix="litaca!",max_messages=65536)
umarbot = discord.Client()
xd=""
enabledosu=True
with open("osuapikey.txt","r") as fi:
    contsent = fi.readlines()
    try:
        xdddd=contsent[0]
    except:
        enabledosu=False
if enabledosu:
    print("osu! api key found... osu! feature enabled")
    xdddd=contsent[0]
    osu = osuapi.osu.OsuApi(key=xdddd,connector=osuapi.connectors.ReqConnector())
else:
    print("osu! api key not found... osu! feature disabled")
@client.command()
async def hello(*args):
    return await client.say("uu")
class LitchErr(Exception):
    pass
class NumberNotText(LitchErr):
    pass
class SomeError(LitchErr):
    pass
def checkpos(ss):
    if ss is None:
    	return 0
    if ss<=0:
        return int(0)
    else:
        return int(ss)
urlaa = "http://pi.michaelbrabec.cz:9010/a/"
@client.event
async def on_ready():
    #await client.change_presence(game=discord.Game(name='Geometry Dash Deadlocked 50%',link="twitch.tv/hikarichizaki",type=1))
    print("Client logged in as ")
    print(client.user.name)
    print(client.user.id)
    print(client.user.id)    
    print('------')
    print(client)
    print("at "+str(dt.datetime.now()))
@client.event
async def on_server_join(server):
    await client.send_message(client.owner,"Someone invited me to `"+server.name+"`")
@client.event
async def on_server_remove(server):
    await client.send_message(client.owner,"Someone removed me from `"+server.name+"`")
    
@client.event
async def on_message(message,retry=-1):
    mcp=message.content
    mc=message.content.lower()
    mh=message.channel
    mau=message.author
    if(message.server==mau):
        ms=mau
    else:
        ms=message.server
    mt=message.timestamp
    ar=client.add_reaction
    edm=client.edit_message
    mm=message.mentions
    m=message.content.startswith
    mmm=list(client.get_all_members())
    with open("unallowed.txt","r") as fi:
        content = fi.readlines() 
    unallowed = [x.strip() for x in content ]
    if(mau.id not in unallowed):
        if enabledosu:
            if mc.startswith(prefix+"osu"):
                oen=osuapi.enums
                args=mcp.split(" ")
                type=args[1]
                b4=args[2]
                usn=mcp[a+10+len(b4):]
                print(usn)
                if type=="user":
                    try:
                        mode=""
                        
                        if b4=="osu" or b4==0:
                            smth=oen.OsuMode.osu
                            mode="osu!standard"
                        elif b4=="taiko" or b4==1:
                            smth=oen.OsuMode.taiko
                            mode="osu!taiko"                    
                        elif b4=="ctb" or b4==2:
                            smth=oen.OsuMode.ctb
                            mode="osu!catch"                    
                        elif b4=="mania" or b4==3:
                            smth=oen.OsuMode.mania
                            mode="osu!mania"                    
                        else:
                            mode="osu!standard"                    
                            smth=oen.OsuMode.std    

                    except Exception:
                        mode="osu!standard"                 
                        smth=oen.OsuMode.osu
                    try:
                        user=osu.get_user(usn,mode=smth)[0]
                        emb = discord.Embed(title=":flag_"+user.country.lower()+": "+user.username+" (ID : "+str(user.user_id)+")", description="**Level : **"+str(user.level)+"\n**Accuracy** : "+str(user.accuracy)+"%", colour=ms.me.color)
                        emb.add_field(name="**Performance Point**",value=str(user.pp_raw),inline=True)
                        emb.add_field(name="Play Counts",value=str(user.playcount),inline=True)
                        emb.add_field(name="Rank Counts",value="**SS** : "+str(checkpos(user.count_rank_ss))+"\n**S** : "+str(checkpos(user.count_rank_s))+"\n**A** : "+str(checkpos(user.count_rank_a)))
                        emb.add_field(name="Leaderboard Ranks",value="**Global PP : **#"+str(user.pp_rank)+"\n**Country PP : **#"+str(user.pp_country_rank),inline=True)
                        emb.set_thumbnail(url="https://a.ppy.sh/"+str(user.user_id))
                        emb.add_field(name="Hit Counts",value="**300** : "+str(user.count300)+"\n**100** : "+str(user.count100)+"\n**50** : "+str(user.count50),inline=True)
                        emb.add_field(name="Score",value="**Total Scores : **"+str(user.total_score)+"\n**Ranked Score : **"+str(user.ranked_score))            
                        await client.send_message(mh,"User info of **"+user.username+"** in mode **"+mode+"**",embed=emb)                
                    except Exception as ex:
                        print(ex)
                        
                        await client.send_message(mh,"**Error** : Internal Error Occured \n```"+str(ex)+"```")                 
                if type=="setuser":
                    l = open("osuusername.txt","r+")
                    content = l.readlines()
                    l.close()
                    
                    xd = [x.strip() for x in content ]            
                    f = open("osuusername.txt","w+")
                    lines=xd
                    for line in lines:
                        if str(mau.id) in line:
                            pass
                        else:
                            f.write(line)
                    f.write(str(mau.id)+"::"+argu+"\n")
                    f.close()
                    await client.send_message(mh,"Your Discord account has been linked to osu! username `"+argu+"`")
                                    

        
        if message.content.startswith(prefix+"sakujes"):
            await client.send_message(mh, "sakuješ "+mcp[a+7:])
        elif message.content.startswith(prefix+"cls"):
            if(not mau.server_permissions.manage_messages):
                await client.send_message(mh,"<@"+str(mau.id)+"> "+", This command is for people that have **MANAGE MESSAGE** only!")
            else:

                await client.send_message(mh,"** **{}** **".format("\n"*150)) #
                        
                    
        elif message.content.startswith(prefix+"setgame "):
            text=mcp[a+8:]        
            if(str(mau.id)!="254214302653743104" and str(mau.id)!="389286877133537290"):
                await client.send_message(mh,"<@"+str(mau.id)+"> "+", This command is for **owner** only!")
            elif "||" in text:
                text2=text.split("||")
                await client.change_presence(game=discord.Game(name=text2[1],type=int(text2[0])))
                await client.send_message(mh,":joy::ok_hand::fire:") #
            else:
                await client.change_presence(game=discord.Game(name=text))
                await client.send_message(mh,":ok_hand:") #            
        elif mc.startswith(prefix+"ping"):
            msg=mcp[a+4:]
            timeb4=dt.datetime.now()
            #pongmsg = await client.send_message(mh, "Pong! *C* **a** *l* **c** *u* **l** *a* **t** *i* **n** *g*")#(timea4-timeb4).total_seconds()*1000)
            pongmsg=await client.send_message(mh,"Pong!")
            timea4=dt.datetime.now()
            dot=""
            #for num in range(1,4):
            #    dot+="."
            #    await client.edit_message(pongmsg, new_content="Pong! (Took {0}ms){1}".format(str(round((random.randint(0,2000)+random.random())*100)/100),dot))
            #    time.sleep(1)
            await client.edit_message(pongmsg, new_content="Pong! (Took **{}**ms) :heart:".format(str(math.ceil(round(((timea4-timeb4).total_seconds()*1000)*100)/100))))
        elif message.content.startswith(prefix+"repeat "):
            if(str(mau.id)!="254214302653743104" and str(mau.id)=="389286877133537290"):
                await client.send_message(mh,"<@"+str(mau.id)+"> "+", This command is for **owner** only!")
            else:
                args=mcp.split(" ")
                times=int(args[1])
                args.pop(0)
                args.pop(0)
                text=" ".join(args)
                for num in range(0,times):
                    time.sleep(0.1)
                    await client.send_message(mh,text)
        elif mc.startswith(prefix+"urban "):
            urbanword=mcp[a+6:]
            defs = ud.define(urbanword)
            stri0=""
            stri1=""
            stri2=""
            stri3=""
            for d in defs:
                stri0=d.word
                stri1=d.definition
                stri2=str(d.upvotes)
                stri3=str(d.downvotes)
                break
            em = discord.Embed(title=stri0, description=stri1, colour=ms.me.color)
            em.add_field(name=":+1: Upvote",value=stri2,inline=True)
            em.add_field(name=":-1: Downvote",value=stri3,inline=True)
            await client.send_message(message.channel, embed=em)
        elif message.content.startswith(prefix+"blacklist "):
            if(str(mau.id)!="254214302653743104" and str(mau.id)=="389286877133537290"):
               await client.send_message(mh,"<@"+str(mau.id)+"> "+", This command is for **owner** only!")
            else:
                user=mcp[a+10:].replace("<","").replace("@","").replace("!","").replace("&","").replace(">","")
                if (user not in unallowed):
                    if(user != "254214302653743104" and user!="389286877133537290"):
                        file = open("unallowed.txt","a") 
                        file.write(str(user)+"\n")
                        file.close()
                        await client.send_message(mh,":ok_hand:")
                    elif(user == "254214302653743104"):
                        await client.send_message(mh,"No owner blacklisting :stuck_out_tongue_winking_eye:")
                    elif(user == "389286877133537290"):
                        await client.send_message(mh,"No self blacklisting :stuck_out_tongue_winking_eye:")
                    else:
                        await client.send_message(mh,"This user is already in a black-list :joy::ok_hand:")
        elif message.content.startswith(prefix+"unblacklist "):
            if(str(mau.id)!="254214302653743104" and str(mau.id)=="389286877133537290"):
               await client.send_message(mh,"<@"+str(mau.id)+"> "+", This command is for **owner** only!")
            else:
                user=mcp[a+12:].replace("<","").replace("@","").replace("!","").replace("&","").replace(">","")
                if (user in unallowed):
                    f = open("unallowed.txt","w")
                    lines=unallowed
                    lines.remove(user)
                    daq=0
                    for line in lines:
                        f.write(line)
                    await client.send_message(mh,":ok_hand:")
                    f.close()
                else:
                    await client.send_message(mh,"This user is not in a black-list :joy::ok_hand:")
        elif message.content.startswith(prefix+"post "):
            if(str(mau.id)!="254214302653743104" and str(mau.id)=="389286877133537290"):
                await client.send_message(mh,"<@"+str(mau.id)+"> "+", This command is for **owner** only!")

                data=mcp.split("|")
                
                r = requests.post(urlaa+"getGJSongInfo.php", data={'songID':i})
                await client.send_message(mh,":ok_hand:")                     
        elif message.content.startswith(prefix+"load "):
            if(str(mau.id)!="254214302653743104" and str(mau.id)=="389286877133537290"):
               await client.send_message(mh,"<@"+str(mau.id)+"> "+", This command is for **owner** only!")
            else:
                cog=mcp[a+5:]
                try:
                    client.load_extension(cog)
                except Exception as e:
                    await client.send_message(mh,'\N{PISTOL}')
                    await client.send_message(mh,'{}: {}'.format(type(e).__name__, e))
                else:
                    await client.send_message(mh,":ok_hand:")
        elif message.content.startswith(prefix+"unload "):
            if(str(mau.id)!="254214302653743104" and str(mau.id)=="389286877133537290"):
               await client.send_message(mh,"<@"+str(mau.id)+"> "+", This command is for **owner** only!")
            else:
                cog=mcp[a+7:]
                try:
                    client.load_extension(cog)
                except Exception as e:
                    await client.send_message(mh,'\N{PISTOL}')
                    await client.send_message(mh,'{}: {}'.format(type(e).__name__, e))
                else:
                    await client.send_message(mh,":ok_hand:")                          
        elif message.content.startswith(prefix+"suggest "):
             suggestion=str(mt)+" UTC : "+str(mau)+" suggested : "+mcp[a+8:]
             file = codecs.open("suggestion.txt","a","utf-8-sig") 
             file.write("\n"+str(suggestion)+"\n")
             file.close()
             await client.send_message(mh,":ok_hand:")
        elif message.content.startswith(prefix+"song "):
            i=mc[a+5:]
            r = requests.post(urlaa+"getGJSongInfo.php", data={'songID':i})
            strx = r.text.split("~|~")
            string='\n'.join(strx)
            gstr = string.replace("1\n","**Song ID : **",1)
            gstr = gstr.replace("\n2\n","\n**Song Name : **",1)
            gstr = gstr.replace("\n3\n","\n**Song Author ID : **",1)
            gstr = gstr.replace("\n4\n","\n**Song Author : **",1)
            gstr = gstr.replace("\n5\n","\n**Song Size : **",1)
            gstr = gstr.replace("\n6\n\n10\n"," MB\n**Song Link : **",1)
            gstr = gstr.replace("\n7\n\n8\n0","\n**Song Banned :** False",1)
            gstr = gstr.replace("\n7\n\n8\n1","\n**Song Banned :** True",1)
            gstr = gstr.replace("\n7","\n**Song Banned :** Please do this command again...",1)
            gstr = gstr.replace("-1","If the song isn't banned, Maybe you are not entering the ID. **I** Can't do that!",1)
            sss=urllib.parse.unquote(gstr)
            await client.send_message(message.channel,sss)
        elif message.content.startswith(prefix+"level "):
            levels = mc[a+6:]
            r = requests.get(urlaa+'/tools/bot/levelSearchBot.php?str='+levels)
            sal=r.content.decode("utf-8")
            await client.send_message(mh,sal)
        elif message.content.startswith(prefix+"whorated "):
            level = mc[a+10:]
            url = urlaa+"/tools/bot/whoRatedBot.php?level="+level
            html = urlopen(url).read()
            soup = BeautifulSoup(html,"html.parser")
            text = soup.get_text()
            await client.send_message(mh,text)
        elif message.content.startswith(prefix+"songup "):
            ids = mc[a+8:]
            r = requests.post(urlaa+"tools/songAdd.php", data={'songlink': ids})
            strex=r.text.replace("<b>Soundcloud links</b> or <b>Direct links</b> or <b>Dropbox links</b> only accepted, <b><font size=\"5\">NO YOUTUBE LINKS</font></b><br><form action=\"songAdd.php\" method=\"post\">Link: <input type=\"text\" name=\"songlink\"><br><input type=\"submit\" value=\"Add Song\"></form>","")
            strex=strex.replace("<b>","**")
            strex=strex.replace("</b><hr>","**")
            await client.send_message(mh,strex)
        elif message.content.startswith(prefix+"b64en "):
            text = mcp[a+6:]
            enc = base64.b64encode(text.encode('ascii')).decode('utf8')
            enc=enc.replace('b\'','**Your Encoded Text : **',1)
            enc=enc.replace('\'','',1)
            await client.send_message(mh,"**Your encoded text : ** `"+enc+"`")
        elif message.content.startswith(prefix+"b64de "):
            text = mcp[a+6:]
            await client.send_message(mh,"**Your decoded text : ** `"+(base64.b64decode(text.encode('utf-8')).decode('utf-8'))+"`")
        elif mc.startswith(prefix+"songreup "):
            await ubot.send_message(mh,"Working in Progress...")
        elif m(prefix+"music "):
            args=mcp[a+6:]
            subcmd=args[1]
            url = args[2]
            if(subcmd=="play"):
                voice=await client.join_voice_channel(channel)
                player = await voice.create_ytdl_player(url)
                player.start()
                
        elif mc.startswith(prefix+"top "):
            tmparr=mc.split(" ")
            types=tmparr[1]
            page=tmparr[2]
            try:
                url = urlaa+"tools/bot/leaderboardsBot.php?type="+types+"&page="+page
                html = urlopen(url).read()
                soup = BeautifulSoup(html,"html.parser")
                text = soup.get_text()
                await client.send_message(mh,text)
            except ValueError:
                print("Error")
        elif mc.startswith(prefix+"player "):
            player=mc[a+7:]
            try:
                url = urlaa+"tools/bot/playerStatsBot.php?player="+player
                html = urlopen(url).read()
                soup = BeautifulSoup(html,"html.parser")
                text = soup.get_text()
                await client.send_message(mh,text)
            except ValueError:
                print("Error")
        elif mc.startswith(prefix+"sayd"):
            msg=mcp[a+5:]
            
            if(msg.strip()==""):
                msg="Attachments : "
            try:

                if message.attachments!=[]:
                
                    url=(message.attachments[0])['url']                    
                    spl=url.split("/")
                    dot=url.split(".")
                    resp = requests.get(url, stream=True)
                    objxd = io.BytesIO(resp.content)                
                    await client.delete_message(message)                    
                    await client.send_file(mh,content=msg,fp=objxd,filename=spl[len(spl)-1])
                else:
                    await client.delete_message(message)                
                    await client.send_message(mh,content=msg)                    
                    
            except discord.errors.Forbidden as ex:
                await client.send_message(mau,content=msg)                

        elif mc.startswith(prefix+"say"):
            msg=mcp[a+4:]
            
            if(msg.strip()==""):
                msg="Attachments : "
            try:

                if message.attachments!=[]:
                
                    url=(message.attachments[0])['url']                    
                    spl=url.split("/")
                    dot=url.split(".")
                    resp = requests.get(url, stream=True)
                    objxd = io.BytesIO(resp.content)                                  
                    await client.send_file(mh,content=msg,fp=objxd,filename=spl[len(spl)-1])
                else:             
                    await client.send_message(mh,content=msg)                    
                    
            except discord.errors.Forbidden as ex:
                await client.send_message(mau,content=msg)   
##        elif mc.startswith(prefix+"eval "):
##            if(str(mau.id)!="254214302653743104" or str(mau.id)!="389286877133537290"):
##                await client.send_message(mh,"<@"+str(mau.id)+"> "+", This command is for **owner** only!")
##            else:
##                try:    
##                    env = {
##                        'client': client,
##                        'channel': message.channel,
##                        'author': message.author,
##                        'server': message.server,
##                        'message': message,
##                    }
##                    env.update(globals())
##                    to_compile = 'async def func():\n%s' % textwrap.indent(mcp.replace("```","").strip(prefix+"eval"), '    ')
##                    try:
##                        exec(to_compile, env)
##                    except SyntaxError as e:
##                        return await client.send_message(message.channel, get_syntax_error(e))
##                    func = env['func']
##                    try:
##                        await func()
##                    except Exception as e:
##                        await client.send_message(mh, "{}:{}".format(type(e).__name__, e))
##                except Exception as e:
##                        pass
        elif mc.startswith(prefix+"google "):
            stri = mcp[a+7:]
            for url in search(stri, tld='com', lang='en', stop=1,num=1,pause=0.25):
                await client.send_message(mh,url)
                break
        elif mc.startswith(prefix+"youtube "):
            stri = mcp[a+8:]

            xxx=youtubesrc(stri)      
            #embeds=discord.Embed(title=youtubetitle(xxx),description=youtubedesc(xxx))
            await client.send_message(mh,youtubesrc(stri))
        elif mc.startswith(prefix+"give "): 
            cmdargs=mcp.split(" ")
            name=""
            with open("items.json", "r") as file:
            
                data = json.load(file)
            
            amount="1"
            iid=""
            ori=cmdargs[2]
            cmdargs[2]=cmdargs[2].replace("minecraft:","")

            itemdat="0"
            for i in data:                    
                if len(cmdargs) == 3:
                    if str(i['type']) == cmdargs[2] or str(i['text_type']) == cmdargs[2]:
                        name=i['name']
                        iid=str(i['type'])
                        #define item name stuff
                        break
                elif len(cmdargs) == 4:
                    if str(i['type']) == cmdargs[2] or str(i['text_type']) == cmdargs[2]:
                        amount=cmdargs[3]
                        iid=str(i['type'])
                        name=i['name']
                        break
                elif len(cmdargs) >= 5:
                    if (str(i['type']) == cmdargs[2] or str(i['text_type']) == cmdargs[2]) and str(i['meta']) == cmdargs[4]:
                        amount=cmdargs[3]
                        itemdat=str(i['meta'])
                        iid=str(i['type'])
                        name=i['name']
                        break
            if cmdargs[1]=="@p":
                usn=mau.name
            elif cmdargs[1]=="@a":
                usn="everyone"
            elif cmdargs[1]=="@e":
                usn="everything"
            elif cmdargs[1]=="@r":
                usn=random.choice(mmm).name
            elif message.mentions!=[]:
                    usn=message.mentions[0].name
            else:
                usr = ms.get_member_named(cmdargs[1])                
                usn=usr.name
            if (name!=""and 0<int(amount)<=64):
                dir_path = os.path.dirname(os.path.realpath(__file__))
                await client.send_file(mh,dir_path+"/items/"+iid+"-"+itemdat+".png",filename=iid+"-"+itemdat+".png",content="Given ["+name+"] * "+amount+" to "+usn)
            elif(int(amount)<=0 or int(amount) >64):
                await client.send_message(mh,"Invalid amount "+amount+", It should be in range 1-64")
            elif(name==""):
                await client.send_message(mh,"Invalid item ID `"+ori+"`:"+itemdat)   
            else:
                await client.send_message(mh,"Usage : "+prefix+"give <player> <item> <amount> <metadata> [data]")                
        elif mc.startswith(prefix+"summon "):
            cmdargs=mcp.split(" ")
            name=""
            with open("entities.json", "r") as file:
                data = json.load(file)
            iid=""
            issummonable=0
            cmdargs[1]=cmdargs[1].lower().replace("minecraft:","")
            usr = discord.utils.get(message.server.members, id=cmdargs[1].replace("@","").replace("!","").replace("&","").replace(">","").replace("<",""))
            for i in data:                    
                if len(cmdargs) == 2:
                    if str(i['type']) == cmdargs[1] or str(i['text_type']) == cmdargs[1]:
                        name=i['name']
                        iid=str(i['type'])
                        issummonable=1
                        #define item name stuff
                        break
                if len(cmdargs) == 3:
                    if (str(i['type']) == cmdargs[1] or str(i['text_type']) == cmdargs[1]) and cmdargs[2]!=0:
                        name=i['name']
                        iid=str(i['type'])
                        issummonable=1
                        #define item name stuff
                        break
                if len(cmdargs) == 4:
                    if (str(i['type']) == cmdargs[1] or str(i['text_type']) == cmdargs[1]) and cmdargs[2]!=0 and cmdargs[3]!=0:
                        name=i['name']
                        iid=str(i['type'])
                        issummonable=1
                        #define item name stuff
                        break
                if len(cmdargs) == 5:
                    if (str(i['type']) == cmdargs[1] or str(i['text_type']) == cmdargs[1]) and cmdargs[2]!=0 and cmdargs[3]!=0 and cmdargs[4]!=0:
                        name=i['name']
                        iid=str(i['type'])
                        issummonable=1
                        #define item name stuff
                        break
                usn=random.choice(mmm).name               
            if (name!=""and issummonable==1):
                dir_path = os.path.dirname(os.path.realpath(__file__))
                await client.send_file(mh,dir_path+"/entities/"+iid+".png",filename=iid+".png",content="Object Summoned (Entity : {})".format(name))
            else:
                await client.send_message(mh,"Usage : "+prefix+"summon <Entity> <x> <y> <z> [data]")

        elif mc.startswith(prefix+"help -c"):
            msg=mc.split(" ")
            index=0
            if len(msg)>=3:
                index=int(msg[2])-1
            F = open('litchbot.txt', 'r')
            await client.send_message(mh,F.read().split("|")[index])
            F.close()            
        elif mc.startswith(prefix+"help"):
            msg=mc.split(" ")
            index=0
            if len(msg)>=2:
                index=int(msg[1])-1
            F = open('litchbot.txt', 'r')
            await client.send_message(mau,F.read().split("|")[index])
            await client.send_message(mh,"Okay! Send help thru your DM! Check it :D")        
            F.close()         
        elif mc.startswith(prefix+"touhou"):
            F = open('iosys.txt', 'r')
            liness = F.readlines()
            await client.send_message(mh,random.choice(liness))
            F.close()
        elif mc.startswith(prefix+"api"):
            F = open('api.txt', 'r')
            await client.send_message(mh,F.read())
            F.close() 
        elif mc.startswith(prefix+"changelog"):
            F = open('changelog.txt', 'r')
            await client.send_message(mh,F.read())
            F.close()
        elif mc.startswith(prefix+"serverinfo"):
            mycolor=mau.color
            em = discord.Embed(title=ms.name, colour=mycolor)
            if (ms.icon!=None):
                em.set_thumbnail(url=ms.icon_url)
            em.add_field(name="Server ID",value=str(ms.id),inline=True)
            em.add_field(name="Server Region",value=str(ms.region),inline=True)
            if (ms.icon!=None):
                em.add_field(name="Server Icon",value=ms.icon_url,inline=True)                  
            em.add_field(name="Members",value=str(ms.member_count),inline=True)
            em.add_field(name="Channels",value=str(len(ms.channels)),inline=True)                
            em.add_field(name="Roles",value=str(len(ms.roles)),inline=True)
            em.add_field(name="Server created at",value=str(ms.created_at.date())+" @ "+str(ms.created_at.time()),inline=True)
            if (ms.emojis!=None):
                em.add_field(name="Emojis",value=str(len(ms.emojis)),inline=True)
            if(ms.afk_channel!=None):
                em.add_field(name="AFK",value=str(int(ms.afk_timeout/60))+"min in `"+str(ms.afk_channel)+"` channel",inline=True)                   
            em.set_footer(text="Owner : "+ms.owner.name+"#"+str(ms.owner.discriminator)+" ("+str(ms.owner.id)+")", icon_url=ms.owner.avatar_url)
            await client.send_message(mh,"Info about **__"+ms.name+"__** server",tts=False,embed=em)
        elif mc.startswith(prefix+"userinfo "):
            no=ms.get_member_named(mcp[a+9:])
            aa=[]
            if no is None:
                try:
                    yes=mcp[a+9:]
                    no=gui.get_user_info(yes)
                except:
                    pass
            if no is None:
                try:
                    no=message.mentions[0]
                except:
                    pass
            print("User is "+str(no))
            try:
                mycolor=no.color
                em = discord.Embed(title=no.name+"#"+no.discriminator, colour=mycolor)
                em.set_thumbnail(url=no.avatar_url)
                em.add_field(name="User ID",value=str(no.id),inline=True)
                em.add_field(name="Bot user",value=("Yes" if no.bot else "No"),inline=True)
                em.add_field(name="Avatar",value=no.avatar_url,inline=True)                          
                em.add_field(name="Joined Date",value=str(no.joined_at.date()),inline=True)                
                em.add_field(name="Roles count on "+ms.name,value=str(len(no.roles)),inline=True)
                em.add_field(name="Account created at",value=str(no.created_at.date())+" @ "+str(no.created_at.time()),inline=True)
                em.add_field(name="Status",value=str(no.status),inline=True)
            except:
                print("!!")
            await client.send_message(mh,"Info about **__"+no.name+"__**",tts=False,embed=em)                                  
        elif mc.startswith(prefix+"serveremoji"):
            emoji=""
            for i in list(ms.emojis):
                emoji+=str(i)
            await client.send_message(mh,emoji)
        elif mc.startswith(prefix+"decvoltonify"):
            
            pattern = mcp[a+13:]

            nignog=pattern.replace("sakuješ","you suck diki").replace("seš", "you sucks").replace("maincra", "Minecraft").replace("maybe.surge.sh", "maybe").replace(" u ", "you").replace("^", "The above message is ").replace("fals", "false").replace("tru", "true").replace("sam", "same").replace("delet", "delete").replace("gey", "gay")          
            await client.send_message(mh,"**DECVOLTONIFY TEXT : **"+nignog)           
        elif mc.startswith(prefix+"emojify "):
            text=mcp[a+8:]
            o = ""
            for i in text:
                i = i.lower()
                if i in "abcdefghijklmnopqrstuvwxyz":
                    o += ":regional_indicator_{}:".format(i)
                elif i in "1234567890":
                    if i == "1":
                        i = "one"
                    elif i == "2":
                        i = "two"
                    elif i == "3":
                        i = "three"
                    elif i == "4":
                        i = "four"
                    elif i == "5":
                        i = "five"
                    elif i == "6":
                        i = "six"
                    elif i == "7":
                        i = "seven"
                    elif i == "8":
                        i = "eight"
                    elif i == "9":
                        i = "nine"
                    elif i == "0":
                        i = "zero"
                    o += ":{}:".format(i)
                elif i == "#":
                    o += "#⃣"
                elif i == "*":
                    o += "*⃣"
                elif i == "!":
                    o += ":exclamation:"
                elif i == "?":
                    o += ":question:"
                elif i == " ":
                    o += " "
            await client.send_message(mh,o)
        elif mc.startswith(prefix+"emojifyred "):
            text=mcp[a+11:]
            o = ""
            for i in text:
                i = i.lower()
                if i in "abm":
                    o += ":{}:".format(i)
                if i in "o":
                    o += ":{}2:".format(i)
                if i in "p":
                    o += ":{}arking:".format(i)
                if i in "cdefghijklnqrstuvwxyz":
                    o += ":regional_indicator_{}:".format(i)
                elif i == " ":
                    o += i
                elif i in "1234567890":
                    if i == "1":
                        i = "one"
                    elif i == "2":
                        i = "two"
                    elif i == "3":
                        i = "three"
                    elif i == "4":
                        i = "four"
                    elif i == "5":
                        i = "five"
                    elif i == "6":
                        i = "six"
                    elif i == "7":
                        i = "seven"
                    elif i == "8":
                        i = "eight"
                    elif i == "9":
                        i = "nine"
                    elif i == "0":
                        i = "zero"
                    o += ":{}:".format(i)
                elif i == "#":
                    o += "#⃣"
                elif i == "*":
                    o += "*⃣"
                elif i == "!":
                    o += ":exclamation:"
                elif i == "?":
                    o += ":question:"
                elif i == " ":
                    o += " "                
            await client.send_message(mh,o)
        elif mc.startswith(prefix+"listroles"):
            try:
                os.makedirs("C:\\Discord\\")                
                os.makedirs("C:\\Discord\\roles\\")
            except:
                pass
            f = codecs.open("C:\\Discord\\roles\\"+ms.name+"-"+ms.id+".txt","w+","utf-8-sig")            
            for i,role in enumerate(ms.roles):
                f.write(str(role)+"\n\n")
            f.close()
            print("success")
        elif mc.startswith(prefix+"listchannel"):
            try:
                os.makedirs("C:\\Discord\\")                    
                os.makedirs("C:\\Discord\\channels\\")
            except:
                pass

            f = codecs.open("C:\\Discord\\channels\\"+ms.name+"-"+ms.id+".txt","w+","utf-8-sig")            
            for i,channel in enumerate(ms.channels):
                f.write((str(channel)+"\n\n"))
            f.close()
            print("success")
        elif mc.startswith(prefix+"listmembers"):
            try:
                os.makedirs("C:\\Discord\\")                    
                os.makedirs("C:\\Discord\\members\\")
            except:
                pass

            f = codecs.open("C:\\Discord\\members\\"+ms.name+"-"+ms.id+".txt","w+","utf-8-sig")
            for channel in ms.members:
                f.write((str(channel)+"\n"))
            f.close()
            print("success")    
        elif mc.startswith(prefix+"coinflip"):
            coinlist=["Head","Tail"]
            numdiceso=0
            dices=1
            stdices=mcp[a+8:]

            try:
                if dices=="":
                    dices=1
                dices=int(stdices)
            except Exception as ex:
                pass
            finally:
                pass
            if dices<=0:
                await client.send_message(mh,"**Error!** : "+str(dices)+" is not a valid coin number")
            elif dices>200:
                await client.send_message(mh,"**Error!** : `Only at most 200 coins can be flip by this command`")
            else:
                out="Coin flip results : "
                ##print(dices)
                for i in range(0,dices):
                    out+="`"+coinlist[random.randint(0,1)]+"` "
                await client.send_message(mh,out)                
            
        elif mc.startswith(prefix+"diceroll"):
            dices=1        
            stdices=mcp[a+8:]

            try:
                if dices=="":
                    dices=1
                dices=int(stdices)
            except Exception as ex:
                pass
            finally:
                pass
            if dices<=0:
                await client.send_message(mh,"**Error!** : "+str(dices)+" is not a valid dice number")
            elif dices>200:
                await client.send_message(mh,"**Error!** : `Only at most 200 dices can be roll by this command`")
            else:
                out=":game_die: Dice results : "
                ##print(dices)
                for i in range(0,dices):
                    out+="`"+str(random.randint(1,6))+"` "
                await client.send_message(mh,out)                
        elif mc.startswith(prefix+"value "):
            parsed=mcp[a+6:]
            try:
                em = discord.Embed(title="Calculator", color=mau.color)
                em.add_field(name="You asked for answer of",value=str(parsed),inline=False)
                em.add_field(name="The answer is",value=str(round(eval(parsed),15)),inline=False)
                await client.send_message(mh,"",embed=em)                
            except:
                if(mau.id=="254214302653743104"):
                    em2 = discord.Embed(title="Knower of the world", color=mau.color)                    
                    await client.send_message(mh,"The answer of `"+str(parsed)+"` is `"+str((eval(parsed)))+"`")
                else:
                    await client.send_message(mh,"you**re** mom gau :joy::ok_hand:")

                

            
ass=asyncio.sleep(1)
def youtubesrc(textToSearch):
    query = urllib.parse.quote_plus(textToSearch)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urlopen(url)
    a=[]
    html = response.read()
    soup = BeautifulSoup(html,"html.parser")
    ass
    for aa in soup.find_all(attrs={'class':'yt-uix-tile-link'}):
            a.append('https://www.youtube.com' + aa['href'])
    return a[0]


#def twittersrc(textToSearch,mode):
#    query = urllib.parse.quote_plus(textToSearch)
#    url = "https://twitter.com/search?f= "+ mode+"&vertical=default&q= "+ query+"&src=typd"
#    response = urlopen(url)
 #   a=[]
  #  html = response.read()
   # soup = BeautifulSoup(html,"html.parser")
   # ass
   # if(mode=="users"):
  #      for aa in soup.find_all(attrs={'class':'ProfileCard'}):
 #           a.append('https://twitter.com/' + aa['data-screen-name'])
#    if(mode=="tweets"):
#        for aa in soup.find_all(attrs={'class':'tweet'}):
#            a.append('https://twitter.com/search'+aa['data-screen-name']+"/status/" + aa['data-tweet-id'])
#    return a[0]

    
if __name__ == '__main__':

    for extension in initial_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            print('Failed to load extension {}\n{}: {}'.format(extension, type(e).__name__, e))
        
def timedelta_milliseconds(td):
    return td.days*86400000 + td.seconds*1000 + td.microseconds/1000
with open("token.txt","r") as fi:
    contaaent = fi.readlines() 
    client.run(contaaent[0])
