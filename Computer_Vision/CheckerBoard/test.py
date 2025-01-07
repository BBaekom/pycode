from diagrams import Diagram, Cluster
from diagrams.k8s.compute import Pod
from diagrams.k8s.network import Ingress, Service
from diagrams.k8s.storage import PersistentVolume
from diagrams.onprem.client import User
from diagrams.generic.database import SQL
from diagrams.generic.storage import Storage

with Diagram("Kubernetes-Based Architecture", direction="LR", show=False):
    user = User("User (Flutter Frontend)")

    # Kubernetes entry (Load Balancer or Ingress)
    with Cluster("Kubernetes Cluster"):
        k8s_entry = Ingress("Kubernetes Entry (Load Balancer or Ingress)")
        user >> k8s_entry

        # Spring Boot instances in the cluster
        with Cluster("Spring Boot Instances"):
            spring_boot = [Pod("Spring Boot Instance") for _ in range(3)]

        # MySQL instances in the cluster
        with Cluster("MySQL Databases"):
            mysql = [SQL("MySQL Instance") for _ in range(3)]

        # Llama 3.1 model servers
        with Cluster("Llama 3.1 LLM Servers"):
            llama_servers = [Pod("Llama 3.1 Server") for _ in range(3)]

        # EEVE model servers
        with Cluster("EEVE LLM Servers"):
            eeve_servers = [Pod("EEVE Server") for _ in range(3)]

        # Connections inside Kubernetes
        k8s_entry >> spring_boot

        # Iterate over each Spring Boot instance and connect to each MySQL instance
        for sb in spring_boot:
            for db in mysql:
                sb >> db

        # spring_boot >> llama_servers
        # spring_boot >> eeve_servers

    # Static file storage outside Kubernetes
    static_storage = Storage("Static File Storage")
    user >> static_storage
