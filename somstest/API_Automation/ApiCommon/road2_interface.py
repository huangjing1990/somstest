from Common.Request import *
from Params.params import *


class Road2_interface():

    def __init__(self):
        self.request = Request()

    def add_road(self, domain, cookie, roadName=None):
        url, data, header = request_data("road2_interface", "addRoad")

        apiUrl = domain + url

        data["roadName"] = roadName

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def find_road(self, domain, cookie, searchValue=None):
        url, data, header = request_data("road2_interface", "findRoadByPage")

        apiUrl = domain + url

        data["searchValue"] = searchValue

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def save_explorer(self, domain, cookie, roadId=None):
        url, data, header = request_data("road2_interface", "findRoadByPage")

        apiUrl = domain + url

        data["roadId"] = roadId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def edit_road(self, domain, cookie, roadId=None, roadName=None):
        url, data, header = request_data("road2_interface", "updateRoad")

        apiUrl = domain + url

        data["roadName"] = roadName
        data["roadId"] = roadId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def delete_road(self, domain, cookie, roadId):
        url, data, header = request_data("road2_interface", "deleteRoad")

        apiUrl = domain + url

        data["roadId"] = roadId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response
