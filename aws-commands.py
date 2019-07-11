import os
import json
import csv
from datetime import datetime
from awsconf import frmt, delimiter, params, profiles, regions

def describe_all_instances(profiles,regions,params,delimiter,frmt):
	print ("Getting all instances")
	os.chdir(os.path.join(path,'aws-instances-details/all-instances'))
	header = ["Profile","Region"]
	for param in params:
		header.append(param)
	print ("Instances Params are {0}".format(header))
	for profile in profiles:
		for region in regions:
			print ("getting {0} instances from region {1}".format(profile,region))
			os.system('aws ec2 --profile {0} --region {1} describe-instances --query "Reservations[*].Instances[*].[InstanceId,Tags[?Key==`Name`].Value,ImageId,State,LaunchTime"] --output json > {0}_{1}.json'.format(profile,region))		
	with open("aws-all-instance-details.csv","w",newline='') as file:
		csv_writer = csv.writer(file,delimiter=delimiter)
		csv_writer.writerow(header)
		for profile in profiles:
			for region in regions:
				print ("Opening {0} region {1} json file".format(profile,region))
				with open("{0}_{1}.json".format(profile,region),"r") as file1:
					jsonfile = json.loads(file1.read())
					try:
						for listInstance in jsonfile:
							for instance in listInstance:
								convert_datetime_object = datetime.strptime(str(instance[4]),'%Y-%m-%dT%H:%M:%S.%fZ')
								pretty_datetime_object = convert_datetime_object.strftime(frmt)
								json_parsed = [profile,region,instance[0],instance[1][0],instance[2],instance[3]["Name"],pretty_datetime_object]
								csv_writer.writerow(json_parsed)
					except (IndexError, json.decoder.JSONDecodeError) as e:
						print (e)
						print ("There are no existing instances or you don't have the rights for {0} account on region {1}".format(profile,region))
						pass
		print ("Deleting all json file from folder")
		[os.remove(json) for json in os.listdir(os.path.join(path,'aws-instances-details/all-instances')) if json[-4:] == "json"]

def describe_stopped_instances(profiles,regions,params,delimiter,frmt):
	print ("Getting all stopped instances")
	os.chdir(os.path.join(path,'aws-instances-details/stopped-instances'))
	header = ["Profile","Region"]
	for param in params:
		header.append(param)
	for profile in profiles:
		for region in regions:
			print ("getting {0} instances from region {1}".format(profile,region))
			os.system('aws ec2 --profile {0} --region {1} describe-instances --filters "Name=instance-state-name,Values=stopped" --query "Reservations[*].Instances[*].[InstanceId,Tags[?Key==`Name`].Value,ImageId,State,LaunchTime"] --output json > {0}_{1}.json'.format(profile,region))		
	with open("aws-stopped-instance-details.csv","w",newline='') as file:
		csv_writer = csv.writer(file,delimiter=delimiter)
		csv_writer.writerow(header)
		for profile in profiles:
			for region in regions:
				print ("Opening {0} region {1} json file".format(profile,region))
				with open("{0}_{1}.json".format(profile,region),"r") as file1:
					jsonfile = json.loads(file1.read())
					try:
						for listInstance in jsonfile:
							for instance in listInstance:
								convert_datetime_object = datetime.strptime(str(instance[4]),'%Y-%m-%dT%H:%M:%S.%fZ')
								pretty_datetime_object = convert_datetime_object.strftime(frmt)
								json_parsed = [profile,region,instance[0],instance[1][0],instance[2],instance[3]["Name"],pretty_datetime_object]
								csv_writer.writerow(json_parsed)
					except IndexError:
						print ("There are no existing instances for {0} account on region {1}".format(profile,region))
						pass
		print ("Deleting all json file from folder")
		[os.remove(json) for json in os.listdir(os.path.join(path,'aws-instances-details/all-instances')) if json[-4:] == "json"]
		
def describe_running_instances(profiles,regions,params,delimiter,frmt):
	print ("Getting all running instances")
	os.chdir(os.path.join(path,'aws-instances-details/running-instances'))
	header = ["Profile","Region"]
	for param in params:
		header.append(param)
	for profile in profiles:
		for region in regions:
			print ("getting {0} instances from region {1}".format(profile,region))
			os.system('aws ec2 --profile {0} --region {1} describe-instances --filters "Name=instance-state-name,Values=running" --query "Reservations[*].Instances[*].[InstanceId,Tags[?Key==`Name`].Value,ImageId,State,LaunchTime"] --output json > {0}_{1}.json'.format(profile,region))			
	with open("aws-running-instance-details.csv","w",newline='') as file:
		csv_writer = csv.writer(file,delimiter=delimiter)
		csv_writer.writerow(header)
		for profile in profiles:
			for region in regions:
				print ("Opening {0} region {1} json file".format(profile,region))
				with open("{0}_{1}.json".format(profile,region),"r") as file1:
					jsonfile = json.loads(file1.read())
					try:
						for listInstance in jsonfile:
							for instance in listInstance:
								convert_datetime_object = datetime.strptime(str(instance[4]),'%Y-%m-%dT%H:%M:%S.%fZ')
								pretty_datetime_object = convert_datetime_object.strftime(frmt)
								json_parsed = [profile,region,instance[0],instance[1][0],instance[2],instance[3]["Name"],pretty_datetime_object]
								csv_writer.writerow(json_parsed)
					except IndexError:
						print ("There are no existing instances for {0} account on region {1}".format(profile,region))
						pass
		print ("Deleting all json file from folder")
		[os.remove(json) for json in os.listdir(os.path.join(path,'aws-instances-details/all-instances')) if json[-4:] == "json"]
	
if __name__ == "__main__":
	path = os.path.dirname(os.path.abspath(__file__))
	try:
		os.mkdir(os.path.join(path, "aws-instances-details"))
		os.mkdir(os.path.join(path, "aws-instances-details/running-instances"))	
		os.mkdir(os.path.join(path, "aws-instances-details/stopped-instances"))	
		os.mkdir(os.path.join(path, "aws-instances-details/all-instances"))	
	except:
		print("Folder already exists")

	describe_all_instances(profiles,regions,params,delimiter,frmt)
	# describe_running_instances(profiles,regions,params,delimiter,frmt)
	# describe_stopped_instances(profiles,regions,params,delimiter,frmt)

