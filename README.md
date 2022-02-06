# SSHConfGen
Generates config files for SSH, for cloud platforms such as AWS, Azure, GCP, Linode etc.

## Usage
Include the generated configs to the main ssh config
```
nano ~/.ssh/config

Include ~/.ssh/custom/*.sshcfg
```
Move generated *.sshcfg from outputs, to ~/.ssh/custom/ (else use the config to set this path)


## Configuration Parameters
* Path to keystores

# TODO
* Azure
* GCP
* Linode
