#!/usr/bin/python3

configs = list(config.split("#")[0].strip() for config in open("config", "r") if config.strip() and config.split("#")[0].strip())
print(configs[0])
