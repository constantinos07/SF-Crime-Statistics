import producer_server

INPUT_FILE = "police-department-calls-for-service.json"

def run_kafka_server():
	# TODO get the json file path
    #input_file = INPUT_FILE

    # TODO fill in blanks
    producer = producer_server.ProducerServer(
        input_file=INPUT_FILE,
        topic="service.calls",
        bootstrap_servers="localhost:9091",
        client_id=None
    )

    return producer


def feed():
    producer = run_kafka_server()
    producer.generate_data()


if __name__ == "__main__":
    feed()
