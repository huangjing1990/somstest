from Common.Request import *
from Params.params import *


class VehicleBoxSet_interface():

    def __init__(self):
        self.request = Request()

    def add_vehicleBoxSet(self, domain, cookie, name=None):
        url, data, header = request_data("vehicleBoxSet_interface", "addVehicleBoxSet")

        apiUrl = domain + url

        data["name"] = name
        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def find_vehicleBoxSet(self, domain, cookie):
        url, data, header = request_data("vehicleBoxSet_interface", "findVehicleBoxSet")

        apiUrl = domain + url

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def edit_vehicleBoxSet(self, domain, cookie,  vehicleBoxSetId=None, name=None):
        url, data, header = request_data("vehicleBoxSet_interface", "updateVehicleBoxSet")

        apiUrl = domain + url

        data["vehicleBoxSetId"] = vehicleBoxSetId
        data["name"] = name

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def delete_vehicleBoxSet(self, domain, cookie, vehicleBoxSetId=None):
        url, data, header = request_data("vehicleBoxSet_interface", "deleteVehicleBoxSet")

        apiUrl = domain + url

        data["vehicleBoxSetId"] = vehicleBoxSetId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

