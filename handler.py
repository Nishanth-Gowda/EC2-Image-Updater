import json
import boto3

def lambda_handler(event, context):
    print(event)
    
    client = boto3.client('ec2')
    
    # Get the instance id
    instance_id = event['detail']['instance-id']
    
    # Calling describe instances passing the instance_id
    response = client.describe_instances(
        InstanceIds=[
            instance_id,  # Pass the actual instance ID
        ]
    )
      
    # Getting the type of the instance          
    instance_type = response['Reservations'][0]['Instances'][0]['InstanceType']
    
    print("Instance ID:", instance_id)
    print("Instance Type:", instance_type)
    
    if instance_type != 'm1.large':
        try:
            # Stop the instance
            client.stop_instances(InstanceIds=[instance_id])
            
            waiter = client.get_waiter('instance_stopped')
            waiter.wait(InstanceIds=[instance_id])
            
            # Change the instance type
            client.modify_instance_attribute(InstanceId=instance_id, Attribute='instanceType', Value='m1.large')
            
            # Start the instance
            client.start_instances(InstanceIds=[instance_id])
            
            print("Instance type changed and instance started.")
        except Exception as e:
            print("Error:", str(e))
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
