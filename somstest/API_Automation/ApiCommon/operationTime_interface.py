from Common.Request import *
from Params.params import *


class OperationTime_interface():

    def __init__(self):
        self.request = Request()

    def add_time(self, domain, cookie, ):
        url, data, header = request_data("operationTime_interface", "addOperationTime")

        apiUrl = domain + url

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def find_time(self, domain, cookie):
        url, data, header = request_data("operationTime_interface", "findOperationTimeByPage")

        apiUrl = domain + url

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def edit_time(self, domain, cookie, operationTimeId,):
        url, data, header = request_data("operationTime_interface", "updateOperationTime")

        apiUrl = domain + url

        data["operationTimeId"] = operationTimeId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def delete_time(self, domain, cookie, operationTimeId,):
        url, data, header = request_data("operationTime_interface", "confimDeleteOperationTime")

        apiUrl = domain + url

        data["operationTimeId"] = operationTimeId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response
