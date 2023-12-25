from pushbullet import Pushbullet

class Message:
    def __init__(self):
        API_KEY = "o.d4ADj9ET8UahPhI3AR43WdFkpDl7C66y"
        self.pb = Pushbullet(API_KEY)

    def police(self, time, place, details):
        message = """
        """
        pass


    def rent_successful(self, phone_no, message):
        push = self.pb.push_sms(device=self.pb.devices[0], number=phone_no, message=message)