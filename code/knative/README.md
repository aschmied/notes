# Knative Eventing Example

Follows the example [here](https://knative.dev/docs/eventing/samples/helloworld/helloworld-go/).

## Notes

* akashv/helloworld-go is available on DockerHub, so you don't need to build it yourself

##  Deploy

1. Deploy Knative with Eventing as described in the [previous research day doc on Knative](https://docs.google.com/document/d/1DEyZlbZTWwB4cbGW7prfR_vGpUAJ3Air4ShwaksRwEg/edit#heading=h.602zovpnrnc2)
1. Deploy the service, trigger, and deployment and verify they are ready:

        kubectl apply --filename sample-app.yaml
        kubectl get deployments --namespace knative-samples
        kubectl get services --namespace knative-samples
        kubectl get triggers --namespace knative-samples

## Test

1. Get the pod name for the helloworld-go app and tails its logs:

        kubectl get pods --namespace knative-samples
        kubectl --namespace knative-samples logs --follow helloworld-go-<your-pod-hash> > out.txt

1. Deploy a cURL pod so send HTTP requests inside the cluster:

        kubectl --namespace knative-samples run curl --image=radial/busyboxplus:curl -it

1. Send a message to the helloworld.go app and exit the cURL pod:

        curl -v "default-broker.knative-samples.svc.cluster.local" \
            -X POST \
            -H "Ce-Id: 536808d3-88be-4077-9d7a-a3f162705f79" \
            -H "Ce-specversion: 0.3" \
            -H "Ce-Type: dev.knative.samples.helloworld" \
            -H "Ce-Source: dev.knative.samples/helloworldsource" \
            -H "Content-Type: application/json" \
            -d '{"msg":"**** Hello from the curl pod. ****"}'
        exit

1. Exit the log tailing and view the out.txt file. You should see a line like:

        Hello World Message from recevied event "**** Hello from the curl pod. ****"

    In my case this was followed by a spew of send/receive logs for the response message sent by helloworld-go. It appears that the filter in the trigger is not working as expected: only messages that satisfy the filters should be delivered to helloworld-go:

        filter:
          attributes:
            type: dev.knative.samples.helloworld
            source: dev.knative.samples/helloworldsource

    But the responses sent by helloworld-go meet neither of those criteria and are still received by the service.

## Clean up

1. Delete the app:

        kubectl delete --filename sample-app.yaml

1. Delete Knative. I did not find a supported method for this. The following gave some errors, but seemed to get most of the resources (I was in nmx-dev. We need to resolve this before testing in nmx-test):

        glooctl install knative --install-eventing --dry-run > out.yaml
        kubectl delete -f out.yaml
