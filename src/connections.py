from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor
from twisted.internet import task
from twisted.internet.protocol import Protocol
import string

#blah

class Commands (object):

	def __init__(self):
		self.channels = []
		self.emotes = []
		self.skills = []
		self.
class NPC(object):

	def __init__(self):
		self.NPCID = None
		self.name = None
		self.location = None
		self.classes = []
		self.skills = []
		self.spells = []
		self.stats = None
		self.equipment = {}
		self.inventory = {}

	def importNPC(self,npcID)
		
class Player(NPC):

	def __init__(self):
		self.playerID = None
		self.toggles = {}
		
class Globals(object):

	def __init__(self):
		self.allPlayers = None
		self.connectedPlayers = []

playerList = []

def sanitize(line):
	return "".join(i for i in line if i in string.printable)

def sanitizeAlpha(line):
	return "".join(i for i in line if i in string.letters)
	
def verifyName(name):
	if len(name) > 20:
		return 1
	if name in knownPlayers:
		return 2
	if name in bannedNames:
		return 3
	return 0

#class Connected(Protocol):
class Connected(LineReceiver,Protocol):
	
	def __init__(self):
		self.name = None
		self.state = "GETNAME"

	def connectionMade(self):
		self.transport.write("Name:")
		self.state = "GOTNAME"
		#retStr = "You are Connected.\n"
		#retStr = "Other players connected are: \n"
		#for i in playerList:
		#	retStr += i + "\n"
        	#self.transport.write(retStr)

	def lineReceived(self, line):
		if self.state == "GOTNAME":
			line = sanitizeAlpha(line)
			result = verifyName(line)
			print line
			self.transport.write(line)
			self.transport.write(line)
			#self.transport.write("Name:")
		#if state == "GOTNAME":
		#elif state == "GETPASSWORD":
		#self.name = line.strip()
		#playerList.append(self)
        	self.transport.write(line)
        	self.transport.write(line)


class ConnectionFactory(Factory):

	def buildProtocol(self, addr):
		return Connected()

def runEverySecond():
	for i in playerList:
		i.transport.write("How are you " + i.name + "?")
		if i.name == "bobby":
			i.transport.write("How are you Bobby?")
	#return "You are connected"

l = task.LoopingCall(runEverySecond)
l.start(1000) # call every second
# 8007 is the port you want to run under. Choose something >1024
endpoint = TCP4ServerEndpoint(reactor, 8007)
endpoint.listen(ConnectionFactory())
reactor.run()
