# SSHConfGen
Generates config files for SSH, for cloud platforms such as AWS, Azure, GCP, Linode etc.
Currently, supports only AWS and runs of a cached API call (aws.json). 

## Usage
Include the generated configs to the main ssh config
```
nano ~/.ssh/config

Include ~/.ssh/custom/*.sshcfg
```
Move generated *.sshcfg from outputs, to ~/.ssh/custom/ (else use the config to set this path)


## Configuration Parameters
* **platform** Select between AWS, Azure, GCP, Linode etc.
* **pathToKeystore** Folder path of private keys 
* **defaultUser** In case detection of OS user isn't available, then use this
* **pathToGenerated** Where to put the generated configuration(s)
* **filePrefix** Prefix to be used for the generated configuration file(s)
* **hostTag** Specify the resource tag which will be used for the Host field 
* **groupTag** Specify the resource tag which will be used incase of you wish to generate separate configuration files 

# TODO
* AWS API
* Azure API
* GCP API
* Linode API
* Move configuration to an ini file