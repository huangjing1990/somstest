from Common.Request import *
from Params.params import *


class Alarm_interface():

    def __init__(self):
        self.request = Request()

    def edit_alarm(self, domain, cookie):
        url, data, header = request_data("alarm_interface", "saveAlarmCondition")

        apiUrl = domain + url

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def find_alarm(self, domain, cookie):
        url, data, header = request_data("alarm_interface", "selectAlarm")

        apiUrl = domain + url

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response
