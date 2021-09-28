from Common.Request import *
from Params.params import *


class PatrolItems_interface():

    def __init__(self):
        self.request = Request()

    def add_patrolItem(self, domain, cookie, parentItemId=None, operationItemName=None, itemType=None):
        url, data, header = request_data("patrolItems_interface", "addPatrolItem")

        apiUrl = domain + url
        data["parentItemId"] = parentItemId
        data["operationItemName"] = operationItemName
        data["itemType"] = itemType
        # itemType:0 检查类；1检查项

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def find_patrolItem(self, domain, cookie):
        url, data, header = request_data("patrolItems_interface", "findPatrolItem")

        apiUrl = domain + url

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def edit_patrolItem(self, domain, cookie, parentItemId=None, operationItemId=None, operationItemName=None,
                        itemType=None):
        url, data, header = request_data("patrolItems_interface", "editPatrolItem")

        apiUrl = domain + url
        data["parentItemId"] = parentItemId
        data["operationItemId"] = operationItemId
        data["operationItemName"] = operationItemName
        data["itemType"] = itemType
        # itemType:0 检查类；1检查项

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def delete_patrolItem(self, domain, cookie, operationItemId=None):
        url, data, header = request_data("patrolItems_interface", "deletePatrolItem")

        apiUrl = domain + url
        data["operationItemId"] = operationItemId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response
