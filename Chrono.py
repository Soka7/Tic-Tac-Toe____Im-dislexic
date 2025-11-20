import time
import threading as th

class Chrono:
    def __init__(self):
        self.Signal = False
    
    def StopTime(self, Time, Timer = False):
        """Stop time for Time seconds.

        Args:
            Time (int): time
        """
        time.sleep(Time)
        if Timer == True:
            self.Signal = True
        return None
        
    def GetTimeFunction(self, Fonction, *args, **kwargs):
        Start = time.time()
        Fonction(*args, **kwargs)
        End = time.time()
        Exe = End - Start
        
        return Exe
    
    def SetTimer(self, Time):
        assert Time < 600, "Too long"
        print(f"Waiting {Time} seconds.")
        self.StopTime(Time, True)
        return True
        
Chrono1 = Chrono()

Thread = th.Thread(target = Chrono1.SetTimer(2000, True))