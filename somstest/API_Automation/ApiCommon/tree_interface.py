from Common.Request import *
from Params.params import *


class Tree_interface():

    def __init__(self):
        self.request = Request()

    def add_tree(self, domain, cookie, treeName=None):
        url, data, header = request_data("tree_interface", "addTree")

        apiUrl = domain + url

        data["treeName"] = treeName

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def find_tree(self, domain, cookie):
        url, data, header = request_data("tree_interface", "findTreeByPage")

        apiUrl = domain + url

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def edit_tree(self, domain, cookie, treeId, treeName):
        url, data, header = request_data("tree_interface", "updateTree")

        apiUrl = domain + url

        data["treeName"] = treeName
        data["treeId"] = treeId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def delete_tree(self, domain, cookie, treeId):
        url, data, header = request_data("tree_interface", "deleteTree")

        apiUrl = domain + url

        data["treeId"] = treeId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response
