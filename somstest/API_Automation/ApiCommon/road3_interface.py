from Common.Request import *
from Params.params import *


class Road3_interface():

    def __init__(self):
        self.request = Request()

    def add_road(self, domain, cookie, roadName=None):
        url, data, header = request_data("road3_interface", "addRoad")

        apiUrl = domain + url

        data["roadName"] = roadName

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def find_road(self, domain, cookie):
        url, data, header = request_data("road3_interface", "findRoadByPage")

        apiUrl = domain + url

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def edit_road(self, domain, cookie, roadId, roadName):
        url, data, header = request_data("road3_interface", "updateRoad")

        apiUrl = domain + url

        data["roadName"] = roadName
        data["roadId"] = roadId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def delete_road(self, domain, cookie, roadId):
        url, data, header = request_data("road3_interface", "deleteRoad")

        apiUrl = domain + url

        data["roadId"] = roadId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response
