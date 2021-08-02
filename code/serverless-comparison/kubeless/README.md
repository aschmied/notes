# Kubeless

## Deployment

1. Deploy nmx-dev
1. Check your Kubernetes context:

        kubectl config current-context

    If it is not `nmx-dev`, set it by doing the following in cloud_clusters:

        mvn cloud:kube-dashboard -Dkube.cluster=nmx-dev -Daws.profile=nmx-dev

1. Download the [Kubeless binary](https://github.com/kubeless/kubeless/releases) and place it on your PATH
1. Download the [Kubeless RBAC YAML](https://github.com/kubeless/kubeless/releases) for the same version
1. Create a namespace for Kubeless and deploy it:

        kubectl create namespace kubeless
        kubectl create -f kubeless-v1.0.5.yaml

1. Check Kubeless pod status:

        kubectl get pods --namespace kubeless

    You should have three kubeless-controller-manager replicas running.

1. Display the server config to see the available runtimes:

        kubeless get-server-config

    If you see the following error, then Kubeless could not find your Kubernetes config:

        FATA[0000] Can not get kubernetes config: CreateFile Z:\.kube\config: The system cannot find the path specified.

    Work around it by setting the `KUBECONFIG` environment variable:

        KUBECONFIG=c:\Users\<user>\.kube\config

## Deploying the App

1. Change to the "kubeless" directory of this repo
1. Deploy the function:

        kubeless function deploy hello-world-kubeless
            --runtime python3.7 \
            --from-file app.py \
            --handler app.handler

1. Issue a test call to the function:

        kubeless function call hello-world-kubeless

1. Create an ingress to expose the function:

        kubeless trigger http create get-hello-world-kubeless \
            --gateway nginx \
            --function-name hello-world-kubeless \
            --path hello-world-kubeless \
            --hostname hello-world-kubeless.nmx.ca

1. To test the function, use the Host header to trick the Ingress controller into thinking your request is to the hostname given in the `trigger create` command above:

        curl -H "Host: hello-world-kubeless.nmx.ca" a639274c8169911ea811212567ee8a9b-dc309ed3f66c078a.elb.us-east-1.amazonaws.com/hello-world-kubeless

## Clean Up

1. Delete the app

        kubeless trigger http delete get-hello-world-kubeless
        kubeless function delete hello-world-kubeless

1. Remove Kubeless

        kubectl delete -f kubeless-v1.0.5.yaml

## References

* [Kubeless deployment](https://kubeless.io/docs/quick-start/)
* [Exposing a Kubeless Function](https://kubeless.io/docs/http-triggers/)
