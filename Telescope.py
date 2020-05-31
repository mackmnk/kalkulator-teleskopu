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
        if pupil < Telescope.__min_eye_pupil or pupil > Telescope.__max_eye_pupil:
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
            raise Exception('Invalid value. Pupil value should be in range from 0.3 to 7 ')        
        self.__pupil = pupil    

    def __init__(self, pupil=7):
        self.__diameter = 203
        self.__focal = 1200
        self.pupil = pupil
                  
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
        self.__maxzoom = self.__diameter*2
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
        self.__min_eyepiece_focal = round(self.__focal/(self.__diameter*2),1)
        return self.__min_eyepiece_focal            
         
    def calculate_maxmagnitudo(self):
        '''calculates maximum star range in magnitudo for the telescope under the dark sky (6.5mag)''' 
        self.__maxmag = round((5* math.log(self.__diameter/10,10) + 6.5),2)
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
        focal = int(input('Give me a telescope focal lenght: '))
        diameter = int(input('Give me a telescope diameter: '))
        
        x = Telescope()
        x.add_diameter_focal(diameter,focal)
        print(x)
    except Exception as e:
        print('Add input failed: ', e)