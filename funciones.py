import logging

from tabulate import tabulate


import threading

from sleekxmpp import ClientXMPP
from sleekxmpp.exceptions import IqError, IqTimeout
from sleekxmpp.xmlstream.stanzabase import ET, ElementBase
class Funciones(ClientXMPP):

    def __init__(self, jid, password, username):
        ClientXMPP.__init__(self, jid, password)

        self.add_event_handler("session_start", self.session_start)
        self.add_event_handler("message", self.message)

        contacts = []
        self.username = username

        #Plugins
        self.register_plugin('xep_0030') # Service Discovery
        self.register_plugin('xep_0199') # XMPP Ping
        self.register_plugin('xep_0045') # Mulit-User Chat (MUC)
        self.register_plugin('xep_0004') # Data forms
        self.register_plugin('xep_0077') # In-band Registration
        self.register_plugin('xep_0066') # Out-of-band Data
        self.register_plugin('xep_0096') # File transfer 
        self.register_plugin('xep_0030')
        self.register_plugin('xep_0047', {
            'auto_accept': True
        })

        # If you wanted more functionality, here's how to register plugins:
        # self.register_plugin('xep_0030') # Service Discovery
        # self.register_plugin('xep_0199') # XMPP Ping

        # Here's how to access plugins once you've registered them:
        # self['xep_0030'].add_feature('echo_demo')

        # If you are working with an OpenFire server, you will
        # need to use a different SSL version:
        # import ssl
        # self.ssl_version = ssl.PROTOCOL_SSLv3

    def log_out(self):
        self.disconnect()
    
    def add_friend(self,data):
        self.send_presence_subscription(pto=data)


    def session_start(self, event):
        try:

            login1 = logging.getLogger("XMPP")
            self.send_presence(new_status = "Conectado")
            roster = self.get_roster()

            for i in roster["roster"]["items"].keys():
                self.contacts.append(i)
        except IqError as err:
            print ("Error: %s" % err.iq['error']['text'])
            self.disconnect()
        except IqTimeout:
            print ("Error")
            self.disconnect
    




        # Most get_*/set_* methods from plugins use Iq stanzas, which
        # can generate IqError and IqTimeout exceptions
        #
        # try:
        #     self.get_roster()
        # except IqError as err:
        #     logging.error('There was an error getting the roster')
        #     logging.error(err.iq['error']['condition'])
        #     self.disconnect()
        # except IqTimeout:
        #     logging.error('Server is taking too long to respond')
        #     self.disconnect()

    def message(self, msg):
        print ("nuevo mensaje")
        if str(msg['type']) == "chat":
            data = []
            data.append((str(msg["from"]), str(msg["body"])))
            ms_data = tabulate(data, headers=['From', 'Message'], tablefmt='grid')
            print (ms_data)
            


    def all_users(self):
        user = self.Iq()
        user["type"] = "set"
        user["id"] = "search_result"
        user["to"] = "search.redes2020.xyz"
        user["from"] = self.boundjid.bare

        data = ET.fromstring("<query xmlns='jabber:iq:search'> \
                                <x xmlns='jabber:x:data' type='submit'> \
                                    <field type='hidden' var='FORM_TYPE'> \
                                        <value>jabber:iq:search</value> \
                                    </field> \
                                    <field var='Username'> \
                                        <value>1</value> \
                                    </field> \
                                    <field var='search'> \
                                        <value>*</value> \
                                    </field> \
                                </x> \
                              </query>")
        user.append(data)
        complete_user = user.send()
        cont = 0
        data = []
        dataUsers = []
        for i in complete_user.findall('.//{jabber:x:data}value'):
            cont = cont + 1
            user_data = ''
            if i.text != None:
                user_data = i.text
            data.append(user_data)
            if cont == 4:
                cont = 0
                dataUsers.append(data)
                data=[]
        return dataUsers

    def user_information(self, JIR):
        user = self.Iq()
        user["type"] = "set"
        user["id"] = "search_result"
        user["to"] = "search.redes2020.xyz"
        user["from"] = self.boundjid.bare
        que = ET.fromstring("<query xmlns='jabber:iq:search'> \
                                <x xmlns='jabber:x:data' type='submit'> \
                                    <field type='hidden' var='FORM_TYPE'> \
                                        <value>jabber:iq:search</value> \
                                    </field> \
                                    <field var='Username'> \
                                        <value>1</value> \
                                    </field> \
                                    <field var='search'> \
                                        <value>"+JIR+"</value> \
                                    </field> \
                                </x> \
                              </query>")
        user.append(que)

        users_data = user.send()
        cont = 0
        data= []
        users_info = []
        for i in users_data.findall('.//{jabber:x:data}value'):
            cont += 1
            user5 = ""
            if i.text != None:
                user5 = i.text
            data.append(user5)
            if cont == 4:
                cont = 0
                users_info.append(data)
                data=[]
        return users_info

    
    def direct_message(self,username,msg):
        
        self.send_message(mto= username, mbody=msg, mfrom=self.boundjid.user, mtype="chat")
        print ("send")
        print (username)
        print (msg)
            