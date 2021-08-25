from pydantic import BaseModel, ValidationError

class Employee(BaseModel):
    name: str

    class Config:
        max_anystr_length = 9
        error_msg_templates = {
            'value_error.any_str.max_length': 'max_length:{limit_value}',
        }


configClass = Employee.__config__()

print(configClass.max_anystr_length)
print(configClass.error_msg_templates)