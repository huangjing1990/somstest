from Common.Request import *
from Params.params import *


class PatrolStandard_interface():

    def __init__(self):
        self.request = Request()

    def add_patrolStandard(self, domain, cookie, operationLevelName=None):
        url, data, header = request_data("patrolStandard_interface", "addPatrolStandard")

        apiUrl = domain + url
        data["operationLevelName"] = operationLevelName

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def find_patrolStandard(self, domain, cookie, operationLevelName=None):
        url, data, header = request_data("patrolStandard_interface", "findPatrolStandard")

        apiUrl = domain + url
        data["searchValue"] = operationLevelName

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def edit_patrolStandard(self, domain, cookie, operationLevelId=None, operationLevelName=None):
        url, data, header = request_data("patrolStandard_interface", "editPatrolStandard")

        apiUrl = domain + url
        data["operationLevelId"] = operationLevelId
        data["operationLevelName"] = operationLevelName

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def find_patrolStandardById(self, domain, cookie, operationLevelId=None):
        url, data, header = request_data("patrolStandard_interface", "findPatrolStandardById")

        apiUrl = domain + url
        data["operationLevelId"] = operationLevelId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def chooseOperationTime(self, domain, cookie, operationLevelId=None):
        url, data, header = request_data("patrolStandard_interface", "chooseOperationTime")

        apiUrl = domain + url
        data["operationLevelId"] = operationLevelId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def delete_patrolStandard(self, domain, cookie, operationLevelId=None):
        url, data, header = request_data("patrolStandard_interface", "deletePatrolStandard")

        apiUrl = domain + url

        data["operationLevelId"] = operationLevelId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response
