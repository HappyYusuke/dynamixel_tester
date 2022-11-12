#!/usr/bin/env python3i
import sys
import time

class Converter():
    def __init__(self):
        self.deg_or_step = 0
        self.value = 0.0

    def degToStep(self, deg):
        return int((deg+180)/360.0*4095)

    def stepToDeg(self, step):
        return round(step/4095.0*360.0-180, 1)

    def convert(self):
        if self.deg_or_step == 1:
            self.value = float(input('Degree >>> '))
            return self.degToStep(self.value)
        else:
            self.value = float(input('Step >>> '))
            return self.stepToDeg(self.value)

    def modeChange(self):
        while True:
            try:
                self.deg_or_step = int(input('1: Degree to Step\n2: Step to Degree\n>>> '))
                print()
                if self.deg_or_step != 1 and self.deg_or_step != 2:
                    print('Please enter 1 or 2. \n')
                else:
                    break
            except ValueError:
                print('\nPlease enter 1 or 2. \n')
            except KeyboardInterrupt:
                print('\nExit...')
                sys.exit()

    def loop(self):
        while True:
            try:
                print(f'{self.convert()}\n')
            except ValueError:
                print('Please enter a numerical value\n')
            except KeyboardInterrupt:
                print('\n')
                self.modeChange()
       
    def execute(self):
        self.modeChange()
        self.loop()



if __name__ == '__main__':
    c = Converter()
    # True はループ. False は毎回選択.T
    c.execute()
