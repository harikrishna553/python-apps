from pydantic import BaseModel, ValidationError

class Model(BaseModel):
    name: str

    class Config:
        max_anystr_length = 9
        error_msg_templates = {
            'value_error.any_str.max_length': 'max_length:{limit_value}',
        }


try:
    Model(name='krishna12345678')
except ValidationError as e:
    print(e)