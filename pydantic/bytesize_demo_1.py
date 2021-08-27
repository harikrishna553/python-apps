from pydantic import (
    BaseModel,
    ByteSize,
    ValidationError
)

class PenDrive(BaseModel):
   size: ByteSize

try:
    drive1 = PenDrive(size = '1b')
    drive2 = PenDrive(size = '1kb')
    drive3 = PenDrive(size = '1mb')
    drive4 = PenDrive(size = '1gb')
    drive5 = PenDrive(size = '1tb')
    drive6 = PenDrive(size = '1pb')

    print(drive1.json())
    print(drive2.json())
    print(drive3.json())
    print(drive4.json())
    print(drive5.json())
    print(drive6.json())
    print('\n\n')

    drive1 = PenDrive(size = '1B')
    drive2 = PenDrive(size = '1kB')
    drive3 = PenDrive(size = '1mB')
    drive4 = PenDrive(size = '1gB')
    drive5 = PenDrive(size = '1tB')
    drive6 = PenDrive(size = '1pB')

    print(drive1.json())
    print(drive2.json())
    print(drive3.json())
    print(drive4.json())
    print(drive5.json())
    print(drive6.json())
    print('\n\n')

    drive1 = PenDrive(size = 1)
    drive2 = PenDrive(size = 1000)
    drive3 = PenDrive(size = 1000000)
    drive4 = PenDrive(size = 1000000000)
    drive5 = PenDrive(size = 1000000000000)
    drive6 = PenDrive(size = 1000000000000000)
    
    print(drive1.json())
    print(drive2.json())
    print(drive3.json())
    print(drive4.json())
    print(drive5.json())
    print(drive6.json())
    print('\n\n')

except ValidationError as e:
    print(e.json())
