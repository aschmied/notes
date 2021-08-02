# Knative

## Deployment

1. Deploy nmx-dev
1. Check your Kubernetes context:

        kubectl config current-context

    If it is not `nmx-dev`, set it by doing the following in cloud_clusters:

        mvn cloud:kube-dashboard -Dkube.cluster=nmx-dev -Daws.profile=nmx-dev

1. Download the [Gloo binary](https://github.com/solo-io/gloo/releases) and place it on your PATH
1. Install the Knative Serving component:

        glooctl install knative --dry-run
        glooctl install knative

1. Check Gloo and Knative pod status

        kubectl get pods --namespace gloo-system
        kubectl get pods --namespace knative-serving

    You should have 10 pods running across the two namespaces.

## Deploying the App

1. Change to the "knative" directory of this repo
1. Look at "service.yaml" to see the app definition
1. Deploy the app:

        kubectl apply -f service.yaml

1. Query Gloo for the external proxy URL for Knative:

        glooctl proxy url --name knative-external-proxy

1. Get the default service URL assigned by Gloo to our hello-world-knative service:

        kubectl get ksvc hello-world-knative -n hello-world-knative --output=custom-columns=NAME:.metadata.name,URL:.status.url

1. Now send a request to the external proxy URL with a Host header to trick the Gloo gateway into thinking we typed the service URL in our address bar:

        curl -H "Host: hello-world-knative.hello-world-knative.example.com" <external-proxy-url>

## Clean Up

1. Delete the app:

        kubectl delete -f service.yaml

1. Delete Knative. I did not find a supported method for this. The following gave some errors, but seemed to get most of the resources (I was in nmx-dev. We need to resolve this before testing in nmx-test):

        glooctl install knative --dry-run > out.yaml
        kubectl delete -f out.yaml

## References

* [Knative deployment](https://knative.dev/docs/install/knative-with-gloo/)
* [Knative research day](https://docs.google.com/document/d/1DEyZlbZTWwB4cbGW7prfR_vGpUAJ3Air4ShwaksRwEg/edit#). Discusses what Knative provides and the Knative deployment options
