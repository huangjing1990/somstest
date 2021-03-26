from Common.Request import *
from Params.params import *


class Org_interface():

    def __init__(self):
        self.request = Request()

    def add_org(self, domain, cookie):
        url, data, header = request_data("org_interface", "addOrg")

        apiUrl = domain + url

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def find_org(self, domain, cookie):
        url, data, header = request_data("org_interface", "findOrgByTree")

        apiUrl = domain + url

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def edit_org(self, domain, cookie, orgId, orgName):
        url, data, header = request_data("org_interface", "editOrg")

        apiUrl = domain + url

        data["orgId"] = orgId
        data["orgName"] = orgName
        data["shortName"] = orgName

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def delete_org(self, domain, cookie, orgId):
        url, data, header = request_data("org_interface", "deleteOrg")

        apiUrl = domain + url

        data["orgId"] = orgId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response
