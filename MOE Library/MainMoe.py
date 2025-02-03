
class MainMoe():
    def __init__(self, obj):
        self.obj=obj
        self.lauch=0
        
    def mainPlay(self):
        while 1:
            self.obj[self.lauch].__init__()
            self.obj[self.lauch].play()
            self.lauch=self.obj[self.lauch].forLauch
            
