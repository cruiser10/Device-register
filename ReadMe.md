# Device Registry service
import json


## Usage

All responses will have the form 

'''json
{
  "data" : "mixed type holding the content "
  "message" : "description of what happened"
}
'''

Subsequent response definition will only detail the expected value of the 'data field'

### List all devices

**Definition**

'GET /devices'

**Response**

- '200 OK' on sucesss

'''json
{
      "identifier" : "vivo",
      "name" : "my mobile",
      "device_type" : "mobile",
      "controller_gateway" : "100.93.254.165"
}
'''

### Registring a new device 

**definition**

'POST /devices'

**Arguments**

- '"identifier" :string' a globally unique identifier 
- '"name" : owner' whose mobile is this 
- '"device_type" : string' type of mobile 
- '"controller_gateway" : string' IP addresss 

If a device with the given identifier already exists, the existing device will be overwritten

**Response**

- '201 created' on success

'''json
{
    
      "identifier" : "vivo",
      "name" : "my mobile",
      "device_type" : "mobile",
      "controller_gateway" : "100.93.254.165"
}
'''

##lookup device details

'GET /device/<identifier>'

**responses**

- '404 Not Found' device does not exist
- '200 OK ' on success

'''json
{
    
      "identifier" : "vivo",
      "name" : "my mobile",
      "device_type" : "mobile",
      "controller_gateway" : "100.93.254.165"
}
'''

## Delete a device 

'DELETE /devices/<identifier>'

**Response**
- '404 Not Found' device does not exist
- '201 No Content'