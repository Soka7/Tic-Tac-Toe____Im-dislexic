import time
import threading as th

class Chrono:
    def __init__(self):
        self.Signal = False
    
    def StopTime(self, Time):
        """Stop time for Time seconds.

        Args:
            Time (int): time
        """
        time.sleep(Time)
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
        self.StopTime(Time)
        return True
    
    def LauchTimer(self, Time):
        Thread = th.Thread(target = self.SetTimer, args = [Time])
        Thread.start()
        
Chrono1 = Chrono()
Chrono1.LauchTimer(20)
print(Chrono1.Signal)