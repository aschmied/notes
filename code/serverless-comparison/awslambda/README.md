# AWS Lambda Using Serverless Framework

## Deployment

Nothing to do. The AWS Lambda platform is available alongside our other AWS services.

## Deploying the App

1. Install [Node 6](https://nodejs.org/en/download/package-manager/) or later
1. Install Serverless Framework:

        npm install -g serverless

1. Configure your AWS credentials if you haven't already:

        serverless config credentials --provider aws --key <aws-access-key-id> --secret <aws-secret-access-key>

1. Change to the "awslambda" directory of this repo
1. Deploy the service:

        serverless deploy

    Take note of the "endpoint" in the log output.

1. Test the function with the endpoint from above:

        curl https://<api-gateway-id>.execute-api.us-east-1.amazonaws.com/dev/hello

## Clean Up

1. Remove the app

        serverless remove

## References

* [Getting Started with Serverless Framework](https://serverless.com/framework/docs/getting-started/)
* [AWS Python Example](https://serverless.com/framework/docs/providers/aws/examples/hello-world/python/)
* [AWS Lambda CLI Reference](https://serverless.com/framework/docs/providers/aws/cli-reference/)
