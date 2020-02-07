# choose your csv delimiter below
delimiter =';'

# edit your expected datetime format below see http://strftime.org/
frmt = '%Y-%m-%d %H:%M:%S'

# add your aws profiles below
profiles= [""]

# add your regions below see https://docs.aws.amazon.com/general/latest/gr/rande.html
regions = ["us-east-1","us-east-2","us-west-1","us-west-2","ca-central-1","eu-central-1","eu-west-1","eu-west-2","eu-west-3","eu-north-1","ap-east-1","ap-northeast-1","ap-northeast-2","ap-southeast-1","ap-southeast-2","ap-south-1","sa-east-1"]

# data to put in the csv see https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instances.html to add params
params = ["InstanceId","ImageId","State","LaunchTime"]

## add here the instance tags you want to get in the csv see in the aws management console to find out what tags are the instances tags
tags_list = ["Name","Owner"]
		