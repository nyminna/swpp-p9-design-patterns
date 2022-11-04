import time


class Counselor:
    def __init__(self):
        self.busy = False

    def talk(self):
        print("I am ready to talk")


class PhoneCall:
    def __init__(self, current_time='weekdays'):
        self.counselors = [Counselor(), Counselor()]
        self.current_time = current_time

    def talk(self):
        if self.current_time == 'weekdays':
            # TODO: fill this function
            # If you want, you can add time.sleep(0.1) before you call talk() in Counselor
            # to simulate the waiting time.
            for c in self.counselors:
                if not c.busy:
            if c.busy == False:
                c.talk()
                c.busy = True
            else:
                print("No available counselor")

            for c in self.counselors:
                if not c.busy:
                    c.busy = True.talk()


            
            
        else:
            time.sleep(0.1)
            print('Counselor will not talk to you')


if __name__ == "__main__":
    p = PhoneCall('weekdays')
    p.talk()
    p.talk()
    p.talk()

    p = PhoneCall('weekend')
    p.talk()

    """
    Expected Output

    > I am ready to talk
    > I am ready to talk
    > No available counselor
    > Counselor will not talk to you

    """
