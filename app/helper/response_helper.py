class ResponseComposer:
    """
        Response helper class for uniform response from all api
    """

    def __init__(self):
        self.data = {}

    def make_response(self, message="", payload={}, status_code=200, show=0):
        self.data["status_code"] = status_code
        self.data["message"] = message
        self.data["show"] = bool(show)
        self.data["payload"] = payload

        return self.data

    def pagination_response(
        self, message="", payload={}, status_code=200, show=0, pager={}
    ):
        self.data["status_code"] = status_code
        self.data["message"] = message
        self.data["show"] = bool(show)
        self.data["payload"] = payload
        self.data["pager"] = pager

        return self.data
