import math

class GreatestCommonDenominator:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "a":("FLOAT",{"default":0.0, "min": 0.0, "max": 1000.0, "step": 1.0}),
                "b":("FLOAT",{"default":0.0, "min": 0.0, "max": 1000.0, "step": 1.0})
            }
        }
    RETURN_TYPES=("INT",)
    RETURN_NAMES=("INT",)
    FUNCTION="calculate"
    CATEGORY="math"

    def calculate(self,a,b):
        a=round(a)
        b=round(b)
        while(b):
            a,b=b,a%b
        return (a,)
    
class LowestCommonMultiple:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "a":("FLOAT",{"default":0.0, "min": 0.0, "max": 1000.0, "step": 1.0}),
                "b":("FLOAT",{"default":0.0, "min": 0.0, "max": 1000.0, "step": 1.0})
            }
        }
    RETURN_TYPES=("INT",)
    RETURN_NAMES=("INT",)
    FUNCTION="calculate"
    CATEGORY="math"

    def calculate(self,a,b):
        a=round(a)
        b=round(b)
        gcd1=a
        gcd2=b
        while(gcd2):
            gcd1,gcd2=gcd2,gcd1%gcd2
        return (a*b//gcd1,)

NODE_CLASS_MAPPINGS={
    "GreatestCommonDenominator":GreatestCommonDenominator,
    "LowestCommonMultiple":LowestCommonMultiple
}

NODE_DISPLAY_NAME_MAPPINGS={
    "GreatestCommonDenominator":"Greatest Common Denominator",
    "LowestCommonMultiple":"Lowest Common Multiple"
}