class Alias:

    def __init__(self, mud, name, func):
        """
            Initialize and register an alias
        """
        self.mud = mud
        self._name = name
        self._exec = func
        mud.register_input_observer(self)

    def notify(self, observable, *args, **kwargs):
        if self._name in kwargs.get('line'):
            print('Triggered!', self._name)
            print('Got', kwargs.get('line'), 'From', observable)
            return self._exec(self.mud)
        return None


def spellup(mud):
    mud.tn.write('say hi\n'.encode())
    return True


def map_area(mud):
    # explore room:
        # determine the name of the current area
        # confirm this is the area the user wants to map
        # get a reference to the title of the current room
        # get a reference to the exits available and
    # explore the next room
    pass


"""
    Alias registry
    
    Each alias must be registered here with a name and the acompanying function.
    Alias functions receive the mud as a parameter so they can independently determine 
    how to interact with the mud.
"""
alias_list = [
    {
        'name': 'spellup',
        'func': spellup
    },
    {
        'name': 'map_area',
        'func': map_area
    }
]