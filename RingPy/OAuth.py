import time

class OAuth:
    accessToken = ""
    refreshToken = ""
    expiresIn = 0
    expireTime = 0
    scope = ""
    tokenType = ""
    __header = None

    def getRequestHeader(self):
        if self.__header is None:
            self.__header = {
                "Content-Type": "application/json",
                "Authorization": "Bearer %s" % self.accessToken
            }
        return self.__header

    @staticmethod
    def fromDictionary(data: map):
        oa = OAuth()
        oa.accessToken = data["access_token"]
        oa.refreshToken = data["refresh_token"]
        oa.expiresIn = data["expires_in"]
        oa.expireTime = time.time() + oa.expiresIn
        oa.scope = data["scope"]
        oa.tokenType = data["token_type"]

        return oa
