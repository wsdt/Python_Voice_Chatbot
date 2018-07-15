#!/usr/bin/python3
import configure
from mgr.mgr_voices import liveSpeech


def main():
    # Configure confidential before if there is a confidential.py
    configure.config_confidential()

    # Start Voice Recognition
    liveSpeech()


if __name__ == '__main__':
    main()
