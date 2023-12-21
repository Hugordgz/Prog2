

class Terminal:
    def __init__(self, phone_number):
        if not self.validate_phone_number(phone_number):
            print("Invalid phone number. Please enter a valid 9-digit number starting with 9, 6, or 7.")
        else:    
            self.phone_number = phone_number
        self.duration = 0

    def validate_phone_number(self, phone_number):
        result = False
        if(phone_number.isdigit() and phone_number[0] in ('9', '6', '7') and len(phone_number) == 9):
            result = True
        return result 
    
    def call(self, other_terminal, duration):
        if not isinstance(other_terminal, Terminal):
            print("Invalid argument. Please provide a valid Terminal object.")
        else:
            self.duration = duration
            other_terminal.duration = duration
    
    def __str__(self):
        formatted_phone_number = self.phone_number[:3] + ' ' + ' '.join([self.phone_number[i:i+2] for i in range(3, len(self.phone_number), 2)])
        return f"{formatted_phone_number} - Conversation time: {self.duration}s"
    
class Mobile(Terminal):
    def __init__(self, phone_number, rate):
        super().__init__(phone_number)
        if rate in ("rat", "monkey", "elephant"):
            self.rate = rate
        else:
            print("Invalid rate. Please enter a valid rate.")

if __name__ == "__main__": 
    t1 = Terminal("666112233")
    t2 = Terminal("666744459")
    t3 = Terminal("632128919")
    t4 = Terminal("664135818")
    print(t1)
    print(t2)
    t1.call(t2, 420)
    t1.call(t3, 210)
    print(t1)
    print(t2)
    print(t3)
    print(t4)
