from Common.Request import *
from Params.params import *


class OperationTask_interface():

    def __init__(self):
        self.request = Request()

    def add_task(self, domain, cookie, ):
        url, data, header = request_data("operation_interface", "addOperationTask")

        apiUrl = domain + url

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def find_task(self, domain, cookie):
        url, data, header = request_data("operation_interface", "findOperationTask")

        apiUrl = domain + url

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def edit_task(self, domain, cookie, operationTaskId,):
        url, data, header = request_data("operation_interface", "updateOperationTask")

        apiUrl = domain + url

        data["operationTaskId"] = operationTaskId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def delete_task(self, domain, cookie, operationTaskId,):
        url, data, header = request_data("operation_interface", "deleteOperationTasks")

        apiUrl = domain + url

        data["operationTaskId"] = operationTaskId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response
