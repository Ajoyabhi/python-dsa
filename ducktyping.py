class jioCaller():
    def call(self):
        print("calling")
class trueCaller():
    def call(self):
        print("ringing")
        print("caller data")
class phone:
    def callfunc(self, phoneApp):
        phoneApp.call()
phoneApp = jioCaller()
p1 = phone()
p1.callfunc(phoneApp)