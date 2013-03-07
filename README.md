get-instances-behind-elb
========================

A script for retriving a list of EC2 instances receiving traffic from a particular Amazon ELB (Elastic Load Balancing) load balancer

Requires **boto**. 

>Usage: get-instances-behind-elb.py `<s3 access key`> `<s3 secret key`> `<ELB Name`> [--region=`<ELB region`>]

--region is not implemented yet - it will provide the option of specifying a region for the ELB
