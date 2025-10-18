def get_message() -> str:
    """Return the message to print."""
    return "Hello World from AWS BuildGem!"


def main() -> None:
    print(get_message())


# Standard Python entry point (if you run locally)
if __name__ == "__main__":
    main()


# AWS Lambda handler
def lambda_handler(event, context):
    """
    AWS Lambda entry point.
    event: dict containing the event data.
    context: runtime information provided by Lambda.
    """
    message = get_message()
    print(message)  # Shows up in CloudWatch Logs
    return {
        "statusCode": 200,
        "body": message
    }
