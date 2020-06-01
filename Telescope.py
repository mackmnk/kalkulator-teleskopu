# Class Telescope, author: Maciej Mindziak
import math
class Telescope(object):

    '''This is a class Telescope, it has 3 atributes:
    pupil in mm set to default value of 7mm
    two attributes accessed by add_apperture_focal method:
    diameter size in mm and focal lenght in mm 

    It raises an exception if:
    diameter and/or focal lenght have non-positive values
    focal lenght is bigger than 5500 mm
    diameter is equal or bigger than focal lenght

    There are 7 methods that can be used by the class instance:
    calculate_fvalue()  - calculate fast diameter value for the given parameters
    calculate_resolution() - calculate angular for the given parameters 
    calculate_maxzoom() - calculate maximum useful magnification value for the given parameters
    calculate_minzoom() - calculate minimum useful magnification value for the given parameters
    calculate_max_eyepiece_focal() - calculate maximum useful eyepiece focal value for the given parameters
    calculate_min_eyepiece_focal() - calculate minimum useful eyepiece focal value for the given parameters
    calculate_maxmagnitudo() - calculate maximum star range in magnitudo for the given parameters    
     '''
    # Telescope class variables, determine ranges of diameter, focal and exit_pupil
    __min_eye_pupil = 0.5
    __max_eye_pupil = 7
    __min_focal = 15
    __max_focal = 6000
    __min_diameter = 10
    __max_diameter = 2000
    __min_skymag = 0.0
    __max_skymag = 7.5 
    __min_multiplier = 1.0
    __max_multiplier = 3.0    

    @staticmethod    
    def validate_diameter(diameter):
        '''checks if diameter is in range of 30mm to 2000mm, if not it returns False'''
        if diameter < Telescope.__min_diameter or diameter > Telescope.__max_diameter:
            return False   
        return True
        
    @staticmethod    
    def validate_diameter_vs_focal(focal, diameter):
        '''checks if focal is larger than diameter, if not it returns False'''
        if diameter >= focal:
            return False   
        return True
    
    @staticmethod    
    def validate_focal(focal):
        '''checks if focal is in range of Telescope.__min_focal to Telescope.__max_focal, if not it returns False'''
        if focal < Telescope.__min_focal or focal > Telescope.__max_focal:
            return False   
        return True
    
    @staticmethod
    def validate_pupil(pupil):
        '''checks if pupil is in range of Telescope.__min_pupil to Telescope.__max_pupil, if not it returns False'''
        if pupil < Telescope.__min_eye_pupil or pupil > Telescope.__max_eye_pupil:
            return False   
        return True

    @staticmethod
    def validate_skymag(skymag):
        '''checks if skymag is in range of Telescope.__min_skymag to Telescope.__max_skymag, if not it returns False'''
        if skymag < Telescope.__min_skymag or skymag > Telescope.__max_skymag:
            return False   
        return True 

    @staticmethod
    def validate_multiplier(multiplier):
        '''checks if multiplier is in range of Telescope.__min_multiplier to Telescope.__max_multiplier, if not it returns False'''
        if multiplier < Telescope.__min_multiplier or multiplier > Telescope.__max_multiplier:
            return False   
        return True 

    def add_diameter_focal(self, focal, diameter):

        '''checks if diameter and focal values are valid, 
        if so it sets new values for self.__diameter and'''

        if not Telescope.validate_diameter(diameter):
            raise Exception('Nieprawidłowa wartość średnicy lustra. Wpisz liczbę od 30 do 2,000')
        elif not Telescope.validate_focal(focal):
            raise Exception('Nieprawidłowa wartość ogniskowej. Wpisz liczbę od 15 do 6,000 ')
        elif not Telescope.validate_diameter_vs_focal(focal, diameter):
            raise Exception('Ogniskowa powinna być większa niż średnica lustra')
        self.__diameter = diameter
        self.__focal = focal                   
       
    @property
    def pupil(self):
        return self.__pupil

    @pupil.setter
    def pupil(self, pupil):
        '''checks if eye pupil value is valid, if so it sets private property atribute name = pupil'''
        if not Telescope.validate_pupil(pupil):
            raise Exception('Nieprawidłowa wartość źrenicy wyjściowej. Wpisz liczbę od 0 do 7')        
        self.__pupil = pupil

    @property
    def skymag(self):
        return self.__skymag

    @skymag.setter
    def skymag(self, skymag):
        '''checks if skymag value is valid, if so it sets private property atribute name = skymag'''
        if not Telescope.validate_skymag(skymag):
            raise Exception('Nieprawidłowa wartość magnitudo. Wpisz liczbę od 0 do 7.5')        
        self.__skymag = skymag

    @property
    def multiplier(self):
        return self.__multiplier

    @multiplier.setter
    def multiplier(self, multiplier):
        '''checks if multiplier value is valid, if so it sets private property atribute name = multiplier'''
        if not Telescope.validate_multiplier(multiplier):
            raise Exception('Nieprawidłowa wartość mnożnika średnicy teleskopu. Wpisz liczbę od 1 do 3')        
        self.__multiplier = multiplier             

    def __init__(self, pupil=6, skymag=6.5, multiplier=2):
        self.__diameter = 203
        self.__focal = 1200
        self.pupil = pupil
        self.skymag = skymag
        self.multiplier = multiplier
                  
    def calculate_fvalue(self):
        '''calculates fast diameter value'''
        self.__fvalue = round(self.__focal/self.__diameter,2)
        return self.__fvalue
        
    def calculate_resolution(self):
        '''calculates angular resolution'''
        self.__ang_resolution = round(138/self.__diameter,2)
        return self.__ang_resolution
    
    def calculate_maxzoom(self): 
        '''calculates max zoom available for the telescope'''
        self.__maxzoom = self.__diameter*self.multiplier
        return self.__maxzoom
        
    def calculate_minzoom(self):
        '''calculates min zoom available for the telescope''' 
        self.__minzoom = round(self.__diameter/self.pupil)
        return self.__minzoom

    def calculate_max_eyepiece_focal(self):
        '''calculates max eyepiece focal lenght for the telescope'''
        self.__max_eyepiece_focal = round(self.__focal/self.__minzoom)
        return self.__max_eyepiece_focal
        
    def calculate_min_eyepiece_focal(self):
        '''calculates minimum eyepiece focal lenght for the telescope'''
        self.__min_eyepiece_focal = round(self.__focal/(self.__maxzoom),1)
        return self.__min_eyepiece_focal            
         
    def calculate_maxmagnitudo(self):
        '''calculates maximum star range in magnitudo for the telescope under the dark sky (6.5mag)''' 
        self.__maxmag = round((5* math.log(self.__diameter/10,10) + self.skymag),2)
        return self.__maxmag
    
    def __str__(self):
        template = '''Parametry teleskopu o aperturze {0} mm i ogniskowej {1} mm:
        - światłosiła wynosi F/{2}
        - maksymalne użyteczne powiększenie wynosi {3}x
        - minimalne użyteczne powiększenie zakładając źrenicę wyjściową {4} mm wynosi {5}x 
        - maksymalna użyteczna ogniskowa okularu to {6} mm
        - minimalna użyteczna ogniskowa okularu to {7} mm
        - maksymalna zdolność rozdzielcza to {8}"
        - maksymalny zasięg gwiazdowy teleskopu pod ciemnym niebem (6.5 mag) to {9} mag'''
        return template.format(self.__diameter, self.__focal, self.calculate_fvalue(), self.calculate_maxzoom(), self.pupil, self.calculate_minzoom(),\
        self.calculate_max_eyepiece_focal(), self.calculate_min_eyepiece_focal(), self.calculate_resolution(), self.calculate_maxmagnitudo())


 
        
 
if __name__ == '__main__':
    #Create an instance and use all the available methods 
    try:
        focal = float(input('Give me a telescope focal lenght: '))
        diameter = float(input('Give me a telescope diameter: '))
        pupil = float(input('Give me your pupil diameter: '))
        skymag = float(input('Give me a sky magnitudo value: '))
        multiplier = float(input('Give me a diameter multiplier value: '))
        x = Telescope(pupil, skymag, multiplier)
        x.add_diameter_focal(focal,diameter)
        print(x)
    except Exception as e:
        print('Add input failed: ', e)