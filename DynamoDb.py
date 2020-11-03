
import boto3


__TableName__ = "People"
Primary_Column_Name = 'Sr'
Primary_Key = 1
columns=["Age","First", "Last"]


client = boto3.client('dynamodb')

DB =     boto3.resource('dynamodb')
table = DB.Table(__TableName__)


response = table.get_item(
            Key={
                Primary_Column_Name:Primary_Key
            }
        )

response["Item"]


Primary_Key = 5

response = table.put_item(
    Item={
        Primary_Column_Name:Primary_Key,
        columns[0]: 44,
        columns[1] :"Youtube",
        columns[2]: "Python"
            }
        )

response["ResponseMetadata"]["HTTPStatusCode"]


Primary_Key = 5 response = table.delete_item( Key={ Primary_Column_Name: Primary_Key } ) response

Describe Method


response = client.describe_table(TableName = __TableName__)
response



from boto3.dynamodb.conditions import Key
response = table.query(
    KeyConditionExpression=Key('Sr').eq(0)
)


response["Items"]


from boto3.dynamodb.conditions import Key, Attr
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('People')

response = table.scan(
    FilterExpression=Attr('Sr').gte(0)
)


for x in response["Items"]:
    print(x)

{'Sr': Decimal('3'), 'Last': 'Shah', 'First': 'Suhas', 'Age': Decimal('58')}
{'Sr': Decimal('4'), 'Last': 'Shah', 'First': 'Karan', 'Age': Decimal('22')}
{'Sr': Decimal('1'), 'Last': 'Shah', 'First': 'Nitin', 'Age': Decimal('61')}
{'Sr': Decimal('0'), 'Last': 'Shah', 'First': 'Soumil', 'Age': Decimal('24')}


from boto3.dynamodb.conditions import Key, Attr
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('People')

response = table.scan(
    FilterExpression=Attr('Age').gte(28)
)

response
