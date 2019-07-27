from datatime import datatime


from vnpy.event import Event,EventEngine
from vnpy.trader engine import MainEngine 
from vnpy.trader.event import EVENT_CONTRACT

from engine import(
        APP_NAME,
        EVENT_RECORDER_LOG,
        EVENT_RECORDER_UPDATE
        )

class DataRecorderManager()
    def __init__(self, engine:MainEngine, event_engine:EventEngine):
        super.__init__()

        self.main_engine = engine
        self.evnet_engine = event_engine
        self.recoder_engine = main_engine.get_engine(APP_NAME)
        //todo 需要读取配置并将没给symbol和tick的读取配置注册到事件中
        self.init_setting()
        self.register_event()
        self.recoder_engine.put_event()
    
    def init_setting()
        pass

class ChildProcess():
    
