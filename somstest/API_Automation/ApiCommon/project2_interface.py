from Common.Request import *
from Params.params import *


class Project2_interface():

    def __init__(self):
        self.request = Request()

    def find_project(self, domain, cookie):
        url, data, header = request_data("project2_interface", "findProjectByPage")

        apiUrl = domain + url

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def update_project(self, domain, cookie):
        url, data, header = request_data("project2_interface", "updateProject")

        apiUrl = domain + url

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

