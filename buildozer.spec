
name: Build NEON GFX TOOL APK

on:
  workflow_dispatch:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-22.04

    steps:
      - name: Checkout source
        uses: actions/checkout@v4

      - name: Set up Java
        uses: actions/setup-java@v4
        with:
          distribution: temurin
          java-version: '17'

      - name: Set up Android SDK
        run: |
          echo "ANDROID_HOME=/usr/local/lib/android/sdk" >> "$GITHUB_ENV"
          echo "ANDROID_SDK_ROOT=/usr/local/lib/android/sdk" >> "$GITHUB_ENV"

          SDKMANAGER=/usr/local/lib/android/sdk/cmdline-tools/latest/bin/sdkmanager

          yes | "$SDKMANAGER" --licenses

          "$SDKMANAGER" --install \
            "platform-tools" \
            "platforms;android-35" \
            "build-tools;35.0.0"

          echo "/usr/local/lib/android/sdk/platform-tools" >> "$GITHUB_PATH"
          echo "/usr/local/lib/android/sdk/build-tools/35.0.0" >> "$GITHUB_PATH"

      - name: Check AIDL
        run: |
          AIDL=/usr/local/lib/android/sdk/build-tools/35.0.0/aidl
          if [ ! -x "$AIDL" ]; then
            echo "AIDL NOT FOUND"
            exit 1
          fi
          echo "AIDL FOUND"

      - name: Install dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y \
            python3-pip python3-venv git zip unzip \
            build-essential autoconf libtool pkg-config \
            zlib1g-dev libncurses5-dev libffi-dev libssl-dev

      - name: Build APK
        run: |
          python3 -m venv .venv
          . .venv/bin/activate
          pip install --upgrade pip
          pip install buildozer cython==0.29.36
          buildozer android debug

      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: NEON-GFX-TOOL-APK
          path: bin/*.apk
          
