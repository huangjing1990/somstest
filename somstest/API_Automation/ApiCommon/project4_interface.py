from Common.Request import *
from Params.params import *


class Project4_interface():

    def __init__(self):
        self.request = Request()

    def add_project(self, domain, cookie, projectName=None):
        url, data, header = request_data("project4_interface", "addProject")

        apiUrl = domain + url

        data["projectName"] = projectName

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def find_project(self, domain, cookie):
        url, data, header = request_data("project4_interface", "findProject")

        apiUrl = domain + url

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def edit_project(self, domain, cookie, projectId=None, projectName=None):
        url, data, header = request_data("project4_interface", "updateProject")

        apiUrl = domain + url

        data["projectId"] = projectId
        data["projectName"] = projectName

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def delete_project(self, domain, cookie, projectId=None):
        url, data, header = request_data("project4_interface", "deleteProject")

        apiUrl = domain + url

        data["projectId"] = projectId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response
