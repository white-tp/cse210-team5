
class font:
    def __init__(self):
        self.yellow_text = "\033[1;33m"
        self.red_text = "\033[1;31m"
    

    def print_title(self):
        print(f"{self.yellow_text}##     ## ####  ######   ##     ## ##        #######  ##      ## ")
        print("##     ##  ##  ##    ##  ##     ## ##       ##     ## ##  ##  ##")
        print("##     ##  ##  ##        ##     ## ##       ##     ## ##  ##  ##")
        print("#########  ##  ##   #### ######### ##       ##     ## ##  ##  ## ")
        print("##     ##  ##  ##    ##  ##     ## ##       ##     ## ##  ##  ##")
        print("##     ##  ##  ##    ##  ##     ## ##       ##     ## ##  ##  ## ")
        print("##     ## ####  ######   ##     ## ########  #######   ###  ###")
        print(f"\033[0m")