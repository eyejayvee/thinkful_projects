class Musician(object):
    def __init__(self, sounds, name):
        self.sounds = sounds
        self.name = name

    def solo(self, length):
        for i in range(length):
            print self.sounds[i % len(self.sounds)],
        print ""

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Bassist, self).__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Guitarist, self).__init__(["Boink", "Bow", "Fwnang"])

class Drummer(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Drummer, self).__init__(["Boom", "Clash", "Tack"])

    def tune(self):
        print "Be with you in a moment"
        print "Twoning, sproing, splang"

#class Band(Musician):
#    pass

def main():
    print "I am looking to start a band! Tell me about yourself and play a little. If I like you, you're in!"
    band_no = 1 # thats me, the lead singer

    while band_no < 4:
      applicant = add_muso = raw_input("What is your name? ")
      instrument =  raw_input("What instrument do you play? Bass, Guitar or Drums? ")

      if instrument == "bass":
          applicant = Bassist()
      elif instrument == "guitar":
          applicant = Guitarist()
      elif  instrument == "drums":
          applicant = Drummer()
      
      print "Let's here you play %s.", applicant #not quite getting the issue / solution here
      applicant.solo(6)

      in_or_out = raw_input("Hmmm, let me think, so I add you or not? ")
      
      if in_or_out == "y":
        band_no += 1
        print "You know, I kinnda like you and you can play a decent tune there. You're in!"
      else:
        print "I'm sorry, I don't think you are what the band needs right now. Keep on jamming, you'll hit the big time one day."
      
if __name__ == '__main__':
    main()