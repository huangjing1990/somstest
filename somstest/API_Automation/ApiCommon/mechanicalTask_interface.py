from Common.Request import *
from Params.params import *


class MechanicalTask_interface():

    def __init__(self):
        self.request = Request()

    def add_task(self, domain, cookie, ):
        url, data, header = request_data("mechanicalTask_interface", "addMechanicalTask")

        apiUrl = domain + url

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def find_task(self, domain, cookie):
        url, data, header = request_data("mechanicalTask_interface", "findMechanicalTask")

        apiUrl = domain + url

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def edit_task(self, domain, cookie, jobTypeId):
        url, data, header = request_data("mechanicalTask_interface", "updateMechanicalTask")

        apiUrl = domain + url

        data["jobTypeId"] = jobTypeId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def delete_task(self, domain, cookie, jobTypeId):
        url, data, header = request_data("mechanicalTask_interface", "deleteMechanicalTask")

        apiUrl = domain + url

        data["jobTypeId"] = jobTypeId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response
