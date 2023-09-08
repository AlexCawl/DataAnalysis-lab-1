class LogDTO:
    def __init__(self, ip: str, date_time: str, http_type: str, url: str, code: str, user_id: str):
        self.ip = ip
        self.date_time = date_time
        self.http_type = http_type
        self.url = url
        self.code = code
        self.user_id = user_id

    def __str__(self):
        return f"{self.__dict__}"
