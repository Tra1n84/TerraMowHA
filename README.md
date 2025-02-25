# TerraMow for Home Assistant

This is a Home Assistant integration for TerraMow robotic lawn mowers.

## Features

- Control lawn mower
- Monitor status and activity
- MQTT based communication

## Installation

1. Copy the `custom_components/terramow` folder to your Home Assistant `/config/custom_components` folder
2. Restart Home Assistant
3. Go to Settings -> Devices & Services -> Add Integration
4. Search for "TerraMow" and follow the configuration steps

## Configuration

The following parameters are required:

- Host: IP address or hostname of the TerraMow device
- Password: MQTT password

## Requirements

- Firmware version 6.6.0 or later is required.
- APP version 1.6.0 or later is required to change Home Assistant related configurations.

## Support

Open an issue on GitHub for support.
