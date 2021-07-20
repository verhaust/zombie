
class Player(object):

    def __init__(self, connection_info):
        self.host = connection_info[0]
        self.port = connection_info[1]
        self.name = ""
        self.history = []
        self.state = 0
        self.commands_to_process = []

    def process_commands(self):
        for command in self.commands_to_process:
            print(time.time())
            print(command)
        
def get_world_base():
    zones = glob.glob('world/*.zn')
    rooms = {}
    npcs = {}
    items = {}
    loadable_npcs = {}
    loadable_items = {}
    for zone in zones:
        with open(zone) as json_in:
            data = json.load(json_in)
            for key, room in data['rooms'].items():
                rooms[key] = room
            for key, npc in data['npcs'].items():
                npcs[key] = npc
            for key, item in data['items'].items():
                items[key] = item
            for key, npc in data['loadable_npcs'].items():
                loadable_npcs[key] = npc
            for key, item in data['loadable_items'].items():
                loadable_items[key] = item

    return rooms, npcs, items, loadable_npcs, loadable_items

def load_npc(npc):
    global npcs
    base_npc = npcs[npc['id']]

class Room(Object):

    def __init__(room):
        self.name = room['name']
        self.id = room['id']
        self.description = room['description']

class Thing(Object):

    def __init__(self):
        pass

default_attributes = {
                'strength': 10,
                'dexterity': 10,
                'willpower': 10,
                'constitution': 10,
                'intelligence': 10,
                'charisma': 10,
                'hitroll_bonus': 0,
                'damage_bonus': 0,
                'armor': 0,
                'damage_reduction': 0,
                'hitpoints': 10,
                'mana': 10,
                'stamina': 10,
                'weight': 10,
                'dimensions': {'height': [2,4],
                                'width': [1,3],
                                'depth': [1,3]
                                },
                }
class Character(Thing):

    def __init__(self, info):
        global default_attributes
        self.name = info['name']
        self.description = info['description']
        self.room = info.get('room', '0')
        self.attributes = info.get('attributes', default_attributes)
        self.equipment = info.get('equipment', {})
        self.inventory = info.get('inventory', [])
        self.spells = info.get('spells', [])
        self.skills = info.get('skills', [])
        self.affects = info.get('affects', [])
    
    def parse_stats(self, info):
        if 'stats' in info.keys():
            self.stats = info['stats']
        else:

class NPC(Character):

    def __init__(npc):
        self.id = npc['id']

class Item(Object):

    def __init__(item):
        self.name = item['name']
        self.id = item['id']
        self.description = item['description']
