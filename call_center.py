# Call Center Assignment

import random

class Call(object): #parent
    def __init__ (self, unique_id, name, number, time, reason):
        self.unique_id = unique_id
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason
        
    def basic_info(self): #method
        rand_num = random.randint (10000, 99999)
        print "Unique ID:", rand_num
        print ("Name: {}").format(self.name)
        print ("Phone Number: {}").format(self.number)
        print ("Time of Call: {}").format(self.time)
        print ("Reason for Call: {}").format(self.reason)
        print ('\n')
        return self

class CallCenter(object):
    def __init__ (self, *calls):
        self.calls = []
        self.queue = len(calls)
        for call in calls:
            self.calls.append(call)

    def add(self, call):
        self.calls.append(call)
        print (self.calls)
        self.queue += 1
        print "Number of Calls: {}".format(self.queue)
        return self
    
    def remove(self):
        self.calls.remove(self.calls[0])
        # print self.calls[0]
        return self

    def info(self): # works
        for i in range (len(self.calls)):
            print ("Name: " + self.calls[i].name)
            print ("Phone Number: " + self.calls[i].number)
        return self

def main ():
    call1 = Call("", "Harry", "111-222-3333", "10:30 AM", "Reason 1")
    call2 = Call("", "Ron", "333-444-5555", "12:30 PM", "Reason 2")
    call3 = Call("", "Hermione", "666-777-8888", "10:00 AM", "Reason 3")
    call4 = Call("", "Fred", "999-000-1111", "3:00 PM", "Reason 4")
    call5 = Call("", "George", "222-000-8888", "07:30 AM", "Reason 5")
    call6 = Call("", "Draco", "444-888-5555", "02:30 PM", "Reason 6")

    call_center = CallCenter(call1, call2, call3, call4).add(call5).remove().info()
main()


# WIP