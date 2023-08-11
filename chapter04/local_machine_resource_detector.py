import socket
from opentelemetry.sdk.resources import Resource, ResourceDetector


class LocalMachineResourceDetector(ResourceDetector):
    def detect(self):
        hostname = socket.gethostname()
        return Resource.create(
            {
                "net.host.name": hostname,
            }
        )
