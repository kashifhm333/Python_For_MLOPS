logs = [
    {"timestamp": "10:00", "service_name": "auth-service", "status_code": 200},
    {"timestamp": "10:01", "service_name": "db-service", "status_code": 500},
    {"timestamp": "10:02", "service_name": "auth-service", "status_code": 500},
    {"timestamp": "10:03", "service_name": "db-service", "status_code": 500},
    {"timestamp": "10:04", "service_name": "ui-service", "status_code": 200}
]

def status_code(logs):
    set_of_unique_services = set()
    unique_count = 0
    for log in logs:
        if log["status_code"] == 500:
            set_of_unique_services.add(log["service_name"])
                
    print("Unique services with status code 500:")
    for service in set_of_unique_services:
        print(service)
        
        
status_code(logs)