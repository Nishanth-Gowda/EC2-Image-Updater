## EC2 Instance Type Upgrader Lambda Function

This AWS Lambda function is designed to automatically upgrade the instance type of an Amazon Elastic Compute Cloud (EC2) instance if it is not of the desired type. The function is triggered by an AWS CloudWatch Events rule, which is typically set up to respond to specific events, such as EC2 instance launches or state changes.

## How It Works

1. **Event Trigger**: The Lambda function is triggered by an event, typically an EC2 instance launch event, which is passed as the `event` parameter to the `lambda_handler` function.

2. **Initialization**: The function starts by initializing the AWS SDK for Python (Boto3) client for EC2. This client is used to interact with EC2 instances and modify their attributes.

3. **Instance ID Extraction**: The `instance_id` is extracted from the event. This is the unique identifier for the EC2 instance that triggered the Lambda function.

4. **Instance Description**: The `describe_instances` method is called to retrieve detailed information about the EC2 instance using its `instance_id`. This information is stored in the `response` variable.

5. **Instance Type Check**: The function checks the instance type of the EC2 instance obtained from the response. If the instance type is not equal to 'm1.large', it proceeds with the instance upgrade.

6. **Instance Stop**: First, the function stops the EC2 instance using the `stop_instances` method. It then waits for the instance to stop using a waiter to ensure that the instance is in a stopped state before proceeding.

7. **Instance Type Modification**: After the instance is stopped, the function uses `modify_instance_attribute` to change the instance type to 'm1.large'.

8. **Instance Start**: Once the instance type is modified, the function starts the EC2 instance using the `start_instances` method.

9. **Logging**: Throughout the process, the function prints information about the instance ID and its type. In case of any errors, it catches exceptions and logs them.

10. **Response**: Finally, the function returns a JSON response with a 200 status code and a simple message.

## Usage

To use this Lambda function effectively:

- **Event Configuration**: Set up an AWS CloudWatch Events rule to trigger this Lambda function when specific EC2 events occur (e.g., instance launches or state changes).

- **IAM Permissions**: Ensure that the Lambda function's execution role has the necessary IAM permissions to describe, stop, and start EC2 instances, as well as modify their attributes.

- **Instance Type**: Adjust the desired instance type ('m1.large' in this example) to match your requirements.

- **Error Handling**: Customize error handling to meet your needs, such as sending notifications or handling specific error scenarios.

This Lambda function can be a valuable tool for automatically managing EC2 instances by ensuring they conform to your desired instance type.
