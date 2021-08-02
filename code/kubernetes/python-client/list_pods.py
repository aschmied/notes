import logging
import subprocess

import kubernetes

kubernetes.config.load_kube_config()

CLUSTER_NAME = '<name>'
CLUSTER_API_ENDPOINT = '<url>'

# Requires AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY environment variables.

def get_token(cluster_name):
    args = ['C:\\Program Files\\kubernetes\\aws-iam-authenticator\\aws-iam-authenticator.exe', "token", "--cluster-id", cluster_name, "--token-only"]
    popen = subprocess.Popen(args, stdout=subprocess.PIPE)
    out, err = popen.communicate()
    if err:
        logging.error(err)
        logging.error('Exiting')
        sys.exit(1)
    return out.rstrip().decode('utf-8')

api_token = get_token(CLUSTER_NAME)
configuration = kubernetes.client.Configuration()
configuration.host = CLUSTER_API_ENDPOINT
configuration.verify_ssl = False
configuration.debug = True
configuration.api_key['authorization'] = 'Bearer ' + api_token
configuration.assert_hostname = True
configuration.verify_ssl = False
kubernetes.client.Configuration.set_default(configuration)

api = kubernetes.client.CoreV1Api()
pods = api.list_pod_for_all_namespaces(watch=False)
for pod in pods.items:
    print(f'{pod.status.pod_ip}\t{pod.metadata.namespace}\t{pod.metadata.name}')
