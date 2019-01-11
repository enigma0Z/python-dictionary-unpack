"""
Unpack Module
-------------

Getting Started
***************

Import the Unpack class::

    from unpack import Unpack

And then throw a dictionary into it::

    unpacked_data = Unpack(data)

Full Example
************

.. testsetup:: *

    from unpack import Unpack

Code:

.. testcode::

    from unpack import Unpack

    my_data = {
        "attribute": "value",
        "dictMember": {
            "blue": "0x0000ff",
            "red": "0xff0000"
        },
        "listMember": [ "one", "two", "three" ],
        "listOfDicts": [
            {
                "a": 1,
                "b": 2
            }, {
                "c": 3,
                "d": 4
            }
        ]
    }

    my_unpacked_data = Unpack(my_data)

    print(my_unpacked_data.attribute)
    print(my_unpacked_data.dictMember.blue)
    print(my_unpacked_data.listMember[0])
    print(my_unpacked_data.listOfDicts[0].a)

Expected Output:

.. testoutput::

    value
    0x0000ff
    one
    1
"""
from .unpack import Unpack
