# SSHConfGen
Generates config files for SSH, for cloud platforms such as AWS, Azure, GCP, Linode etc.
Currently, supports only AWS and runs of a cached API call (aws.json). 
Seeks to alleviate the pains when having to access (and maintain) a large number of VMs, possibly across multiple AWS accounts, and each time having to either do a history search or manually fetch connection info from the AWS console.


## Usage

Generate cached API response (to be automated in the next release)
```
aws ec2 describe-instances --profile <aws_profile> --region <us-west-1>  > aws.json
<region -- for ex. us-west-1>
```

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
* Check for paginated API responses