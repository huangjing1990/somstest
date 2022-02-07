from Common.Request import *
from Params.params import *


class CleanPlan_interface():

    def __init__(self):
        self.request = Request()

    def add_cleanPlan(self, domain, cookie, routeIds=None, month=None):
        url, data, header = request_data("cleanPlan_interface", "addCleanPlan")

        apiUrl = domain + url

        data["routeIds"] = routeIds
        data["month"] = month

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def find_cleanPlan(self, domain, cookie, monthStart=None, monthEnd=None):
        url, data, header = request_data("cleanPlan_interface", "findCleanPlan")

        apiUrl = domain + url

        data["monthStart"] = monthStart
        data["monthEnd"] = monthEnd

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def edit_cleanPlan(self, domain, cookie, cleanPlanId=None, month=None):
        url, data, header = request_data("cleanPlan_interface", "updateCleanPlan")

        apiUrl = domain + url

        data["cleanPlanId"] = cleanPlanId
        data["month"] = month

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def add_cleanPlanDetail(self, domain, cookie, date=None, cleanPlanId=None):
        url, data, header = request_data("cleanPlan_interface", "addCleanPlanDetail")

        apiUrl = domain + url

        data["date"] = date
        data["cleanPlanId"] = cleanPlanId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    # 顺延计划明细
    def postponeCleanPlanDetail(self, domain, cookie, cleanPlanId=None, date=None, driverDays=None, vehicleDays=None):
        url, data, header = request_data("cleanPlan_interface", "postponeCleanPlanDetail")

        apiUrl = domain + url

        data["cleanPlanId"] = cleanPlanId
        data["date"] = date
        data["driverDays"] = driverDays
        data["vehicleDays"] = vehicleDays

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    # 提交审核
    def submitCleanPlan(self, domain, cookie, cleanPlanIds=None):
        url, data, header = request_data("cleanPlan_interface", "submitCleanPlan")

        apiUrl = domain + url

        data["cleanPlanIds"] = cleanPlanIds

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    # 查询审核记录
    def findCleanAuditing(self, domain, cookie, monthStart=None, monthEnd=None):
        url, data, header = request_data("cleanPlan_interface", "findCleanAuditing")

        apiUrl = domain + url

        data["monthStart"] = monthStart
        data["monthEnd"] = monthEnd

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    # 审核通过
    def cleanAuditing(self, domain, cookie, cleanPlanIds=None):
        url, data, header = request_data("cleanPlan_interface", "cleanAuditing")

        apiUrl = domain + url

        data["cleanPlanIds"] = cleanPlanIds

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def delete_cleanPlan(self, domain, cookie, CleanPlanId=None):
        url, data, header = request_data("cleanPlan_interface", "deleteCleanPlan")

        apiUrl = domain + url

        data["CleanPlanId"] = CleanPlanId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response
