import boto3

TableName = "People"
columns=["Age","First", "Last"]

client = boto3.client('dynamodb')

DB = boto3.resource('dynamodb')
table = DB.Table(TableName)

PrimaryColumn = 'Sr'
PrimaryKey = 1
response = table.get_item(Key={PrimaryColumn:PrimaryKey})

PrimaryKey = 5
response = table.put_item(Item={PrimaryColumn:PrimaryKey,  columns[0]: 44, columns[1] :"Youtube",  columns[2]: "Python" })

PrimaryKey = 5 
response = table.delete_item( Key={ PrimaryColumn: PrimaryKey } ) 

response = client.describe_table(TableName = TableName)


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
