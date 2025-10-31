class MCPLogger:
    def __init__(self):
        self.to = ''
    

    def logger(self, message, to):
        self.to = to

    def logger_info(self):
        return self.to