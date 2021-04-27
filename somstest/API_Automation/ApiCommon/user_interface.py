from Common.Request import *
from Params.params import *


class User_interface():

    def __init__(self):
        self.request = Request()

    # 添加用户
    def add_user(self, domain, cookie):
        url, data, header = request_data("user_interface", "addUser")

        apiUrl = domain + url

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    # 查询用户
    def find_userByOrg(self, domain, cookie):
        url, data, header = request_data("user_interface", "findUserByOrg")

        apiUrl = domain + url

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    # 编辑用户
    def edit_user(self, domain, cookie, userId):
        url, data, header = request_data("user_interface", "updateUser")

        apiUrl = domain + url

        data["userId"] = userId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    # 查看用户
    def find_userById(self, domain, cookie, userId):
        url, data, header = request_data("user_interface", "findUserById")

        apiUrl = domain + url

        data["userId"] = userId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    # 用户授权角色
    def edit_userHasRole(self, domain, cookie, userId):
        url, data, header = request_data("user_interface", "updateUserHasRole")

        apiUrl = domain + url

        data["userId"] = userId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    # 解锁
    def unLockUser(self, domain, cookie, userId):
        url, data, header = request_data("user_interface", "unLockUser")

        apiUrl = domain + url

        data["userId"] = userId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    # 密码重置
    def resetPassword(self, domain, cookie, userId):
        url, data, header = request_data("user_interface", "resetPassword")

        apiUrl = domain + url

        data["userId"] = userId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    # 删除用户
    def delete_user(self, domain, cookie, userId):
        url, data, header = request_data("user_interface", "deleteUserById")

        apiUrl = domain + url

        data["userIds"] = userId + ","

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    # 登录历史
    def login_history(self, domain, cookie, time_start, time_end):
        url, data, header = request_data("user_interface", "findUserLoginHistory")

        apiUrl = domain + url

        data["timeStart"] = time_start
        data["timeEnd"] = time_end

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response
