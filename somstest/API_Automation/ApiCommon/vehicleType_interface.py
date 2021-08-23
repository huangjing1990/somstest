from Common.Request import *
from Params.params import *


class VehicleType_interface():

    def __init__(self):
        self.request = Request()

    def add_vehicleType(self, domain, cookie):
        url, data, header = request_data("vehicleType_interface", "addVehicleWorkType")

        apiUrl = domain + url

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def find_vehicleType(self, domain, cookie):
        url, data, header = request_data("vehicleType_interface", "findVehicleWorkTypeByPage")

        apiUrl = domain + url

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def edit_vehicleType(self, domain, cookie, workTypeId):
        url, data, header = request_data("vehicleType_interface", "updateVehicleWorkType")

        apiUrl = domain + url

        data["workTypeId"] = workTypeId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def delete_vehicleType(self, domain, cookie, workTypeId):
        url, data, header = request_data("vehicleType_interface", "deleteVehicleWorkType")

        apiUrl = domain + url

        data["workTypeId"] = workTypeId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response
