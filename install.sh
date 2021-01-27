#!/bin/sh

apt-get install libwayland-server0 libappindicator1 fonts-liberation libgbm1 -y -qq
rm -r google-chrome*
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
dpkg -i google-chrome*.deb
CHROME_DRIVER_VERSION=`curl -sS https://chromedriver.storage.googleapis.com/LATEST_RELEASE`
wget -N https://chromedriver.storage.googleapis.com/88.0.4324.96/chromedriver_linux64.zip -P ~/
unzip ~/chromedriver_linux64.zip -d ~/
rm ~/chromedriver_linux64.zip
python3 -m venv $PWD+`/env`
mv -f ~/chromedriver $PWD+`/env/bin/chromedriver`
chown root:root $PWD+`/env/bin/chromedriver`
chmod 0755 $PWD+`/env/bin/chromedriver`
echo "selenium installed successfully."
