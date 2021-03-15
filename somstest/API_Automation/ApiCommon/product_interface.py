from Common.Request import *
from Params.params import *


class Product_interface():

    def __init__(self):
        self.request = Request()

    def addproduct(self, domain, token=None, appId=None, name=None):
        """
        新增商品
        :param  域名
        :param token
        :param appID
        :param  商品名称
        :return: 返回注册信息
        """
        url, data, header = request_data("product_interface", "add_product")
        apiUrl = domain + url

        data['storeId'] = appId
        data['name'] = name

        header['authorization'] = token
        header['appid'] = appId

        response = self.request.post_request(apiUrl, data, header)

        return response

    def add_classification(self, domain, token=None, appId=None, name=None):
        """
        新增商品分类
        :param 域名
        :param token
        :param appId
        :param 商品分类的名称
        :return: 返回注册信息
        """
        url, data, header = request_data("product_interface", "add_classification")
        apiUrl = domain + url

        data['storeId'] = appId
        data['name'] = name

        header['authorization'] = token
        header['appid'] = appId

        response = self.request.post_request(apiUrl, data, header)

        return response

    def getInfos(self, domain, token=None, appId=None):
        """
        确认商品分类添加成功
        :param 域名
        :param token
        :param appId
        :param 商品分类的名称
        :return: 返回注册信息
        """
        url, data, header = request_data("product_interface", "getInfos")
        apiUrl = domain + url

        data['storeId'] = appId

        header['authorization'] = token
        header['appid'] = appId

        response = self.request.get_request(apiUrl, data, header)

        return response

    def getDetails(self, domain, token=None, appId=None, keyword=None):
        """
        搜索要更新的商品
        :param 域名
        :param token
        :param appId
        :param 商品分类的名称
        :return: 返回注册信息
        """
        url, data, header = request_data("product_interface", "getDetails")
        apiUrl = domain + url

        data['storeId'] = appId
        data['keyword'] = keyword

        header['authorization'] = token
        header['appid'] = appId

        response = self.request.post_request(apiUrl, data, header)

        return response

    def updateRelationships(self, domain, token=None, appId=None, classificationIds=None, goodsIds=None):
        """
        切换商品到新的分类
        :param 域名
        :param token
        :param appId
        :param 商品分类的名称
        :return: 返回注册信息
        """
        url, data, header = request_data("product_interface", "updateRelationships")
        apiUrl = domain + url

        data['classificationIds'] = classificationIds
        data['goodsIds'] = goodsIds

        header['authorization'] = token
        header['appid'] = appId

        response = self.request.post_request(apiUrl, data, header)

        return response

    def isgetDetails(self, domain, token=None, appId=None, classificationId=None):
        """
        切换商品到新的分类
        :param 域名
        :param token
        :param appId
        :param 商品分类的名称
        :return: 返回注册信息
        """
        url, data, header = request_data("product_interface", "isgetDetails")
        apiUrl = domain + url

        data['storeId'] = appId
        data['classificationId'] = classificationId

        header['authorization'] = token
        header['appid'] = appId

        response = self.request.post_request(apiUrl, data, header)

        return response

    def apply(self, domain, token=None, appId=None, ids=None):
        """
        切换商品到新的分类
        :param 域名
        :param token
        :param appId
        :param 商品分类的名称
        :return: 返回注册信息
        """
        url, data, header = request_data("product_interface", "apply")
        apiUrl = domain + url

        data['ids'] = ids

        header['authorization'] = token
        header['appid'] = appId

        response = self.request.post_request(apiUrl, data, header)

        return response

    def remove(self, domain, token=None, appId=None, ids=None):
        """
        切换商品到新的分类
        :param 域名
        :param token
        :param appId
        :param 商品分类的名称
        :return: 返回注册信息
        """
        url, data, header = request_data("product_interface", "remove")
        apiUrl = domain + url

        data['ids'] = ids

        header['authorization'] = token
        header['appid'] = appId

        response = self.request.post_request(apiUrl, data, header)

        return response

    def deleteClass(self, domain, token=None, appId=None, id=None):
        """
        切换商品到新的分类
        :param 域名
        :param token
        :param appId
        :param 商品分类的名称
        :return: 返回注册信息
        """
        url, data, header = request_data("product_interface", "deleteClass")
        apiUrl = domain + url

        data['storeId'] = appId
        data['id'] = id

        header['authorization'] = token
        header['appid'] = appId

        response = self.request.post_request(apiUrl, data, header)

        return response