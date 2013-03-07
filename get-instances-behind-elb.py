#!/usr/bin/python -tt
"""
A script for retriving a list of EC2 instances receiving traffic from a particular
ELB load balancer

Requires boto. 

Usage: get-instances-behind-elb.py <s3 access key> <s3 secret key> <ELB Name> [--region=<ELB region>]
"""
import sys
import boto
from boto.ec2.elb import ELBConnection


def get_instance_list(access_key, secret_key, elb_name):
  instances_and_ips = []
  conn = ELBConnection(access_key, secret_key)
  load_balancers = conn.get_all_load_balancers()
  for lb in load_balancers:
    if lb.name == elb_name:
      for instance in lb.instances:
        instances_and_ips.append(get_instance_ip(access_key, secret_key, instance.id))
  return instances_and_ips
    
def get_instance_ip(access_key, secret_key, instance_id):
  ec2_conn = boto.connect_ec2(access_key, secret_key)
  reservations = ec2_conn.get_all_instances(instance_id)
  return instance_id, reservations[0].instances[0].ip_address

def main():
  try:
    args = sys.argv[1:]
    if args[2]:
      all_instances_with_ips = get_instance_list(args[0], args[1], args[2])
      print '\n' + args[2]
      print '-'*len(args[2]) + '\n'
      print 'Instance:  IP:'
      print '---------  ---'
      for inst in all_instances_with_ips:
        print inst[0], inst[1]
    else:
      raise Exception('IndexError')
      sys.exit(1)
  except IndexError:
    print 'Usage: get-instances-behind-elb.py <s3 access key> <s3 secret key> <ELB Name> [--region=<ELB region>]'
    sys.exit(1)


if __name__ == '__main__':
  main()