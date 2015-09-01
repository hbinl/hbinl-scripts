__author__ = 'HaoBin'

class Logger(object):
    def __init__(self, filename="output.txt"):
        self.terminal = sys.stdout
        filename = "permute_output_" + str(time.time()) + ".txt"
        self.log = open(filename, "w")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass