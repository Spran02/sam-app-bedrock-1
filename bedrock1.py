from helper import *
import boto3
import uuid

# bedrock_agent = boto3.client(service_name='bedrock-agent', region_name='us-east-1')
# bedrock_agent_runtime = boto3.client(service_name='bedrock-agent-runtime', region_name='us-east-1')

# roleArn = 'arn:aws:iam::632178947285:role/service-role/AmazonBedrockExecutionRoleForAgents_1AH652L5RD2'

# create_agent_response = bedrock_agent.create_agent(
#     agentName='test-local-agent5',
#     foundationModel='amazon.nova-micro-v1:0',
#     instruction="""You are an advanced AI agent that must get the utc time and you must add 2 numbers.""",
#     agentResourceRoleArn=roleArn
# )

# print("Create agent response: ", create_agent_response)

# agentId = create_agent_response['agent']['agentId']
# print(f"Agent ID: {agentId}")


# wait_for_agent_status(
#     agentId=agentId, 
#     targetStatus='NOT_PREPARED'
# )

# bedrock_agent.prepare_agent(
#     agentId=agentId
# )

# wait_for_agent_status(
#     agentId=agentId, 
#     targetStatus='PREPARED'
# )

# create_agent_alias_response = bedrock_agent.create_agent_alias(
#     agentId=agentId,
#     agentAliasName='MyAgentAlias1',
# )

# agentAliasId = create_agent_alias_response['agentAlias']['agentAliasId']

# print(f"Agent Alias ID: {agentAliasId}")

# wait_for_agent_alias_status(
#     agentId=agentId,
#     agentAliasId=agentAliasId,
#     targetStatus='PREPARED'
# )

# create_agent_action_group_response = bedrock_agent.create_agent_action_group(
#     actionGroupName='local_agent_action_group1',
#     agentId=agentId,
#     actionGroupExecutor={
#         'lambda': 'arn:aws:lambda:us-east-1:632178947285:function:sam-app-bedrock-test1-HelloWorldFunction-bGz1zqhaq10U'
#     },
#     functionSchema={
#         'functions': [
#             {
#                 'name': 'add_two_numbers',
#                 'description': 'adds 2 numbers.',
#                 'parameters': {
#                     'number1': {
#                         'description': 'first number to add',
#                         'required': True,
#                         'type': 'string'
#                     },
#                     'number2': {
#                         'description': 'second number to add',
#                         'required': True,
#                         'type': 'string'
#                     },
#                 }
#             },            
#             {
#                 'name': 'get_time',
#                 'description': 'gets utc time. ',
#                 'parameters': {}
                
#             }
#         ]
#     },
#     agentVersion='DRAFT',
# )

# actionGroupId = create_agent_action_group_response['agentActionGroup']['actionGroupId']
# print(f"Action Group ID: {actionGroupId}")


# wait_for_action_group_status(
#     agentId=agentId, 
#     actionGroupId=actionGroupId,
#     targetStatus='ENABLED'
# )

# bedrock_agent.prepare_agent(
#     agentId=agentId
# )

# wait_for_agent_status(
#     agentId=agentId,
#     targetStatus='PREPARED'
# )


# bedrock_agent.update_agent_alias(
#     agentId=agentId,
#     agentAliasId=agentAliasId,
#     agentAliasName='MyAgentAlias1',
# )

# wait_for_agent_alias_status(
#     agentId=agentId,
#     agentAliasId=agentAliasId,
#     targetStatus='PREPARED'
# )


agentId='TUD99R4O6E'
agentAliasId='CVBL5FS7HT'

sessionId = str(uuid.uuid4())
message = "what is the utc time now?"

invoke_agent_and_print(
    agentId=agentId,
    agentAliasId=agentAliasId,
    inputText=message,
    sessionId=sessionId,
    enableTrace=True
)