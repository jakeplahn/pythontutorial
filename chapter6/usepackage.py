# import sound.effects.echo
# print(sound.effects.echo.echofilter())

# from sound.effects import echo
# print(echo.echofilter())

# from sound.effects.echo import echofilter
# print(echofilter())

# from sound.effects import *

from sound.effects import echo
print(echo.echofilter())

from sound.filters import vocoder
print(vocoder.heartbeat())