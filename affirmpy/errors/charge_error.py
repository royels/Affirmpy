from .error import Error

class ChargeError(Error):
    DUPLICATE_CAPTURE_CODE = "duplicate-capture"


    def is_duplicate_capture(self):
        str(self.code) == ChargeError.DUPLICATE_CAPTURE_CODE
