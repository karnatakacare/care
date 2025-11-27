from plugs.manager import PlugManager
from plugs.plug import Plug

abdm_plugin = Plug(
    name="abdm",
    package_name="git+https://github.com/10bedicu/care_abdm.git",
    version="@production",
    configs={}
)


gateway_device_plugin = Plug(
    name="gateway_device",
    package_name="git+https://github.com/10bedicu/care_teleicu_devices.git",
    version="@main",
    configs={}
)

camera_device_plugin = Plug(
    name="camera_device",
    package_name="git+https://github.com/10bedicu/care_teleicu_devices.git",
    version="@main",
    configs={}
)

vitals_observation_device_plugin = Plug(
    name="vitals_observation_device",
    package_name="git+https://github.com/10bedicu/care_teleicu_devices.git",
    version="@main",
    configs={}
)

care_auto_tag_plugin = Plug(
    name="care_auto_tag",
    package_name="git+https://github.com/10bedicu/care_auto_tag.git",
    version="@main",
    configs={},
)

plugs = [
    abdm_plugin,
    gateway_device_plugin,
    camera_device_plugin,
    vitals_observation_device_plugin,
    care_auto_tag_plugin
]

manager = PlugManager(plugs)
