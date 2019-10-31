# monitor-aws-ec2-instances
This is a small and modest python script to output in a csv file all your aws ec2 instances status & details

# 1) Install awscli package

If python is installed just run in a prompt the command below (the working directory must be the aws folder:
It will install awscli on your python environment, you can use virtualenv if you don't to pollute your python

```python
cd monitor-aws-ec2-instances
pip install -r requirements.txt
```

# 2) Set up your .aws folder

To do before running the script : 

Add all aws profiles and keys inside the file .aws\credentials (example in .aws folder attached)
Then copy the folder .aws inside C:\Users\<yourUser> for windows user else ~/.aws for Unix

In the config file add your profiles and leave the output to text

In the script add the regions and profiles you want to use.
The two lists <regions> & <profiles> must follow the below naming rule:
["Region1";"Region2";"Region3"]

# 3) Known Issues:

If you get this error json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
means that the awscli command wasn't executed properly. Check your credentials file to see if the profile is active and is working

Sometimes not all json files will be deleted if the script fails.

# 4Â) To d

Documentation
