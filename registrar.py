import logging

from sleekxmpp import ClientXMPP
from sleekxmpp.exceptions import IqError, IqTimeout


class EchoBot(ClientXMPP):

    def __init__(self, jid, password,name):
        ClientXMPP.__init__(self, jid, password)

        self.add_event_handler("session_start", self.session_start)
        self.add_event_handler("register", self.register_user)

        # If you wanted more functionality, here's how to register plugins:
        # self.register_plugin('xep_0030') # Service Discovery
        # self.register_plugin('xep_0199') # XMPP Ping

        # Here's how to access plugins once you've registered them:
        # self['xep_0030'].add_feature('echo_demo')

        # If you are working with an OpenFire server, you will
        # need to use a different SSL version:
        # import ssl
        # self.ssl_version = ssl.PROTOCOL_SSLv3
                #Plugins
        self.register_plugin('xep_0030')
        self.register_plugin('xep_0004')
        self.register_plugin('xep_0066')
        self.register_plugin('xep_0077') 


    def session_start(self, event):
        self.send_presence()
        self.get_roster()
        self.disconnect()

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

    def register_user(self, msg):
        print ("entro a la funcion")
        new_msg = self.Iq()
        print ("entro 1")
        new_msg["type"]= "set"
        new_msg["register"]["username"] = self.boundjid.user
        print ("entro 2")
        new_msg["register"]["password"] = self.password
        print ("entro 3")



        print ("antes del try")
        try:
            print ("dentro del try")
            new_msg.send(now=True)
            print ("creo la cuenta")
        except IqError as iqe:
            print ("Error: %s" %iqe.iq["Error"]["text"])
            self.disconnect()
        except IqTimeout:
            print ("server no responde")
            self.disconnect()




