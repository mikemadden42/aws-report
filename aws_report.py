#!/usr/bin/env python3
"""Summary AWS resources."""

import boto3


def list_instances():
    """List ec2 instances."""
    ec2 = boto3.resource("ec2")

    print("RUNNING EC2 INSTANCES")
    print("=====================")
    instances = ec2.instances.filter(
        Filters=[{"Name": "instance-state-name", "Values": ["running"]}]
    )
    for i in instances:
        print(
            i.id,
            i.key_name,
            i.architecture,
            i.instance_type,
            i.private_ip_address,
            i.launch_time,
            i.state["Name"],
        )
    print()

    print("STOPPED EC2 INSTANCES")
    print("=====================")
    instances = ec2.instances.filter(
        Filters=[{"Name": "instance-state-name", "Values": ["stopped"]}]
    )
    for i in instances:
        print(
            i.id,
            i.key_name,
            i.architecture,
            i.instance_type,
            i.private_ip_address,
            i.launch_time,
            i.state["Name"],
        )
    print()


def list_buckets():
    """List s3 buckets."""
    storage = boto3.resource("s3")

    print("S3 BUCKETS")
    print("==========")
    for bucket in storage.buckets.all():
        print(bucket.name)
    print()


def list_users():
    """List iam users"""
    iam = boto3.client("iam")

    print("IAM USERS")
    print("=========")
    users = iam.list_users()
    for key in users["Users"]:
        print(key["UserName"])
    print()


def main():
    """Summary AWS resources."""
    list_instances()
    list_buckets()
    list_users()


if __name__ == "__main__":
    main()
