import requests
import wx
#import keyboard
#import pyautogui
import os,sys
import re
#<script type="application/json" data-target="react-app.embeddedData">.*?</script>
User_Agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 QIHU 360SE'#default
print('[DEBUG] EveryBlock Downlaod successfully')
class WxMainlyObject(wx.Frame):
	def __init__(self,parent,id):
		wx.Frame.__init__(self,parent,id,title = "SpiderViewer----Beta1.2.0",size = (600,620))
		self.panel = wx.Panel(self)
		self.MainlyTable = wx.TextCtrl(self.panel,pos = (0,0),size = (500,530),style = wx.TE_PROCESS_TAB|wx.TE_MULTILINE)
		self.FontShowing = wx.StaticText(self.panel,pos = (0,530),label = 'Cookie: ')
		self.table = wx.TextCtrl(self.panel,pos = (50,530),size = (300,25),style = wx.TE_PROCESS_TAB|wx.TE_MULTILINE)
		self.UrlShowing  = wx.StaticText(self.panel,pos = (0,555),label = 'Url:')
		self.Url = wx.TextCtrl(self.panel,pos = (50,555),size = (300,25),style = wx.TE_PROCESS_TAB|wx.TE_MULTILINE)
		self.writen = wx.Button(self.panel,pos = (500,0),size = (85,60),label = 'Help')
		self.Variables = wx.Button(self.panel,pos = (500,60),size = (85,60),label = 'Variables')
		self.Notice = wx.Button(self.panel,pos = (500,120),size = (85,60),label = 'Notice')
		self.writen.Bind(wx.EVT_BUTTON,self.WriteBinders)
		self.Variables.Bind(wx.EVT_BUTTON,self.VariablesTool)
		self.ButtonYes = wx.Button(self.panel,pos = (350,530),size = (50,50),label = 'Yes')
		self.ButtonYes.Bind(wx.EVT_BUTTON,self.GetCookieVariables)
		self.Notice.Bind(wx.EVT_BUTTON,self.Notices)
		self.url = ''
		self.headers = {
	
			'User-Agent': User_Agent,
			'Cookie':False#'__guid=234898968.352653242602504060.1652705208503.2004; __huid=11UNhTAysG3L6nPzE13bQJYc2q4ct%2BbbO8YUs0ZkEvxiA%3D; __hsid=9ae8b6f80a9f041a; __DC_monitor_count=1; count=1; sessionID=234898968.4509475793366565000.1666366654299.6052; _uc_mid=901fece658dd4d6a40f8644e8a68c2d0; __asc=1d61d5db80a11565237251e748050ccb.1067.1666366654956; _uc_m2=b7d9690187b5cc78f6ae14a0f2510f50d001f9172b85; __asc2=8a4c57c536af3ce2fd2c4c1c83e9b87eed94c7d39a9f.1109.1666366655220; customEng=10-21; test_cookie_enable=null; click_hotword_count=1'
		}
		

		#self.Requests_Maining = requests.get(url = self.url,headers = self.headers).content.decode()
		#self.work = wx.StaticText(self.panel,label = 'success',pos = (20,20))
		self.label = wx.TextCtrl(self.panel,pos = (400,530),size = (180,50),style = wx.TE_PROCESS_TAB|wx.TE_MULTILINE)
		#self.label.SetValue(self.Requests_Maining)
	def Notices(self,event):
			class Notices(wx.Frame):
				def __init__(self,parent,id):
					wx.Frame.__init__(self,parent,id,title = 'Notices',size = (600,300))
					self.panel = wx.Panel(self)
					self.headers = {
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
					
					}
					self.r = requests.get(url = 'https://raw.githubusercontent.com/SupnaOnUbuntu/SupnaOnUbuntu/main/Notice.txt',headers = self.headers,verify = False,timeout = 10).content.decode()
					self.NoticeLabel = wx.TextCtrl(self.panel,pos = (30,10),size = (500,200),style = wx.TE_PROCESS_TAB | wx.TE_MULTILINE | wx.TE_READONLY)
					try:
						self.NoticeLabel.SetValue(self.r)
						print(self.r)
					except Exception as err:
						self.NoticeLabel.SetValue(str(err))
				
			app = wx.App()
			frame = Notices(parent = None,id = -1)
			frame.Show()
			app.MainLoop()
	
	def GetCookieVariables(self,event):
		def URL_SAVE_FUNCTIONS(UrlData,ErrorMessage,Content):
			'''
				UrlData:URL Reequests
				ErrorMessage:None/True default:None
				Content:SetValue or don't Set default:Set
			'''
			UrlDataer = UrlData
			if self.MainlyTableGetValue != None and self.labelGetValue == '!S':
				print('Matched-[DEBUG] SubbedBox initing')
				class IS_PRESSED_MATCHEDBOXER(wx.Frame):
					def __init__(self,parent,id):
						wx.Frame.__init__(self,parent,id,title = 'Match-Sub',size = (800,640))
						self.panel = wx.Panel(self)
						self.SetCursor(wx.StockCursor(wx.CURSOR_CROSS))
						self.Matched = wx.TextCtrl(self.panel,pos = (0,00),size = (300,600),style = wx.TE_READONLY|wx.TE_MULTILINE)
						'''self.conditions = wx.TextCtrl(self.panel,pos = (400,0),size = (300,200),style = wx.TE_MULTILINE)'''
						self.ConditionalButton = wx.Button(self.panel,pos = (300,350),size = (220,50),label = 'Sub by myself')
						self.ConditionalButton_Replace = wx.Button(self.panel,pos = (560,350),size = (220,50),label = 'Replace by myself')
						self.SaveButton = wx.Button(self.panel,pos = (300,275),size = (100,50),label = 'Save as')
						self.ConditionalButton.Bind(wx.EVT_BUTTON,self.ConditionallyOnClick)
						self.ConditionalButton_Replace.Bind(wx.EVT_BUTTON,self.Conditionally_ReplaceOnClick)
						self.SaveButton.Bind(wx.EVT_BUTTON,self.SaveOnClick)
						wx.StaticText(self.panel,pos = (320,130),label = 'The previous operation:')
						self.PreviousOperation = wx.TextCtrl(self.panel,pos = (480,50),size = (300,200),style = wx.TE_READONLY|wx.TE_MULTILINE)
						self.PreviousOperation.SetValue(self.Matched.GetValue())
						self.PreviousOperationButton = wx.Button(self.panel,pos = (680,0),size = (100,50),label = 'Undo')
						self.PreviousOperationButton.Bind(wx.EVT_BUTTON,self.PreviousOperationFunctions)
						wx.StaticText(self.panel,pos = (300,250),label = '---------------------------------------------------------------------------------------------')
						wx.StaticText(self.panel,pos = (300,330),label = '---------------------------------------------------------------------------------------------')
						if Content == None:
							self.Matched.SetValue(str(UrlDataer))
						else:
							self.Matched.SetValue('No data was inputed!')
					def Conditionally_ReplaceOnClick(self,event):
						self.New_Matched = self.Matched.GetValue()
						print(self.New_Matched)
						app = wx.App()
						Windows = wx.Frame(None,title = 'Replace',pos = (300,300),size = (300,150))
						panel = wx.Panel(Windows)
						self.MatchString = wx.TextCtrl(panel,pos = (84,0),size = (200,30))
						wx.StaticText(panel,label = 'MatchString:',pos = (0,15))
						self.ReplaceString = wx.TextCtrl(panel,pos = (84,40),size = (200,30))
						wx.StaticText(panel,label = 'ReplaceString:',pos = (0,50))
						ReplaceButton = wx.Button(panel,label = 'Yes',pos = (160,70),size= (100,40))
						ReplaceButton.Bind(wx.EVT_BUTTON,self.Replacing)
						Windows.Show()
						app.MainLoop()
					def Replacing(self,event):
						MatchStingReplacer = self.MatchString.GetValue()
						ReplaceStringReplacer = self.ReplaceString.GetValue()
						Matched_Replacer = re.sub(MatchStingReplacer,ReplaceStringReplacer,self.New_Matched)
						LenReplacer = len(Matched_Replacer)
						LenMatched = len(self.New_Matched)
						FinalWords = LenMatched - LenReplacer
						print('[DEBUG]Replace successfully\nReplace words: ',str(FinalWords))
						self.PreviousOperation.SetValue(self.New_Matched)
						self.Matched.SetValue(Matched_Replacer)
						'''
						class Replace(wx.Frame):
							def __init__(self,parent,id):
								wx.Frame.__init__(self,parent,id,pos = (300,300),size = (300,150),title = 'Replace')
								self.panel = wx.Panel(self)
								self.New_Matched = New_Matched
								self.MatchString = wx.TextCtrl(self.panel,pos = (84,0),size = (200,30))
								wx.StaticText(self.panel,label = 'MatchString:',pos = (0,15))
								self.ReplaceString = wx.TextCtrl(self.panel,pos = (84,40),size = (200,30))
								wx.StaticText(self.panel,label = 'ReplaceString:',pos = (0,50))
								self.ReplaceButton = wx.Button(self.panel,label = 'Yes',pos = (160,70),size= (100,40))
								self.ReplaceButton.Bind(wx.EVT_BUTTON,self.Replacing)
							def Replacing(self,event):
								#self.New_Matched = self.Matched.GetValue()
								self.MatchStingReplacer = self.MatchString.GetValue()
								self.ReplaceStringReplacer = self.ReplaceString.GetValue()
								self.Matched_Replacer = re.sub(self.MatchStingReplacer,self.ReplaceStringReplacer,self.New_Matched)

								print('[DEBUG]Replace successfully replace words: ')
						app = wx.App()
						Replace = Replace(parent = None,id = -1)
						Replace.Show()
						app.MainLoop()
					'''
					def ConditionallyOnClick(self,event):
						New_Matched = self.Matched.GetValue()
						self.dialog = wx.TextEntryDialog(self,'Sub by myself','Sub command:')
						if self.dialog.ShowModal() == wx.ID_OK:
							self.conditiions = self.dialog.GetValue()
							print('[DEBUG]Conditions: ',self.conditiions)
							Rematched = re.sub(str(self.conditiions),'',New_Matched)
							LenWords = len(New_Matched) - len(Rematched)
							print('[DEBUG]implemented successfully delete words: ',str(LenWords))
							self.PreviousOperation.SetValue(str(New_Matched))
							self.Matched.SetValue(Rematched)
						self.dialog.Destroy
					def SaveOnClick(self,event):
						New_Matched = self.Matched.GetValue()
						self.SaveAS = wx.TextEntryDialog(self,'Save as','Path:')
						if self.SaveAS.ShowModal() == wx.ID_OK:
							try:
								with open(self.SaveAS.GetValue(),'w',encoding = 'utf-8') as f:
									f.write(New_Matched)
									print('[DEBUG] Save successfully')
							except UnicodeEncodeError as err:
								print('[WARNING] ',err,'change from UTF-8 to GBK')
								with open(self.SaveAS.GetValue(),'w') as f:
									f.write(New_Matched)
									print('[DEBUG] Save successfully')

					def PreviousOperationFunctions(self,event):
						self.Undo = self.Matched.GetValue()
						self.Matched.SetValue(self.PreviousOperation.GetValue())
						self.PreviousOperation.SetValue(self.Undo)

				app = wx.App()
				frame = IS_PRESSED_MATCHEDBOXER(parent = None,id = -1)
				frame.Show()
				app.MainLoop()
			if self.MainlyTableGetValue != None and self.labelGetValue == '!R':
				print(self.MainlyTableGetValue)
	
			if self.MainlyTableGetValue != None and self.labelGetValue == '!W':
				'''UrlDataer = UrlData'''
				print('Writen-[DEBUG] WritingBox initing')
				class IS_PRESSED_WRITINGBOXER(wx.Frame):
					def __init__(self,parent,id):
						wx.Frame.__init__(self,parent,id,title = 'Save',size = (850,500))
						self.panel = wx.Panel(self)
						self.ButtonSave = wx.StaticText(self.panel,label = 'SaveName',pos = (35,50))
						self.Savename = wx.TextCtrl(self.panel,pos = (100,50),size = (300,30))
						self.SavePathText = wx.StaticText(self.panel,label = 'SavePath',pos = (35,150))
						self.Savepath = wx.TextCtrl(self.panel,pos = (100,150),size = (300,30))
						self.SavestuffixText = wx.StaticText(self.panel,label = 'stuffix',pos = (35,230))
						self.SaveStuffix = wx.TextCtrl(self.panel,pos = (100,230),size = (50,30))
						self.SavingButton = wx.Button(self.panel,pos = (150,300),size = (150,40),label = 'Save')
						self.Readonly = wx.TextCtrl(self.panel,pos = (500,20),size = (300,400),style = wx.TE_READONLY|wx.TE_MULTILINE)
						if Content == None:
							self.Readonly.SetValue(str(UrlDataer))
						else:
							self.Readonly.SetValue('No data was inputed!')
						self.SavingButton.Bind(wx.EVT_BUTTON,self.Writing)#suffix
					def Writing(self,event):
						self.name = self.Savename.GetValue()
						self.path = self.Savepath.GetValue()
						self.stuffix = self.SaveStuffix.GetValue()
						if (ErrorMessage == None):
							try:
								with open(self.path+self.name+'.'+self.stuffix,'w') as f:
									f.write(UrlDataer)
									print('[DEBUG] '+self.path+self.name+'.'+self.stuffix+' download successfuly')
							except UnicodeEncodeError:
								os.system('del '+self.path+self.name+'.'+self.stuffix)
								with open(self.path+self.name+'.'+self.stuffix,'w',encoding = 'utf-8') as f:
									f.write(UrlDataer)
									print('[DEBUG] '+self.path+self.name+'.'+self.stuffix+' download successfully')
						else:
							with open(self.path+self.name+'.'+self.stuffix,'wb') as f:
								f.write(UrlDataer)
								print('[DEBUG] '+self.path+self.name+'.'+self.stuffix+' download successfully')
							
				app = wx.App()
				frame = IS_PRESSED_WRITINGBOXER(parent = None,id =-1)
				frame.Show()
				app.MainLoop()
		

		#print('[DEBUG] GetCookieVariables is  initing successfully')
		self.reloaders  = self.table.GetValue()
		self.setUrl = self.Url.GetValue()
		self.labelGetValue = self.label.GetValue()
		self.MainlyTableGetValue = self.MainlyTable.GetValue()
		self.url = self.setUrl
		self.headers['Cookie'] = self.reloaders
		try:
			print('[DEBUG] Trying Get Request Post')
			self.r = requests.get(url = self.url,headers = self.headers).content.decode('utf-8')
			self.MainlyTable.SetValue(self.r)
			URL_SAVE_FUNCTIONS(self.r,None,None)
		except requests.exceptions.MissingSchema as UrlError:
			self.MainlyTable.SetValue('[ERROR]: Throwing Errors'+str(UrlError))
		except UnicodeDecodeError as EncodingError:
			try:
				self.r = requests.get(url = self.url,headers = self.headers).content.decode('gbk')
				self.MainlyTable.SetValue(self.r)
				#print(self.r)
				URL_SAVE_FUNCTIONS(self.r,None,None)
				print('[WARNING] Throwing Errors' + EncodingError)
			except UnicodeDecodeError as errorer:
				print('[ERROR] Throwing Errors: '+str(errorer))
				try:
					self.r = requests.get(url = self.url,headers = self.headers).content
					if(len(self.r) >= 1000):
						self.MainlyTable.SetValue("can't show this website's data!But you can output the data messages.\nReturn: Successfully")
					else:
						self.MainlyTable.SetValue(self.r)
				except:
					self.r = requests.get(url = self.url,headers = self.headers).content
					self.MainlyTable.SetValue("can't decodec this website's data!\nReturn: Failed")
					os.system('pause')
					exit()
				URL_SAVE_FUNCTIONS(self.r,str(errorer),True)
		self.label.SetValue('[DEBUGGED] '+str(self.headers)+'\n[DEBUGGED]' + str(self.url) + '\n[DEBUGGED]' + 'User-Agent : Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 QIHU 360SE')
		
		
		print('[DEBUG] GetCookieVariables is initing successfully')
		
	def WriteBinders(self,event):
		print('[DEBUG] HelpingBox gets ready')
		BaserImage_1 = '''data:image/png;base64,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'''
		with open('SpiderHelping.html','w') as f:
			f.write('<!DOCTYPE HTML><head><meta charset="utf-8"><title>Helper</title><style type = "text/css">body{background-color: skyblue;font-style: italic;font-size: small;}h3{font-size:30px;text-align:center;}th,td{text-align:center;font-style:oblique;width:300px;height:30px;border:1px solid black;font-size:15px}table{text-align:center;}</style></head><html><body><h3>Hi, there is a helping notice</h3><strong><h1>This is the Gui helper</h1></strong><img src="'+BaserImage_1+'"<br><h3 name = "Notice" id = "Notice">Notice:</h3><hr><table style = "border-collapse: collapse;"><p style = "text-align:center">Serveral codes of the DebugBox:</p><tr><th>!W</th><td>Put the file datas into a new creation files</td><td>2023/4/16 0:31</td></tr></table></body></html>')
		os.system('SpiderHelping.html')
			#print(a)
	def VariablesTool(self,event):
		print('[DEBUG] VariablesTool is initing successfully')
		VariablesCookies = self.table.GetValue()
		VariablesUrl = self.Url.GetValue()
		if (VariablesUrl == ''):
			print('[DEBUG] No enter URL')
			return None
		else:
			print('[DEBUG] MoreVariables get ready')
			class VariablesTooler(wx.Frame):
				def __init__(self,parent,id):
					wx.Frame.__init__(self,parent,id,title = 'MoreVariables',pos = (100,100),size = (600,600))
					self.panel = wx.Panel(self)
					self.buttonMoreVariables = wx.Button(self.panel,label = 'Yes',pos = (400,450),size = (100,30))
					
					'''
					Variables = {
						'Cookie' : VariablesCookies,
						'URL' : VariablesUrl,
						'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 QIHU 360SE',
						'Accept-Encoding' : 'Undefined',
						'Accept-Language' : 'Undefined',
						'Cache-Control' : 'Undefined',
						'Connection' : 'Undefined',
						'Host' : 'Undefined',
						'Referer' : 'Undefined',
						'Sec-Fetch-Dest' : 'Undefined',
						'Sec-Fetch-Mode' : 'Undefined',
						'Sec-Fetch-Site' : 'Undefined',
						'Sec-Fetch-User' : 'Undefined',
						'Upgrade-Insecure-Requests' : 'Undefined',
					}
					'''
					VariablesArray = ['VariableCookie','VariableURL','VariableUser_Agent','VariableAccept_Encoding','VariableAccept_Language','VariableCache_Control','VariableConnection','VariableHost','VariableReferer','VariableSec_Fetch_Dest','VariableSec_Fetch_Mode','VariableSec_Fetch_Site','VariableSec_Fetch_User','VariableUpgrade_Insecure_Requests']
					'''VariablesLines Area'''
					self.ps = wx.StaticText(self.panel,label = '*ps: if web requests value is "Undefined".The machine will not press that values!',pos = (0,500))
					self.CookieStatic = wx.TextCtrl(self.panel,pos = (120,50),size = (80,30),style = wx.TE_READONLY).SetValue('Cookie')
					self.Cookie = wx.TextCtrl(self.panel,pos = (200,50),size = (200,30),style = wx.TE_READONLY)
					self.Cookie.SetValue(VariablesCookies)
					self.URLStatic = wx.TextCtrl(self.panel,pos = (120,80),size = (80,30),style = wx.TE_READONLY).SetValue('Url')
					self.URL = wx.TextCtrl(self.panel,pos = (200,80),size = (200,30),style = wx.TE_READONLY)
					self.URL.SetValue(VariablesUrl)
					self.User_AgentStatic = wx.TextCtrl(self.panel,pos = (120,110),size = (80,30),style = wx.TE_READONLY).SetValue('User-Agent')
					self.User_Agent = wx.TextCtrl(self.panel,pos = (200,110),size = (200,30))
					self.User_Agent.SetValue('Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 QIHU 360SE')
					self.Accept_EncodingStatic = wx.TextCtrl(self.panel,pos = (120,140),size = (80,30),style = wx.TE_READONLY).SetValue('Accept-Encoding')
					self.Accept_Encoding = wx.TextCtrl(self.panel,pos = (200,140),size = (200,30))
					self.Accept_LanguageStatic = wx.TextCtrl(self.panel,pos = (120,170),size = (80,30),style = wx.TE_READONLY).SetValue('Accept-Language')
					self.Accept_Language = wx.TextCtrl(self.panel,pos = (200,170),size = (200,30))
					self.Cache_ControlStatic = wx.TextCtrl(self.panel,pos = (120,200),size = (80,30),style = wx.TE_READONLY).SetValue('Cache-Control')
					self.Cache_Control = wx.TextCtrl(self.panel,pos = (200,200),size = (200,30))
					self.ConnectionStatic = wx.TextCtrl(self.panel,pos = (120,230),size = (80,30),style = wx.TE_READONLY).SetValue('Connection')
					self.Connection = wx.TextCtrl(self.panel,pos = (200,230),size = (200,30))
					self.HostStatic = wx.TextCtrl(self.panel,pos = (120,260),size = (80,30),style = wx.TE_READONLY).SetValue('Host')
					self.Host = wx.TextCtrl(self.panel,pos = (200,260),size = (200,30))
					self.RefererStatic = wx.TextCtrl(self.panel,pos = (120,260),size = (80,30),style = wx.TE_READONLY).SetValue('Referer')
					self.Referer = wx.TextCtrl(self.panel,pos = (200,260),size = (200,30))
					self.Sec_Fetch_DestStatic = wx.TextCtrl(self.panel,pos = (120,290),size = (80,30),style = wx.TE_READONLY).SetValue('Sec-Fetch-Dest')
					self.Sec_Fetch_Dest = wx.TextCtrl(self.panel,pos = (200,290),size = (200,30))
					self.Sec_Fetch_ModeStatic = wx.TextCtrl(self.panel,pos = (120,320),size = (80,30),style = wx.TE_READONLY).SetValue('Sec-Fetch-Mode')
					self.Sec_Fetch_Mode = wx.TextCtrl(self.panel,pos = (200,320),size = (200,30))
					self.Sec_Fetch_SiteStatic = wx.TextCtrl(self.panel,pos = (120,350),size = (80,30),style = wx.TE_READONLY).SetValue('Sec-Fetch-Site')
					self.Sec_Fetch_Site = wx.TextCtrl(self.panel,pos = (200,350),size = (200,30))
					self.Sec_Fetch_UserStatic = wx.TextCtrl(self.panel,pos = (120,380),size = (80,30),style = wx.TE_READONLY).SetValue('Sec-Fetch-User')
					self.Sec_Fetch_User = wx.TextCtrl(self.panel,pos = (200,380),size = (200,30))
					self.Upgrade_Insecure_RequestsStatic = wx.TextCtrl(self.panel,pos = (120,380),size = (80,30),style = wx.TE_READONLY).SetValue('Upgrade-Insecure-Requests')
					self.Upgrade_Insecure_Requests = wx.TextCtrl(self.panel,pos = (200,380),size = (200,30))
					self.CodingTypeStatic = wx.TextCtrl(self.panel,pos = (120,410),size = (80,30),style = wx.TE_READONLY).SetValue('Coding')
					self.CodingType = wx.TextCtrl(self.panel,pos = (200,410),size = (200,30))
					'''Init_Array = [self.Cookie.GetValue(),self.URL.GetValue(),self.User_Agent.GetValue(),self.Accept_Encoding.GetValue(),self.Accept_Language.GetValue(),self.Cache_Control.GetValue(),self.Connection.GetValue(),self.Host.GetValue(),self.Host.GetValue(),self.Referer.GetValue(),self.Sec_Fetch_Dest.GetValue(),self.Sec_Fetch_Mode.GetValue(),self.Sec_Fetch_Site.GetValue(),self.Sec_Fetch_User.GetValue(),self.Upgrade_Insecure_Requests.GetValue()]'''
					self.buttonMoreVariables.Bind(wx.EVT_BUTTON,self.SelectionMoreVariables)

				def SelectionMoreVariables(self,event):
						print('[DEBUG] successfully')
						CodingType = self.CodingType.GetValue()
						Init_Array = [self.Cookie.GetValue(),self.URL.GetValue(),self.User_Agent.GetValue(),self.Accept_Encoding.GetValue(),self.Accept_Language.GetValue(),self.Cache_Control.GetValue(),self.Connection.GetValue(),self.Host.GetValue(),self.Host.GetValue(),self.Referer.GetValue(),self.Sec_Fetch_Dest.GetValue(),self.Sec_Fetch_Mode.GetValue(),self.Sec_Fetch_Site.GetValue(),self.Sec_Fetch_User.GetValue(),self.Upgrade_Insecure_Requests.GetValue()]
						class MoreVariablesPrase(wx.Frame):
							def __init__(self,parent,id):
								wx.Frame.__init__(self,parent,id,title = 'Prase',pos = (300,300),size = (600,375))
								self.panel = wx.Panel(self)		
								self.MoreVariablesLabel = wx.TextCtrl(self.panel,pos = (0,0),size = (580,300),style = wx.TE_MULTILINE)
								self.WrittenSave = wx.Button(self.panel,pos = (0,300),size = (100,30),label = 'Save As')
								self.WrittenPath = wx.TextCtrl(self.panel,pos = (100,300),size = (200,30))
								self.WrittenSave.Bind(wx.EVT_BUTTON,self.WrittenSaves)
								self.CodingTypes = CodingType
								self.Old_Variables = {
									'Cookie' : Init_Array[0],
									#'URL' : Init_Array[1],
									'User-Agent' : Init_Array[2],
									'Accept-Encoding' : Init_Array[3],
									'Accept-Language' : Init_Array[4],
									'Cache-Control' : Init_Array[5],
									'Connection' : Init_Array[6],
									'Host' : Init_Array[7],
									'Referer' : Init_Array[8],
									'Sec-Fetch-Dest' : Init_Array[9],
									'Sec-Fetch-Mode' : Init_Array[10],
									'Sec-Fetch-Site' : Init_Array[11],
									'Sec-Fetch-User' : Init_Array[12],
									'Upgrade-Insecure-Requests' : Init_Array[13],
								}
								self.New_Variables = {}
								num = 0
								for j in (list(self.Old_Variables.keys())):
									if self.Old_Variables[j] == '':
										self.Old_Variables.pop(j)
									else:
										self.New_Variables[j] = Init_Array[num]
									num+=1
								#-------------I'm Cutting line!--------------------
								print(self.New_Variables)
								print(self.CodingTypes)
								if self.CodingTypes != '':
									self.r = requests.get(url = Init_Array[1],headers = self.New_Variables).content.decode(self.CodingTypes)
									self.MoreVariablesLabel.SetValue(r)
								else:
									self.r = requests.get(url = Init_Array[1],headers = self.New_Variables).content.decode()
									if (len(self.r) <= 8*1024*1024):
										self.MoreVariablesLabel.SetValue(self.r)
									else:
										self.MoreVariablesLabel.SetValue('The files size was so big!We cannot print it.You can try to create this files and preview them!')
								#self.r = requests.get(url = Init_Array[1],headers = self.New_Variables).content.decode(str(Init_Array[14]))
								#self.MoreVariablesLabel.SetValue(self.r)
								self.r = self.r
							def WrittenSaves(self,event):
								WrittenPaths = self.WrittenPath.GetValue()
								with open(WrittenPaths,'w',encoding = 'utf-8') as f:
									f.write(self.r)
						app = wx.App()
						frame = MoreVariablesPrase(id =-1,parent = None)
						frame.Show()
						app.MainLoop()
		app = wx.App()
		frame = VariablesTooler(parent = None,id = -1)
		frame.Show()
		app.MainLoop()
		if frame == None:
			return 'error'
		print('[DEBUG] MoreVariables closed')
        
print('[DEBUG] GUI initing successfully')                                
app = wx.App()
frame = WxMainlyObject(parent = None,id = -1)
frame.Show()
app.MainLoop()
print('[DEBUG] FrameClosing')





#CODER_BY_SupnaOnUbuntu
#GITHUB:SupnaOnUbuntu
#WeChat:imhkbYHY
#Bilibili:HKRequestGet
