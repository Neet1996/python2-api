# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
# https://kaijento.github.io/2017/05/19/web-scraping-youtube.com/
import time,random,sys,json,codecs,threading,glob,requests,urllib,urllib2,urllib3
from bs4 import BeautifulSoup
from urllib import urlopen
from gtts import gTTS
from googletrans import Translator

cl = LINETCR.LINE()
#cl.login(qr=True)
cl.login(token="EpHJdpdRYfugpYoNvjO0.LWgKk7amvuthLm0twfh+Ga.fEplE3C5w/K0Vq5Q9Fve75lC9rP/b/abbouxKpubqhI=")
cl.loginResult()
ki=ki2=ki3=ki4=cl


reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""
─┅═✥ʙᴏᴛ ᴛʜᴀɪʟᴀɴᴅ✥═┅─
❂͜͡☆➣ 『Me』
❂͜͡☆➣ 『Id』
❂͜͡☆➣ 『Wc』
❂͜͡☆➣ 『Mid』
❂͜͡☆➣ 『ของขวัญ』
❂͜͡☆➣ 『Speed/Sp』
❂͜͡☆➣ 『พูด text』
❂͜͡☆➣ 『ขอเพลง text』
❂͜͡☆➣ 『แทค』
❂͜͡☆➣ 『แอบ』
❂͜͡☆➣ 『อ่าน』
─┅═✥Admin bot✥═┅─
❂͜͡☆➣ 『Mid @』
❂͜͡☆➣ 『botset』
❂͜͡☆➣ 『ปิดเข้า/เปิดเข้า』
❂͜͡☆➣ 『บอทแทคออก』
  ─┅═✥ᵀᴴᴬᴵᴸᴬᴺᴰ✥═┅─
