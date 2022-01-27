from Common.Request import *
from Params.params import *


class CleanRoute_interface():

    def __init__(self):
        self.request = Request()

    def add_cleanRoute(self, domain, cookie, cleanRouteName=None):
        url, data, header = request_data("cleanRoute_interface", "addCleanRoute")

        apiUrl = domain + url

        data["cleanRouteName"] = cleanRouteName

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def find_cleanRoute(self, domain, cookie):
        url, data, header = request_data("cleanRoute_interface", "findCleanRoute")

        apiUrl = domain + url

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def edit_cleanRoute(self, domain, cookie, cleanRouteId=None,cleanRouteName=None):
        url, data, header = request_data("cleanRoute_interface", "updateCleanRoute")

        apiUrl = domain + url

        data["cleanRouteId"] = cleanRouteId
        data["cleanRouteName"] = cleanRouteName

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def disable_cleanRoute(self, domain, cookie, cleanRouteId=None):
        url, data, header = request_data("cleanRoute_interface", "disableCleanRoute")

        apiUrl = domain + url

        data["cleanRouteId"] = cleanRouteId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def delete_cleanRoute(self, domain, cookie, cleanRouteId=None):
        url, data, header = request_data("cleanRoute_interface", "deleteCleanRoute")

        apiUrl = domain + url

        data["cleanRouteId"] = cleanRouteId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response
