Fingerprint # (microarray) the Begin 
ifeq ($ (strip $ (MTK_FINGERPRINT_SUPPORT)), yes or The) 
PRODUCT_PACKAGES + = fingerprintd 
PRODUCT_PACKAGES + = fingerprint.default 
PRODUCT_COPY_FILES + = device / DROI / leagoo3 / madev / bin directory / fingerprintd: system / bin directory / fingerprintd 
PRODUCT_COPY_FILES + = frameworks / native / data / etc / android.hardware.fingerprint.xml: $ (TARGET_COPY_OUT_VENDOR) /etc/permissions/android.hardware.fingerprint.xml 
PRODUCT_COPY_FILES + = device / droi / leagoo3 / madev / lib / hw / fingerprint .ma120n.so: $ (TARGET_COPY_OUT_VENDOR) /lib/hw/fingerprinted.ma120n.so 
PRODUCT_COPY_FILES + = device / droi / leagoo3 / madev / lib / libfprint-x32.so: $ (TARGET_COPY_OUT_VEPAplicferent-x32.so: $ (TARGET_COPY_OUT_VENDrpactfextr.x32.so: $ (TARGET_COPY_OUT_VEP);)
PRODUCT_COPY_FILES + = device / droi / leagoo3 / madev / lib / libma-fpservice.so: $ (TARGET_COPY_OUT_VENDOR) /lib/libma-fpservice.so 
endif 
# Fingerprint End
