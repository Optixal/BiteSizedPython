#!/usr/bin/python3

configs = dict(config.split("#")[0].strip().split(" ") for config in open("config", "r") if config.strip() and config.split("#")[0].strip())
print(configs["Test"])
