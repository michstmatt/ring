import uuid

class RingConstants:
    apiVersion = "11"
    rootURL = "https://api.ring.com"
    oauth = "https://oauth.ring.com/oauth/token"
    session = "%s/clients_api/session" % rootURL
    dings = "%s/clients_api/dings/active" % rootURL
    devices = "%s/clients_api/ring_devices" % rootURL
    history = "%s/clients_api/doorbots/history" % rootURL
    hardwareID = str(uuid.uuid4())

    @staticmethod
    def Recording(id: str):
        return "%s/clients_api/dings/%s/recording?disable_redirect=true" % (RingConstants.rootURL, id)

    @staticmethod
    def LiveStream(id: str):
        return "%s/clients_api/doorbots/%s/vod" % (RingConstants.rootURL, id)