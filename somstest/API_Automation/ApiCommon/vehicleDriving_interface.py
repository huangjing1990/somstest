from Common.Request import *
from Params.params import *


class VehicleDriving_interface():

    def __init__(self):
        self.request = Request()

    # 实时定位
    def getVehicleLatestPosition(self, domain, cookie):
        url, data, header = request_data("vehicleDriving_interface", "getVehicleLatestPosition")

        apiUrl = domain + url

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    # 车辆信息框
    def getVehiclestate(self, domain, cookie):
        url, data, header = request_data("vehicleDriving_interface", "getVehiclestate")

        apiUrl = domain + url

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    # 轨迹回放
    def getTrajectory(self, domain, cookie):
        url, data, header = request_data("vehicleDriving_interface", "getTrajectory")

        apiUrl = domain + url

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response
