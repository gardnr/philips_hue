# Philips Hue

Tested with Hue white lamp [model: LWB014](https://www2.meethue.com/en-us/p/hue-white-dual-pack-e26/046677530372)

[Device setup instructions](https://developers.meethue.com/develop/get-started-2/)

```
$ pip install -r requirements.txt

$ gardnr add driver hue driver:Hue -c bridge_address=192.168.1.2 -c light_number=1
```

*NOTE*

To register GARDNR with the Bridge, you must manually run either the power on or off command within 30 seconds after pressing the button on the Bridge. This only needs to be done once.
