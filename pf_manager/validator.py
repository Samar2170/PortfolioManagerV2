from numpy import require
from util.exceptions import CustomException, ValidationException


class Validator:
    @classmethod
    def validate_kwargs(cls,kwargs,required_keys):
        validation_flag, key = cls.isset_kwargs(kwargs,required_keys)
        if not validation_flag:
            raise ValidationException('Missing required key: {}'.format(key))

    @classmethod
    def validate_partial_kwargs(cls,kwargs,required_keys):
        validation_flag, key = cls.isset_partial_kwargs(kwargs,required_keys)
        if not validation_flag:
            raise ValidationException('Missing required key: {}'.format(key))

    @classmethod
    def isset_kwargs(cls, kwargs, required_keys):
        for key in required_keys:
            if key not in kwargs or kwargs[key] is None or kwargs[key]=='':
                return False, key
        return True, None

    @classmethod
    def validate_bank_name(cls, bank_name):
        bank_names_lower = [x.lower() for x in BANKS]
        if bank_name.lower() in bank_names_lower:
            return bank_name.upper()
        else:
            raise ValidationException('Invalid bank name')

    @classmethod
    def validate_ifsc(cls, ifsc):
        if isinstance(ifsc,str) and len(ifsc)==11:
            return ifsc
    
    @classmethod
    def isset_partial_kwargs(cls, kwargs, required_keys):
        if len(required_keys)==1:
            if required_keys[0] not in kwargs:
                return False, required_keys[0]
            else:
                return True, None
        else:
            matches = 0
            for key in required_keys:
                if key in kwargs:
                    matches += 1
            if matches >0:
                return True, None
            else:
                return False, required_keys[0]
            