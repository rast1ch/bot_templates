from enum import Enum


class ApplicationModeEnum(Enum):
    """
    Enum for application modes.
    """

    DEV = "DEV"
    STAGE = "STAGE"
    PROD = "PROD"
