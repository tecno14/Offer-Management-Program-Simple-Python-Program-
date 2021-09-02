import enum

class categories(enum.Enum):
    mobile_app = "mobile_app"
    website = "website"
    microservice = "microservice"

    @staticmethod
    def getAllList():
        return [
            categories.mobile_app,
            categories.website,
            categories.microservice
        ]
