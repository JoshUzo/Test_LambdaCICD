import json
import os
import subprocess
import boto3

# Hardcoded AWS Credentials (Bad Practice) 
AWS_ACCESS_KEY_ID = "AKIAFAKEACCESSKEY1234"
AWS_SECRET_ACCESS_KEY = "FAKESECRETKEY5678"

def run_shell_command():
    # Running shell commands unsafely (Command Injection Risk) 
    return subprocess.Popen("ls -la", shell=True, stdout=subprocess.PIPE).communicate()[0]

def insecure_eval(user_input):
    # Using eval() unsafely (Remote Code Execution Risk) 
    return eval(user_input)

def lambda_handler(event, context):
    # Accessing environment variables insecurely 
    secret_key = os.getenv("SECRET_KEY", "default_secret")

    # Simulating a security issue
    output = run_shell_command()
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            "message": "Hello from Lambda!",
            "output": output.decode("utf-8"),
            "eval_result": insecure_eval("2 + 2")  #  Potential security risk 
        })
    }
