import os
import json
import csv
from datetime import datetime

from config import delimiter,frmt,profiles,regions,params,tags_list

def format_tags(tags):
    tags = []
    for tag in tags_list:
        tags.append("Tags[?Key==`{}`].Value".format(tag)) ## windows
        #tags.append("Tags[?Key=='{}'].Value".format(tag)) ## linux
    return tags

def describe_all_instances(profiles,regions,params,delimiter,frmt):
    print ("Getting all instances")
    os.chdir(os.path.join(path,'aws-instances-details/all-instances'))
    header = ["Profile","Region"]
    for param in params:
        header.append(param)
    for tag in tags_list:
        header.append(tag)
    print ("Instances Params are {0}".format(header))
    formatted_tags = format_tags(tags_list)
    print(",".join(formatted_tags))
    for profile in profiles:
        for region in regions:
            print ("getting {0} instances from region {1}".format(profile,region))
            # os.system('aws ec2 --profile {0} --region {1} describe-instances --query "Reservations[*].Instances[*].[InstanceId,Tags[?Key==`Name`].Value,ImageId,State,LaunchTime]" --output json > {0}_{1}.json'.format(profile,region))		
            command = 'aws ec2 --profile {0} --region {1} describe-instances --query "Reservations[*].Instances[*].[{2},{3}]" --output json > {0}_{1}.json'.format(profile,region,",".join(params),",".join(formatted_tags))		
            os.system(command)
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
                                json_parsed = [profile,region]
                                print ("DEBUG JSON AVANT BOUCLE",json_parsed)
                                for info in instance:
                                    if type(info) == list:
                                        print ("INFO = LIST", info)
                                        json_parsed.append(info[0])
                                    elif type(info) == str:
                                        try:
                                            print("INFO DATETIME",info)
                                            convert_datetime_object = datetime.strptime(str(info),'%Y-%m-%dT%H:%M:%S.%fZ')
                                            pretty_datetime_object = convert_datetime_object.strftime(frmt)
                                            json_parsed.append(pretty_datetime_object)
                                        except ValueError:
                                            json_parsed.append(info)
                                    elif type(info) == dict:
                                        try:
                                            json_parsed.append(info["Name"])
                                        except KeyError:
                                            json_parsed.append(info)
                                    else:
                                        json_parsed.append(info)
                                print(json_parsed)
                                csv_writer.writerow(json_parsed)
                    except IndexError:
                        print ("There are no existing instances for {0} account on region {1}".format(profile,region))
                        continue
        print ("Deleting all json file from folder")
        [os.remove(json) for json in os.listdir(os.path.join(path,'aws-instances-details/all-instances')) if json[-4:] == "json"]

if __name__ == "__main__":
	path = os.path.dirname(os.path.abspath(__file__))
	try:
		os.mkdir(os.path.join(path, "aws-instances-details"))
		os.mkdir(os.path.join(path, "aws-instances-details/all-instances"))	
	except:
		print("Folder already exists")

	describe_all_instances(profiles,regions,params,delimiter,frmt)
