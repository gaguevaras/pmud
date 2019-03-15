class Trigger:

    def __init__(self, mud, name, func):
        """
            Initialize and register a trigger
        """
        self.mud = mud
        self._name = name # Currently only triggering by exact match to name
        self._exec = func
        mud.register_output_observer(self)

    def notify(self, observable, *args, **kwargs):
        if self._name in kwargs.get('line'):
            print('Triggered!', self._name)
            print('Got', kwargs.get('line'), 'From', observable)
            return self._exec(self.mud)
        return None

def questing(mud):
	mud.tn.write('say hi\n'.encode())
	return


"""
    Trigger registry
    
    Each trigger must be registered here with a name and the acompanying function.
    Trigger functions receive the mud as a parameter so they can independently determine 
    how to interact with the mud.
"""
trigger_list = [
    { 'name': 'quest again', 'func': questing }    
]