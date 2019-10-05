import requests
import json
import time
import os
from .RingConstants import RingConstants
from .OAuth import OAuth



class Ring:
    oAuth = None
    sessionToken = None
    authSession = {"api_version": RingConstants.apiVersion, "auth_token": ""}
    chimes = []
    cameras = []

    def Authenticate(self, username, password):
        body = {
            "client_id": "ring_official_android",
            "grant_type": "password",
            "password": password,
            "scope": "client",
            "username": username
        }

        response = requests.post(RingConstants.oauth, json.dumps(body))
        if response.status_code == 200:
            self.oAuth = OAuth.fromDictionary(response.json())
            return True
        else:
            return False

    def EstablishSession(self):
        body = {
            "device": {
                "hardware_id": RingConstants.hardwareID,
                "metadata": {
                    "api_version": RingConstants.apiVersion,
                },
                "os": "android"
            }
        }
        headers = self.oAuth.getRequestHeader()

        response = requests.post(
            RingConstants.session, json.dumps(body), headers=headers)
        if response.status_code == 201:
            self.sessionToken = response.json(
            )["profile"]["authentication_token"]
            self.authSession["auth_token"] = self.sessionToken
            return True
        else:
            return False

    def GetDevices(self):
        response = requests.get(RingConstants.devices, params=self.authSession)
        data = response.json()
        self.chimes = data["chimes"]
        self.cameras = data["stickup_cams"]

    def PollForDing(self):
        response = requests.get(RingConstants.dings, params=self.authSession)
        data = response.json()
        return data

    def GetHistory(self):
        response = requests.get(RingConstants.history, params=self.authSession)
        return (response.json())

    def GetLiveStream(self, id):
        response = requests.post(
            RingConstants.LiveStream(id), params=self.authSession
            )
        print(response.status_code, response.content)

    def GetRecording(self, id: str, path: str):
        response = requests.get(
            RingConstants.Recording(id), params=self.authSession
            )
        data = response.json()

        print("Downloading", id)
        mp4response = requests.get(data["url"])
        fileName = "./%s/%d.mp4" % (path, id)   
        with open(fileName, "wb") as f:
            f.write(mp4response.content)

    def GetChimes(self):
        pass
