from Common.Request import *
from Params.params import *


class ContainerType_interface():

    def __init__(self):
        self.request = Request()

    def add_containerType(self, domain, cookie, name=None, volume=None):
        url, data, header = request_data("containerType_interface", "addContainerType")

        apiUrl = domain + url

        data["name"] = name
        data["volume"] = volume

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def find_containerType(self, domain, cookie):
        url, data, header = request_data("containerType_interface", "findContainerTypeByPage")

        apiUrl = domain + url

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def edit_containerType(self, domain, cookie, typeId, volume, name):
        url, data, header = request_data("containerType_interface", "updateContainerType")

        apiUrl = domain + url

        data["name"] = name
        data["typeId"] = typeId
        data["volume"] = volume

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def delete_containerType(self, domain, cookie, typeId):
        url, data, header = request_data("containerType_interface", "deleteContainerType")

        apiUrl = domain + url

        data["typeId"] = typeId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response
