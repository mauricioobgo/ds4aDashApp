import boto3, sys, os, yaml
import json

client = boto3.client("ecs", region_name="us-east-1")


client = boto3.session.Session(profile_name=profile).client("batch", region_name=region)
with open("environments/{0}/{1}/batch_jobs.yml".format(os.environ.get("ENVIRONMENT", "latest"), region)) as f:
  config = yaml.safe_load(f)
  for job in config["jobs"]:
    try:
      print("Registering Batch Job {0}".format(job["jobDefinitionName"]))
      response = client.register_job_definition(**job)
    except Exception as e:
      print(e)
      sys.exit(1)
response = client.register_task_definition(
        containerDefinitions=[
            {
                "name": "AmazonSampleImage",
                "image": "amazon/amazon-ecs-sample",
                "cpu": 0,
                "portMappings": [],
                "essential": True,
                "environment": [],
                "mountPoints": [],
                "volumesFrom": [],
                "logConfiguration": {
                    "logDriver": "awslogs",
                    "options": {
                        "awslogs-group": "/ecs/AWSSampleApp",
                        "awslogs-region": "us-east-1",
                        "awslogs-stream-prefix": "ecs"
                    }
                }
            }
        ],
        executionRoleArn="arn:aws:iam::585584209241:role/ecsTaskExecutionRole",
        family= "AWSSampleApp2",
        networkMode="awsvpc",
        requiresCompatibilities= [
            "FARGATE"
        ],
        cpu= "256",
        memory= "512")

print(json.dumps(response, indent=4, default=str))