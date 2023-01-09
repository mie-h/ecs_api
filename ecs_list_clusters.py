from ecs_def_client import ecs_client
import json

def list_clusters():
    
    lv_response = ecs_client.list_clusters()

    lv_cluster_arns = lv_response.get("clusterArns","")
    if not lv_cluster_arns:
        print(f"Empty cluster arns")
        return 

    print(json.dumps(lv_cluster_arns))

    return 0,lv_cluster_arns