from Common.Request import *
from Params.params import *


class Road1_interface():

    def __init__(self):
        self.request = Request()

    def findxs_road(self, domain, cookie):
        url, data, header = request_data("road1_interface", "findxsRoadByPage")

        apiUrl = domain + url

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def add_road(self, domain, cookie, roadName=None):
        url, data, header = request_data("road1_interface", "addRoad")

        apiUrl = domain + url

        data["roadName"] = roadName

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def find_road(self, domain, cookie):
        url, data, header = request_data("road1_interface", "findRoadByPage")

        apiUrl = domain + url

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def edit_road(self, domain, cookie, roadId, roadName):
        url, data, header = request_data("road1_interface", "updateRoad")

        apiUrl = domain + url

        data["roadName"] = roadName
        data["roadId"] = roadId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def Explorer_road(self, domain, cookie, roadId):
        url, data, header = request_data("road1_interface", "ExplorerRoad")

        apiUrl = domain + url

        data["roadId"] = roadId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def delete_road(self, domain, cookie, roadId):
        url, data, header = request_data("road1_interface", "deleteRoad")

        apiUrl = domain + url

        data["roadId"] = roadId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response
