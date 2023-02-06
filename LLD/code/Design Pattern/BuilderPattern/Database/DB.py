

class Database:
    '''
    def __init__(self,host,port,username,password):
        self.host=host
        self.port=port
        self.username=username
        self.password=password
        '''
    '''
    def __init__(self,**kwargs):
        self.host=map.get('host')
        self.port=map.get('port')
        self.username=map.get('username')
        self.password=map.get('password')
        
        '''

    def __init__(self,**kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)









