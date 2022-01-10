from Common.Request import *
from Params.params import *


class Project3_interface():

    def __init__(self):
        self.request = Request()

    def add_project(self, domain, cookie, projectName=None):
        url, data, header = request_data("project3_interface", "addProduceProject")

        apiUrl = domain + url

        data["projectName"] = projectName

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def find_project(self, domain, cookie):
        url, data, header = request_data("project3_interface", "findProjectByPage")

        apiUrl = domain + url

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def edit_project(self, domain, cookie, projectId, projectName):
        url, data, header = request_data("project3_interface", "updateProduceProject")

        apiUrl = domain + url

        data["projectName"] = projectName
        data["projectId"] = projectId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def delete_project(self, domain, cookie, projectId):
        url, data, header = request_data("project3_interface", "deleteProduceProject")

        apiUrl = domain + url

        data["projectId"] = projectId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response
