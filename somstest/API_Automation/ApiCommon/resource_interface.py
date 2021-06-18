from Common.Request import *
from Params.params import *


class Resource_interface():

    def __init__(self):
        self.request = Request()

    def add_resource(self, domain, cookie, ):
        url, data, header = request_data("resource_interface", "addOperationResource")

        apiUrl = domain + url

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def find_resource(self, domain, cookie):
        url, data, header = request_data("resource_interface", "findOperationResource")

        apiUrl = domain + url

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def edit_resource(self, domain, cookie, operationResourceId,):
        url, data, header = request_data("resource_interface", "updateOperationResource")

        apiUrl = domain + url

        data["operationResourceId"] = operationResourceId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def delete_resource(self, domain, cookie, operationResourceId,):
        url, data, header = request_data("resource_interface", "deleteOperationResources")

        apiUrl = domain + url

        data["operationResourceId"] = operationResourceId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response
