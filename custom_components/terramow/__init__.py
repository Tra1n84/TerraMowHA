"""The TerraMow integration."""

from __future__ import annotations

from dataclasses import dataclass
import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    CONF_HOST,
    CONF_PASSWORD,
    Platform,
)
from homeassistant.core import HomeAssistant

_LOGGER = logging.getLogger(__name__)

PLATFORMS: list[Platform] = [Platform.LAWN_MOWER]

@dataclass
class TerraMowBasicData:
    host: str
    password: str

type TerraMowConfigEntry = ConfigEntry[TerraMowBasicData]

async def async_setup_entry(hass: HomeAssistant, entry: TerraMowConfigEntry) -> bool:
    host = entry.data[CONF_HOST]
    password = entry.data[CONF_PASSWORD]

    _LOGGER.info("Setting up TerraMow with host %s", host)

    basic_data = TerraMowBasicData(host=host, password=password)
    entry.runtime_data = basic_data

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: TerraMowConfigEntry) -> bool:
    """Unload a config entry."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
