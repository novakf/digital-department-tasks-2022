import datetime
import json
from api import register_booking

class Booking:
    
    def __init__(self, room_name, start, end):
        if start>end:
            raise ValueError("start>end")
        self.room_name = room_name
        self.start = start
        self.end = end

    @property
    def duration(self):
        return (self.end - self.start).seconds/60
    
    @property
    def start_date(self):
        return self.start.date().isoformat()
        
    @property
    def end_date(self):
        return self.end.date().isoformat()
    
    @property
    def start_time(self):
        return self.start.time().strftime("%H:%M")
        
    @property
    def end_time(self):
        return self.end.time().strftime("%H:%M")

    def to_dict(self):
        return {
            "room_name":self.room_name,
            "start_date":self.start_date,
            "start_time":self.start_time,
            "end_date":self.end_date,
            "end_time":self.end_time,
            "duration":self.duration,
        }

def create_booking(room_name, start, end) -> str:
    print("Начинаем создание бронирования")
    bkg = Booking(room_name, start, end)
    res: dict = {}
    try:
        if register_booking(bkg):
            res["created"] = True
            res["msg"] = "Бронирование создано"
        else:
            res["created"] = False
            res["msg"] = "Комната занята"
    except KeyError:
        res["created"] = False
        res["msg"] = "Комната не найдена"
    finally:
        print("Заканчиваем создание бронирования")

    res["booking"] = bkg.to_dict()
    
    return json.dumps(res)