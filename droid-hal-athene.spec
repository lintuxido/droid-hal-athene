# These and other macros are documented in dhd/droid-hal-device.inc
%define device athene
%define vendor motorola
%define vendor_pretty Motorola
%define device_pretty G4 Plus
%define installable_zip 1
%define android_config \
#define WANT_ADRENO_QUIRKS 1 \
#define QCOM_BSP 1 \
%{nil}
%define straggler_files \
   /init.mmi.boot.sh\
   /init.mmi.touch.sh\
   /init.mmi.laser.sh\
   /init.oem.hw.sh\
   /init.qcom.bt.sh\
   /init.qcom.ril.sh\
%{nil}
%include rpm/dhd/droid-hal-device.inc
