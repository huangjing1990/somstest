from Common.Request import *
from Params.params import *


class Fence_interface():

    def __init__(self):
        self.request = Request()

    def add_fence(self, domain, cookie, fenceName=None):
        url, data, header = request_data("fence_interface", "addFence")

        apiUrl = domain + url

        data["fenceName"] = fenceName

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def find_fence(self, domain, cookie):
        url, data, header = request_data("fence_interface", "findFence")

        apiUrl = domain + url

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def choose_vehicle(self, domain, cookie, fenceId=None):
        url, data, header = request_data("fence_interface", "chooseVehicle")

        apiUrl = domain + url

        data["fenceId"] = fenceId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def edit_fence(self, domain, cookie, fenceId=None, fenceName=None):
        url, data, header = request_data("fence_interface", "editFence")

        apiUrl = domain + url

        data["fenceId"] = fenceId
        data["fenceName"] = fenceName

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def delete_fence(self, domain, cookie, fenceId=None):
        url, data, header = request_data("fence_interface", "deleteFence")

        apiUrl = domain + url

        data["fenceId"] = fenceId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response
