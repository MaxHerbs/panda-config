# PandA Configure
A script to reconfigure PV on a PandA over channel access. 
Tested on version `0.10.0` on firmware `4.0b1`. 

# Using the Script
Set up the `config.yaml`. Configure the IOC prefix for the target panda.
The current config will work, but changes can be made in the yaml file if a different PV setup is desired.

Each block should have at least a `name`, and at least one item in `puts`.

```yaml
blocks:
  - name: CLOCK1
    puts: 
      label: Configurable clocks 1
      enable: PCAP.ACTIVE
```

PV names are built by concatenating `iocPrefix + name + puts[i]` so any accessible PV can be added within its own block in the config file.

To run the script,

```bash 
$ python main.py
```