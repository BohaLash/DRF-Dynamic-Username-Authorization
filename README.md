# DRF-Dynamic-Username-Authorization
 Django backend for auth with different username fields for different user types


### How to use:
  1. Add code from `backends.py` to your project.
  2. Create a custom backend for your model 
  by inheriting `DynamicUsernameBackend`
  and specifying `USERNAME_FIELD`:
```py
from crm.backends import DynamicUsernameBackend
from .models import Client


class ClientBackend(DynamicUsernameBackend):
    USERNAME_FIELD = 'email'

```
  2. Edit `settings.py` and add your custom backend:
  ```py
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'client.backends.ClientBackend',
    # ...,
]
```
