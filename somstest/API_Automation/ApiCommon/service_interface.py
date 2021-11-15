from Common.Request import *
from Params.params import *


class Service_interface():

    def __init__(self):
        self.request = Request()

    def add_service(self, domain, cookie, name=None):
        url, data, header = request_data("service_interface", "addService")

        apiUrl = domain + url

        data["name"] = name

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def find_service(self, domain, cookie, searchValue=None):
        url, data, header = request_data("service_interface", "findService")

        apiUrl = domain + url

        data["searchValue"] = searchValue

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def edit_service(self, domain, cookie, cateringUnitsId=None, name=None):
        url, data, header = request_data("service_interface", "updateService")

        apiUrl = domain + url

        data["cateringUnitsId"] = cateringUnitsId
        data["name"] = name

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def delete_service(self, domain, cookie, cateringUnitsId=None):
        url, data, header = request_data("service_interface", "deleteService")

        apiUrl = domain + url

        data["cateringUnitsId"] = cateringUnitsId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response
