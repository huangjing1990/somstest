from Common.Request import *
from Params.params import *


class RoadSection_interface():

    def __init__(self):
        self.request = Request()

    def add_roadSection(self, domain, cookie, roadSectionName=None):
        url, data, header = request_data("roadSection_interface", "addRoadSection")

        apiUrl = domain + url

        data["roadSectionName"] = roadSectionName

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def find_roadSection(self, domain, cookie):
        url, data, header = request_data("roadSection_interface", "findRoadSection")

        apiUrl = domain + url

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def edit_roadSection(self, domain, cookie, roadSectionId=None, roadSectionName=None):
        url, data, header = request_data("roadSection_interface", "updateRoadSection")

        apiUrl = domain + url

        data["roadSectionId"] = roadSectionId

        data["roadSectionName"] = roadSectionName

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def delete_roadSection(self, domain, cookie, roadSectionId=None):
        url, data, header = request_data("roadSection_interface", "deleteRoadSection")

        apiUrl = domain + url

        data["roadSectionId"] = roadSectionId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response
