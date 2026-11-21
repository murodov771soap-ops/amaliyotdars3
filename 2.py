class Telofon:
    def __int__(self,nom,xotira,imei):
        self.nom = nom
        self.xotira=xotira
        self.imei=imei
        
        def get_imei(self):
        
         return self.imei
        
        def set_imei(self,yangi):
            self.imei = yangi
            
        def info(self):
            print(f"{self.nom}-{self.xotira}(IMEI{self.get_imei})")
            
        def get_xotira(self,yangi):
            temp = yangi
            if    temp =1.0:    
            
t1 = Telofon("Samsung A22",256,12345678)
"""print(t1.get_imei()) """

t1.set_xotira(128)
print(t1.get_xotira())

