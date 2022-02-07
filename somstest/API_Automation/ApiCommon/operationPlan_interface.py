from Common.Request import *
from Params.params import *


class OperationPlan_interface():

    def __init__(self):
        self.request = Request()

    def add_org(self, domain, cookie, orgName):
        url, data, header = request_data("org_interface", "addOrg")

        apiUrl = domain + url

        data["orgName"] = orgName

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

    def add_team(self, domain, cookie):
        url, data, header = request_data("org_interface", "addTeam")

        apiUrl = domain + url

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def find_team(self, domain, cookie):
        url, data, header = request_data("org_interface", "findTeamById")

        apiUrl = domain + url

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def edit_team(self, domain, cookie, teamId):
        url, data, header = request_data("org_interface", "editTeam")

        apiUrl = domain + url

        data["orgId"] = teamId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def delete_team(self, domain, cookie, teamId):
        url, data, header = request_data("org_interface", "deleteTeam")

        apiUrl = domain + url

        data["orgId"] = teamId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response
