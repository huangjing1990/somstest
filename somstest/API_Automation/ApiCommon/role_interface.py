from Common.Request import *
from Params.params import *


class Role_interface():

    def __init__(self):
        self.request = Request()

    def add_role(self, domain, cookie, roleName=None):
        url, data, header = request_data("role_interface", "addRole")

        apiUrl = domain + url

        data["roleName"] = roleName

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def find_role(self, domain, cookie):
        url, data, header = request_data("role_interface", "findRoleByPage")

        apiUrl = domain + url

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def edit_role(self, domain, cookie, roleId):
        url, data, header = request_data("role_interface", "updateRole")

        apiUrl = domain + url

        data["roleId"] = roleId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def delete_role(self, domain, cookie, roleId):
        url, data, header = request_data("role_interface", "deleteRole")

        apiUrl = domain + url

        data["roleId"] = roleId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response
