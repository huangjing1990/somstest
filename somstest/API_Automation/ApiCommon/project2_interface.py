from Common.Request import *
from Params.params import *


class Project2_interface():

    def __init__(self):
        self.request = Request()

    def add_project(self, domain, cookie, projectName=None):
        url, data, header = request_data("project2_interface", "addProject")

        apiUrl = domain + url

        data["projectName"] = projectName

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def finds_project(self, domain, cookie):
        url, data, header = request_data("project2_interface", "findsProject")

        apiUrl = domain + url

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def choice_project(self, domain, cookie, projectId):
        url, data, header = request_data("project2_interface", "updateBidState")

        apiUrl = domain + url

        data["projectId"] = projectId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def find_project(self, domain, cookie):
        url, data, header = request_data("project2_interface", "findProjectByPage")

        apiUrl = domain + url

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def edit_project(self, domain, cookie, projectId, projectName):
        url, data, header = request_data("project2_interface", "updateProject")

        apiUrl = domain + url

        data["projectName"] = projectName
        data["projectId"] = projectId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def findxs_road(self, domain, cookie, projectId):
        url, data, header = request_data("project2_interface", "findxsRoadByPage")

        apiUrl = domain + url

        data["project.projectId"] = projectId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def add_road(self, domain, cookie, roadName=None, projectId=None):
        url, data, header = request_data("project2_interface", "addRoad")

        apiUrl = domain + url

        data["roadName"] = roadName
        data["project.projectId"] = projectId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def find_road(self, domain, cookie, projectId):
        url, data, header = request_data("project2_interface", "findRoadByPage")

        apiUrl = domain + url

        data["project.projectId"] = projectId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def edit_road(self, domain, cookie, roadId, roadName, projectId):
        url, data, header = request_data("project2_interface", "updateRoad")

        apiUrl = domain + url

        data["roadName"] = roadName
        data["roadId"] = roadId
        data["project.projectId"] = projectId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def delete_road(self, domain, cookie, roadId, projectId):
        url, data, header = request_data("project2_interface", "deleteRoad")

        apiUrl = domain + url

        data["roadId"] = roadId
        data["project.projectId"] = projectId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def delete_project(self, domain, cookie, projectId):
        url, data, header = request_data("project2_interface", "deleteProject")

        apiUrl = domain + url

        data["projectId"] = projectId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

