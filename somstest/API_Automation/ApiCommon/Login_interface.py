from Common.Request import *
from Params.params import *


class Login_interface():

    def __init__(self):
        self.request = Request()

    def login(self, domain, lu=None, pd=None):
        url, data, header = request_data("login_interface", "login")
        apiUrl = domain + url

        data['lu'] = lu
        data['pd'] = pd

        response = self.request.post_request(apiUrl, data, header)
        # token = response['body']['data']['token']
        # appID = response['body']['data']['apps'][0]['appId']
        return response

    def get_userToken(self, domain, appId, token):
        """
        用户登陆
        :param URL地址
        :param 用户登陆appID
        :return: 返回用户登陆后的token
        """
        url, data, header = request_data("login_interface", "getUserToken")
        apiUrl = domain + url

        data['appId'] = appId
        header['authorization'] = token
        header['appid'] = appId

        response = self.request.get_request(apiUrl, data, header)
        token = response['body']['data']['token']
        return token

    def logout(self, domain, appId, token):
        """
        退出登录
        :param URL地址
        :param 用户登陆appID
        :return: 返回用户登陆后的token
        """
        url, data, header = request_data("login_interface", "logout")
        apiUrl = domain + url

        header['authorization'] = token
        header['appid'] = appId

        response = self.request.get_request(apiUrl, data, header)

        return response
