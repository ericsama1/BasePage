from settings import language

if language == 'en':
    from i18n.en.messages import (
        BaseBrowserConstants, BaseElementConstants, BasePageConstants,
        BaseRadioConstants, BaseSelectConstants
    )
elif language == 'es':
    from i18n.es.messages import (
        BaseBrowserConstants, BaseElementConstants, BasePageConstants,
        BaseRadioConstants, BaseSelectConstants
    )
else:
    from i18n.other.messages import (
        BaseBrowserConstants, BaseElementConstants, BasePageConstants,
        BaseRadioConstants, BaseSelectConstants
    )


# Browsers
CHROME = 'chrome'
FIREFOX = 'firefox'
IE = 'ie'
OPERA = 'opera'
EDGE = 'edge'

# Attributes
VALUE = 'value'


class Message(
        BaseBrowserConstants, BaseElementConstants, BasePageConstants,
        BaseRadioConstants, BaseSelectConstants
        ):
    pass
