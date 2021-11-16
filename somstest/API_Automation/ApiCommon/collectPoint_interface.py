from Common.Request import *
from Params.params import *


class CollectPoint_interface():

    def __init__(self):
        self.request = Request()

    def find_collectPoint(self, domain, cookie):
        url, data, header = request_data("collectPoint_interface", "findCollectPoint")

        apiUrl = domain + url

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def find_collectPointByName(self, domain, cookie):
        url, data, header = request_data("collectPoint_interface", "findCollectPointByName")

        apiUrl = domain + url

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def look_collectPoint(self, domain, cookie, collectorPointId=None):
        url, data, header = request_data("collectPoint_interface", "lookCollectPoint")

        apiUrl = domain + url

        data["collectorPointId"] = collectorPointId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def edit_collectPoint(self, domain, cookie, collectorPointId=None):
        url, data, header = request_data("collectPoint_interface", "editCollectPoint")

        apiUrl = domain + url

        data["points"] = collectorPointId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response
