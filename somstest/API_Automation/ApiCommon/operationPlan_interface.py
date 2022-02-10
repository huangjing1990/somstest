from Common.Request import *
from Params.params import *


class OperationPlan_interface():

    def __init__(self):
        self.request = Request()

    # 添加人工计划
    def add_operationPlan(self, domain, cookie, roadSectionIds=None, month=None):
        url, data, header = request_data("operationPlan_interface", "addOperationPlan")

        apiUrl = domain + url

        data["roadSectionIds"] = roadSectionIds
        data["month"] = month

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    # 查询人工计划
    def find_operationPlan(self, domain, cookie, monthStart=None, monthEnd=None, roadSectionIds=None):
        url, data, header = request_data("operationPlan_interface", "findOperationPlan")

        apiUrl = domain + url

        data["monthStart"] = monthStart
        data["monthEnd"] = monthEnd
        data["roadSectionIds"] = roadSectionIds

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    # 编辑人工计划
    def edit_operationPlan(self, domain, cookie, operationPlanId=None, month=None):
        url, data, header = request_data("operationPlan_interface", "editOperationPlan")

        apiUrl = domain + url

        data["operationPlanId"] = operationPlanId
        data["month"] = month

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    # 新建计划明细
    def add_PlanDetail(self, domain, cookie, date=None, operationPlanId=None, usersId=None):
        url, data, header = request_data("operationPlan_interface", "addPlanDetail")

        apiUrl = domain + url

        data["date"] = date
        data["operationPlanId"] = operationPlanId
        data["usersId"] = usersId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    # 顺延计划明细
    def postponePlanDetail(self, domain, cookie, operationPlanId=None, roadSectionId=None, date=None, taskdays=None,
                           userdays=None):
        url, data, header = request_data("operationPlan_interface", "postponePlanDetail")

        apiUrl = domain + url

        data["operationPlanId"] = operationPlanId
        data["roadSectionId"] = roadSectionId
        data["date"] = date
        data["taskdays"] = taskdays
        data["userdays"] = userdays

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    # 提交审核
    def submitOperationPlan(self, domain, cookie, operationPlanIds=None):
        url, data, header = request_data("operationPlan_interface", "submitOperationPlan")

        apiUrl = domain + url

        data["operationPlanIds"] = operationPlanIds

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    # 查询审核记录
    def findOperationAuditing(self, domain, cookie, monthStart=None, monthEnd=None):
        url, data, header = request_data("operationPlan_interface", "findOperationAuditing")

        apiUrl = domain + url

        data["monthStart"] = monthStart
        data["monthEnd"] = monthEnd

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    # 审核通过
    def createAuditing(self, domain, cookie, operationPlanIds=None):
        url, data, header = request_data("operationPlan_interface", "createAuditing")

        apiUrl = domain + url

        data["operationPlanIds"] = operationPlanIds

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    # 下发计划
    def issueOperationPlan(self, domain, cookie, operationPlanIds=None):
        url, data, header = request_data("operationPlan_interface", "issueOperationPlan")

        apiUrl = domain + url

        data["operationPlanIds"] = operationPlanIds

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    # 顺延计划
    def postponePlan(self, domain, cookie, operationPlanIds=None):
        url, data, header = request_data("operationPlan_interface", "postponePlan")

        apiUrl = domain + url

        data["operationPlanIds"] = operationPlanIds

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    # 删除计划
    def deleteOperationPlan(self, domain, cookie, operationPlanId=None):
        url, data, header = request_data("operationPlan_interface", "deleteOperationPlan")

        apiUrl = domain + url

        data["operationPlanId"] = operationPlanId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response
