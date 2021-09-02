import enum

class tags(enum.Enum):
    e_commerce = "e_commerce"
    delivery = "delivery"
    maps = "maps"
    tracking = "tracking"

    @staticmethod
    def getAllList():
        return [
            tags.e_commerce,
            tags.delivery,
            tags.maps,
            tags.tracking
        ]