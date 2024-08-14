## Packages to install
### pyttsx3
### pyaudio
### speechRecognition
### wikipedia

## Code which you want to change in __init__ file
```
from disutils.version import LooseVersion
        if LooseVersion(pyaudio.__version__) < LooseVersion("0.2.11"):
            raise AttributeError("PyAudio 0.2.11 or later is required (found version {})".format(pyaudio.__version__))
        return pyaudio
```
##  replace the above code with the given code
```
from packaging.version import Version
        if Version(pyaudio.__version__) < Version("0.2.11"):
            raise AttributeError("PyAudio 0.2.11 or later is required (found version {})".format(pyaudio.__version__))
        return pyaudio
```
## then install packaging package
