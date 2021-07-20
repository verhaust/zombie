
class GameState(asyncio.protocol):

    def __init__(self, rooms, npcs, items):
        self.all_rooms = rooms
        self.all_npcs = npcs
        self.all_items = items
        self.rooms = self.initial_rooms()
        self.npcs = self.initial_npcs()
        self.items = self.initial_items()

    def initial_rooms():
        for id, room in self.initial_rooms():
            self.rooms[id] = Room(room)

    def initial_npcs():
        for id, npc in self.initial_npcs():
            self.npc[id] = NPC(npc)

    def initial_items():
        for id, item in self.initial_items():
            self.item[id] = Item(item)