✍ŦɛşŦ ƅ✪Ŧ Îℕƿ¥➣➤
By. Admin Tum
By. Admin M
Project 
"""

Thaihelp ="""
"""

helo=""

KAC=[cl,ki,ki2,ki3,ki4]
mid = cl.getProfile().mid
kimid = ki.getProfile().mid
ki2mid = ki2.getProfile().mid
ki3mid = ki3.getProfile().mid
ki4mid = ki4.getProfile().mid
Bots = [mid,kimid,ki2mid,ki3mid,ki4mid,"uf6c337b7dc57d24351b192caf612b812"]
bot1 = cl.getProfile().mid
superadmin = "uf6c337b7dc57d24351b192caf612b812"
admsa = "uf6c337b7dc57d24351b192caf612b812"
admin = "uf6c337b7dc57d24351b192caf612b812"
owner = "uf6c337b7dc57d24351b192caf612b812"

wait = {
    'contact':False,
    'autoJoin':True,
    'autoAdd':True,
    'autoCancel':{"on":False,"members":50},
    'leaveRoom':False,
    'timeline':False,
    'message':"สนใจบอทแทค แอดไลน์มาที่ \n http://line.me/ti/p/~Neet1996 \n เพื่อดึงบอทเข้ากลุ่มของท่าน ใช้ฟรี 1 เดือน\n และแก้ไขทันเวลาในตอนที่ บอทตาย",
    "lang":"JP",
    "clock":False,


}

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    "ricoinvite":{},
    'ROM':{},
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }

setTime = {}
setTime = wait2['setTime']
blacklistFile='blacklist.txt'
pendinglistFile='pendinglist.txt'
mulai = time.time()

contact = cl.getProfile()
mybackup = cl.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus

contact = ki.getProfile()
backup = ki.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

user1 = mid
user2 = ""

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d ชั่วโมง %02d นาที %02d วินาที' % (hours, mins, secs)

def bot(op):
    global AsulLogged
    global ki6
    global user2
    global readAlert
    global lgncall
    global save1
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 13:
            invitor = op.param2
            if invitor in [superadmin]:
                cl.acceptGroupInvitation(op.param1)
            if invitor not in [superadmin]:
                cl.rejectGroupInvitation(op.param1)
        if op.type == 16:
            gname = cl.getGroup(op.param1).name
            cl.sendText(superadmin,"บอทแทคsuperได้เข้าร่วมกลุ่ม\n"+gname+"\n"+op.param1)
#-------------------------------------------------------------------------
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 25:
            msg = op.message
            if msg.text.lower() == "fuck":
                kk.sendText(superadmin,msg.to)

# ----------------- NOTIFED MEMBER OUT GROUP
 #       if op.type == 15:
  #          if op.param2 in bot1:
   #             return
    #        cl.sendText(op.param1,"" + cl.getContact(op.param2).displayName + " \n   ••*•••*•••*•••*••\nขอบคุณที่ใช้บริการ\nโอกาสหน้าเชิญใหม่นะครับ\n💙 ขอบคุณครับ 💙 \n◡̈••*•••*•••*•••*•••*••\n✍ŦɛşŦ ƅ✪Ŧ Îℕƿ¥➣➤")


# ----------------- NOTIFED MEMBER JOIN GROUP
        if op.type == 17:
            if op.param2 in bot1:
                return
            ginfo = cl.getGroup(op.param1)
            cl.sendText(op.param1, "ʕ•ᴥ•ʔ ยินดีต้อนรับสู่กลุ่ม ʕ•ᴥ•ʔ  \n ☞ " + str(ginfo.name) + "...☜""\n\n🔇กรุณาปิดการแจ้งเตือนครับ🔇\n ◡̈--------------------------◡̈\n✍ŦɛşŦ ƅ✪Ŧ Îℕƿ¥➣➤")

            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
            	if wait["ricoinvite"] == True:
                     if msg.from_ in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 ki.sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 cl.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 cl.sendText(msg.to,"Call my daddy to use command !, \nปลดแบน @" + invite)
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     ki.findAndAddContactsByMid(target)
                                     ki.inviteIntoGroup(msg.to,[target])
                                     random.choice(KAC).sendText(msg.to,"Invited Success \n➡ " + _name)
                                     wait2["ricoinvite"] = False
                                     break                              
                                 except:             
                                          cl.sendText(msg.to,"Negative, Err0r Detected")
                                          wait2["ricoinvite"] = False
                                          break


            elif msg.text is None:
                return
            elif msg.text.lower()  == 'help':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpMessage)
#-------------------public-------------------------------)
            elif msg.text in ["ของขวัญ","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                cl.sendMessage(msg)
            elif "Me" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)

            elif "Id" == msg.text:
                key = msg.to
                cl.sendText(msg.to, key)
				
            elif "พูด " in msg.text:
                say = msg.text.replace("พูด ","")
                lang = 'th'
                tts = gTTS(text=say, lang=lang)
                tts.save("say.mp3")
                cl.sendAudio(msg.to,"say.mp3")
            elif "name:" in msg.text:
                if msg.from_ in [superadmin]:
                    string = msg.text.replace("name:","")
                    if len(string.decode('utf-8')) <= 20:
                        profile = cl.getProfile()
                        profile.displayName = string
                        cl.updateProfile(profile)
                        cl.sendText(msg.to, "เปลี่ยนชื่อสำเร็จ")
            elif "bio:" in msg.text:
                string = msg.text.replace("bio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"เปลี่ยนสถานะเป็น " + string)
#-----------------------------------------------
#                Admin
#-----------------------------------------------
            elif msg.text in ["Join on","suเปิดเข้า"]:
				if msg.from_ in admin:
					if wait["autoJoin"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"เปิดอยู่แล้ว 􀜁􀇔􏿿👈")
						else:
							cl.sendText(msg.to,"เข้ากลุ่มอัตโนมัติเปิดอยู่👈")
					else:
						wait["autoJoin"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"เปิดเข้ากลุ่มอัตโนมัติ")
						else:
							cl.sendText(msg.to,"เปิดระบบเข้ากลุ่มอัตโนมัติ")
            elif msg.text in ["Join off","suปิดเข้า"]:
				if msg.from_ in admin:
					if wait["autoJoin"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"ปิดอยู่แล้ว")
						else:
							cl.sendText(msg.to,"ระบบเข้ากลุ่มอัตโนมัติปิดอยู่")
					else:
						wait["autoJoin"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"ปิดเข้ากลุ่มอัตโนมัติ")
						else:
							cl.sendText(msg.to,"ปิดระบบเข้ากลุ่มอัตโนมัติ👈")	
            elif msg.text in ["subotset"]:
				if msg.from_ in admin:
					md = "⭐Status บอทแทค⭐\n*============*\n"
					if wait["autoJoin"] == True: md+="[•]Auto Join [On]\n"
					else: md +="[•]Auto Join [Off]\n"
					cl.sendText(msg.to,md)
					
            elif msg.text in ["Reject","suลบรัน"]:
				if msg.from_ in admin:
					gid = cl.getGroupIdsInvited()
					for i in gid:
						cl.rejectGroupInvitation(i)
					if wait["lang"] == "JP":
						cl.sendText(msg.to,"ปฎิเสธเรียบร้อย")
					else:
						cl.sendText(msg.to,"ลองดู")
            elif msg.text in ["suรายชื่อกลุ่ม"]:
				if msg.from_ in admin:
					gid = cl.getGroupIdsJoined()
					h = ""
					for i in gid:
						h += "[★] %s\n" % (cl.getGroup(i).name +"→["+str(len(cl.getGroup(i).members))+"]")
					cl.sendText(msg.to,"[List Group]\n"+ h +"กลุ่มทั้งหมด  =" +"["+str(len(gid))+"]")
#--------------------------------------------------------------------------------------------		
#-----------------------------------------------
#                READ POINT
#-----------------------------------------------						
            elif msg.text in ["แอบ"]:
				if msg.toType == 2:
					cl.sendText(msg.to, "ตั้งจุดเช็คคนอ่าน:" + datetime.now().strftime('\n📅%Y/%m/%d 🕛 %H:%M:%S'))
					try:
						del wait2['readPoint'][msg.to]
						del wait2['readMember'][msg.to]
					except:
						pass
					wait2['readPoint'][msg.to] = msg.id
					wait2['readMember'][msg.to] = ""
					wait2['setTime'][msg.to] = datetime.now().strftime('📅%Y-%m-%d 🕛 %H:%M:%S')
					wait2['ROM'][msg.to] = {}

					
            elif msg.text in ["อ่าน"]: 
                if msg.toType == 2:
					if msg.to in wait2['readPoint']:
						if wait2["ROM"][msg.to].items() == []:
							chiya = ""
						else:
							chiya = ""
							for rom in wait2["ROM"][msg.to].items():
								chiya += rom[1] + "\n"
								
						cl.sendText(msg.to, "คนที่อ่าน%s\n \n\nวันและเวลาในการอ่าน:\n[%s]" % (wait2['readMember'][msg.to],setTime[msg.to]))
					else:
						cl.sendText(msg.to, "ไม่สามารถอ่านได้กรุณาตั้งค่าใหม่พิมพ์\n[แอบ]ตั้งค่าเสร็จสิ้นกรุณาพิมพ์\n[อ่าน]]")
						
            elif msg.text in ["Tag@@","Tagall","แทค","แทก","tagall","tag@@"]:
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*100 : (j+1)*100]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    cl.sendMessage(msg) 
            elif msg.text in ["Mid"]:
                cl.sendText(msg.to,mid)
				
            elif msg.text.lower() == 'runtime':
                eltime = time.time() - mulai
                van = "ระยะเวลาการทำงานของบอท :\n"+waktu(eltime)
                cl.sendText(msg.to,van)
				
            elif msg.text in ["Welcome","wc","welcome","Wc"]:
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"ยินดีต้อนรับสู่กลุ่ม " + str(ginfo.name))
                cl.sendText(msg.to,"Owner Group " + str(ginfo.name) + " :" + ginfo.creator.displayName )
#-----------------------------------------------
#                YOUTUBE
#-----------------------------------------------

            elif 'ขอเพลง ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('ขอเพลง ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    cl.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    cl.sendText(msg.to,"Could not find it")	
            elif 'ยูทูป ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('ยูทูป ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    cl.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    cl.sendText(msg.to,"Could not find it")	

#-----------------------------------------------
#                BOT RESPONS
#-----------------------------------------------
            
            elif msg.text.lower() == 'บอทตอบ':
                profile = ki.getProfile()
                text = profile.displayName
                ki.sendText(msg.to, text + " รายงานตัวครับผม")
			

#----------------------ADMIN COMMAND------------------------------#
            elif "#Me" in msg.text:
				if msg.from_ in admin:
					msg.contentType = 13
					msg.contentMetadata = {'mid': msg.to+"',"}
					cl.sendMessage(msg)
            elif "#แจกโปร " in msg.text:
				if msg.from_ in admin:
					bctxt = msg.text.replace("#แจกโปร ", "")
					a = cl.getGroupIdsJoined()
					for manusia in a:
						cl.sendText(manusia, (bctxt))
            elif "sug " in msg.text:
                if msg.from_ in admin: 
                    bctxt = msg.text.replace("sug ", "")
                    a = cl.getGroupIdsJoined()
                    for manusia in a:
                        cl.sendText(manusia,"ข้อความอัตโนมัติ :\n" + (bctxt))
            elif "suf " in msg.text:
                if msg.from_ in admin: 
                    bctxt = msg.text.replace("suf ", "")
                    a = cl.getAllContactIds()
                    for manusia in a:
                        cl.sendText(manusia,"ข้อความอัตโนมัติ :\n" + (bctxt))
            elif ("Baby " in msg.text):
                if msg.from_ in admin:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.kickoutFromGroup(msg.to,[target])
                        except:
                            cl.sendText(msg.to,"เตะติดแบน")

            elif msg.text in ["Sp","Speed","speed"]:
				cl.sendText(msg.to,"「กำลังเชคความเร็วบอทแทค...」")
				start = time.time()
				time.sleep(0.001)
				elapsed_time = time.time() -start
				cl.sendText(msg.to, "%sseconds" % (elapsed_time))

            elif "Mid @" in msg.text:
              if msg.from_ in admin:  
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        ki.sendText(msg.to, g.mid)
                    else:
                        pass


 #-----------------------------------------------------------
            elif "#leave" in msg.text:
                try:
                    import sys
                    sys.exit()
                except:
                    pass
#-----------------------------------------------------------
            
            elif msg.text.lower() == 'respons':
                profile = ki.getProfile()
                text = profile.displayName
                ki.sendText(msg.to, text)

            elif msg.text in ["suออก"]:
				if msg.from_ in admin: 
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							cl.sendText(msg.to,"ไปก็ได้ บ๊ายบาย "  +  str(ginfo.name)  + "")
							cl.leaveGroup(msg.to)							
						except:
							pass
			
#------------------------------------------------------------------



#------------------------------------------------------------------------------------

        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
                    Nama = cl.getContact(op.param2).displayName
                    if Nama in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n|| " + Nama
                        wait2['ROM'][op.param1][op.param2] = "|| " + Nama
                        wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                else:
                    cl.sendText
            except:
                pass

def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()


while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
