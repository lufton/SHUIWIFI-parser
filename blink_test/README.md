This is a simple test firmware to verify you have soldered all required pins correctly.

Flash it using next command (replace <PORT> with real one, e.g. COM3):
```commandline
python -m esptool --port <PORT> write_flash 0x1000 bootloader.bin 0x8000 partitions.bin 0xe000 boot_app0.bin 0x010000 firmware.bin
```
If you were able to flash your module and LED connected to GPIO4 is blinking than you have done everything right! Congratulations! Now you can flash the module as described on the main page of this repo.